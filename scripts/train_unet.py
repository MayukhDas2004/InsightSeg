import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

X = np.load("X.npy").astype(np.float32)
Y = np.load("Y.npy").astype(np.int32)

print(X.shape)
print(Y.shape)

X_train, X_val, Y_train, Y_val = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

inputs = tf.keras.layers.Input(shape=(240, 240, 4))

c1 = tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same")(inputs)
c1 = tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same")(c1)
p1 = tf.keras.layers.MaxPooling2D()(c1)

c2 = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(p1)
c2 = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(c2)
p2 = tf.keras.layers.MaxPooling2D()(c2)

b = tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same")(p2)
b = tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same")(b)

u1 = tf.keras.layers.UpSampling2D()(b)
u1 = tf.keras.layers.Concatenate()([u1, c2])

c3 = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(u1)
c3 = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(c3)

u2 = tf.keras.layers.UpSampling2D()(c3)
u2 = tf.keras.layers.Concatenate()([u2, c1])

c4 = tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same")(u2)
c4 = tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same")(c4)

outputs = tf.keras.layers.Conv2D(4, 1, activation="softmax")(c4)

model = tf.keras.Model(inputs, outputs)

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    X_train,
    Y_train,
    validation_data=(X_val, Y_val),
    epochs=1,
    batch_size=2
)

import pandas as pd

pd.DataFrame(history.history).to_csv(
    "training_history.csv",
    index=False
)

print("Training history saved")

model.save("unet_model.keras")

print("Model saved")