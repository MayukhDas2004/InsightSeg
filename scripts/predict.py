import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("unet_model.keras")

X = np.load("X.npy").astype(np.float32)

prediction = model.predict(X[:1])

print("Prediction shape:", prediction.shape)
print("Prediction min:", prediction.min())
print("Prediction max:", prediction.max())