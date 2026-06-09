import tensorflow as tf
from tensorflow.keras import layers, Model

inputs = layers.Input(shape=(240, 240, 4))

# Encoder
c1 = layers.Conv2D(16, 3, activation='relu', padding='same')(inputs)
c1 = layers.Conv2D(16, 3, activation='relu', padding='same')(c1)
p1 = layers.MaxPooling2D()(c1)

c2 = layers.Conv2D(32, 3, activation='relu', padding='same')(p1)
c2 = layers.Conv2D(32, 3, activation='relu', padding='same')(c2)
p2 = layers.MaxPooling2D()(c2)

# Bottleneck
b = layers.Conv2D(64, 3, activation='relu', padding='same')(p2)
b = layers.Conv2D(64, 3, activation='relu', padding='same')(b)

# Decoder
u1 = layers.UpSampling2D()(b)
u1 = layers.Concatenate()([u1, c2])

c3 = layers.Conv2D(32, 3, activation='relu', padding='same')(u1)
c3 = layers.Conv2D(32, 3, activation='relu', padding='same')(c3)

u2 = layers.UpSampling2D()(c3)
u2 = layers.Concatenate()([u2, c1])

c4 = layers.Conv2D(16, 3, activation='relu', padding='same')(u2)
c4 = layers.Conv2D(16, 3, activation='relu', padding='same')(c4)

outputs = outputs = layers.Conv2D(4, 1, activation='softmax')(c4)

model = Model(inputs, outputs)

model.summary()