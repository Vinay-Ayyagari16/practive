import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define dataset path
DATASET_PATH = '/home/thrymr/Downloads/archive'


# Load dataset using ImageDataGenerator
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = datagen.flow_from_directory(DATASET_PATH, target_size=(64, 64), batch_size=16, class_mode="categorical", subset="training")

val_data = datagen.flow_from_directory(DATASET_PATH, target_size=(64, 64),batch_size=16, class_mode="categorical", subset="validation")

# Print class labels
print("Class labels:", train_data.class_indices)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Build CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(train_data.class_indices), activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(train_data, validation_data=val_data, epochs=10)

# Save model
model.save("sign_language_model.h5")
print("Model saved successfully!")

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("sign_language_model.h5")

# Load class labels
labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
class_indices = {i: labels[i] for i in range(len(labels))}

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Define ROI (Region of Interest)
    x, y, w, h = 100, 100, 300, 300
    roi = frame[y:y+h, x:x+w]
    
    # Preprocess image
    roi_resized = cv2.resize(roi, (64, 64))
    roi_resized = roi_resized / 255.0
    roi_resized = np.expand_dims(roi_resized, axis=0)

    # Predict sign
    prediction = model.predict(roi_resized)
    pred_index = np.argmax(prediction)
    pred_label = class_indices[pred_index]

    # Draw ROI
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, f"Prediction: {pred_label}", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display frame
    cv2.imshow("Sign Language Translator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()