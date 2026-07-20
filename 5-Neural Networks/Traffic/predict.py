import sys
import cv2
import numpy as np
import tensorflow as tf

def predict_image(model_path, image_path):
    # 1 trained model
    model = tf.keras.models.load_model(model_path)

    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read image.")
        return
  
    resized_image = cv2.resize(image, (30, 30))

    resized_image = resized_image / 255.0
    
    input_tensor = np.expand_dims(resized_image, axis=0)

    predictions = model.predict(input_tensor)
 
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class] * 100
    
    print(f"\n🎯 Predicted Sign Category ID: {predicted_class}")
    print(f"📈 Confidence: {confidence:.2f}%")

if __name__ == "__main__":
    # Ensure correct terminal arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python predict.py model_name.h5 path_to_image.png")
        sys.exit(1)
        
    predict_image(sys.argv[1], sys.argv[2])