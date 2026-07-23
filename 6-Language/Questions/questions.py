import nltk
from pathlib import Path
import sys
import string
import math

# Automatically download missing resources if not present
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idf(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idf(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    files = {}
    dir_path = Path(directory)

    for file_path in dir_path.iterdir():
        if file_path.is_file() and file_path.suffix == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                files[file_path.name] = f.read()
                
    return files


def tokenize(document):
    """
    Given a document string, return a list of lowercased words.
    """
    words = nltk.word_tokenize(document.lower())
    
    filtered_words = [
        word for word in words
        if word not in string.punctuation and word not in nltk.corpus.stopwords.words("english")
    ]
    
    return filtered_words

def compute_idf(documents):
    total_docs = len(documents)
    
    doc_counts = {}
    for doc in documents:
        unique_words = set(doc)
        for word in unique_words:
            doc_counts[word] = doc_counts.get(word, 0) + 1
            
    idf_scores = {}
    for word, count in doc_counts.items():
        idf_scores[word] = math.log(total_docs / count)
        
    return idf_scores


def top_files(query, files, idfs, n):
    file_scores = {}
    for filename, file_words in files.items():
        total_score = 0

        for word in query:
            if word in file_words and word in idfs:
                tf = file_words.count(word)
                total_score += tf * idfs[word]
                
        file_scores[filename] = total_score

    sorted_files = sorted(file_scores, key=lambda f: file_scores[f], reverse=True)

    return sorted_files[:n]


def top_sentences(query, sentences, idfs, n):
    sentence_scores = {}

    for sentence, words in sentences.items():

        mwm = sum(idfs.get(word, 0) for word in query if word in words)

        matching_words_count = sum(1 for word in words if word in query)
        qtd = matching_words_count / len(words)

        sentence_scores[sentence] = (mwm, qtd)

    sorted_sentences = sorted(
        sentence_scores,
        key=lambda s: (sentence_scores[s][0], sentence_scores[s][1]),
        reverse=True
    )

    return sorted_sentences[:n]


if __name__ == "__main__":
    main()

