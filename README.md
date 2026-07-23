# 🤖 CS50 AI Projects 🚀

Welcome to my repository tracking my journey, assignments, and implementations for Harvard's **CS50 Introduction to Artificial Intelligence with Python**! 🎓💡

---

## 📁 Repository Structure

This repository is organized by project tracks, showcasing various AI concepts from search algorithms to reinforcement learning:

### 🔍 [0-Search](./0-Search)
* **`tictactoe/`** ❌⭕: An unbeatable AI opponent built using the **Minimax** adversarial search algorithm.
* Core AI search algorithms and optimization techniques implemented as part of the CS50 AI curriculum.

### 🧠 [4-Learning](./4-Learning)
* **`shopping/`** 🛍️: A Machine Learning model predicting user purchase intent using K-Nearest Neighbors (KNN).
* **`nim/`** 🕹️: An AI agent that trains itself to play the game of Nim perfectly using **Reinforcement Learning (Q-Learning)**.

### 🧠 [5-Neural Networks](./5-Neural Networks)

* **traffic/ 🚗**: A Convolutional Neural Network (CNN) built with **TensorFlow** and **OpenCV** to classify traffic signs with **98% accuracy**. Includes a `predict.py` script for real-time single-image prediction.

* **Methodology:** Used **OpenCV** to preprocess and resize the GTSRB dataset images into normalized tensors.
* **Architecture:** Built a deep **Convolutional Neural Network (CNN)** using **TensorFlow/Keras** featuring stacked **Conv2D** and **MaxPooling2D** layers (scaling from 32 to 64 filters) to extract complex geometric features.
*   **Regularization & Results:** Integrated a **Dropout** layer to eliminate overfitting, achieving a final evaluation accuracy of **98%** using the **Adam** optimizer.

  ### 🔍 Document Retrieval & NLP Question Answering Engine

An Information Retrieval (IR) system built with Python and NLTK that uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Query Term Density** scoring to answer user prompts using a document corpus.

## 📌 Features

* **Custom Tokenization Pipeline:** Text preprocessing using `nltk` to remove punctuation, normalize case, and filter out English stop words.
* **Global IDF Indexing:** Computes log-scaled Inverse Document Frequency scores across all text files in the corpus to identify high-value keywords.
* **TF-IDF Document Retrieval:** Ranks documents using TF-IDF matching to isolate the most relevant context file for a given prompt.
* **Context-Aware Sentence Extraction:** Ranks sentences using Matching Word Measure (IDF sum) and Query Term Density tie-breaking to extract exact, concise answers.

---


---

## 🛠️ Tech Stack & Tools

* **Course Framework:** CS50 AI 🏫
* **Language:** Python 🐍
* **Libraries:** Logic, Math, Random, Time, **TensorFlow (Keras), OpenCV, NumPy, Scikit-learn, NLTK**
* **Environment:** VS Code & Git 💻

---

## 🚀 How to Run the Projects

### Running Tic-Tac-Toe ❌⭕
1. Navigate to the project directory:
   ```bash
   
   cd 0-Search/tictactoe

### Running Traffic Classifier 🚗

1. Navigate to the project directory:
   ```bash
   cd 5-Neural Networks/traffic
   pip install -r requirements.txt
   python traffic.py gtsrb
   python predict.py path/to/image.png (to predict a single traffic sign image )

   
