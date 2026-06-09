from sklearn.model_selection import train_test_split
import numpy as np

# Dummy test
X = np.zeros((326, 240, 240, 4))
Y = np.zeros((326, 240, 240))

X_train, X_val, Y_train, Y_val = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42
)

print("Train:", X_train.shape)
print("Validation:", X_val.shape)