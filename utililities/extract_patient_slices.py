from pathlib import Path
import nibabel as nib
import numpy as np

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

# Load modalities
flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()
t1 = nib.load(list(patient.glob("*_t1.nii.gz"))[0]).get_fdata()
t1ce = nib.load(list(patient.glob("*_t1ce.nii.gz"))[0]).get_fdata()
t2 = nib.load(list(patient.glob("*_t2.nii.gz"))[0]).get_fdata()

# Load mask
seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

# Normalize
def normalize(img):
    return (img - np.mean(img)) / np.std(img)

flair = normalize(flair)
t1 = normalize(t1)
t1ce = normalize(t1ce)
t2 = normalize(t2)

X = []
Y = []

for i in range(seg.shape[2]):

    # Keep only slices containing tumor
    if np.any(seg[:, :, i] > 0):

        image_slice = np.stack([
            flair[:, :, i],
            t1[:, :, i],
            t1ce[:, :, i],
            t2[:, :, i]
        ], axis=-1)

        mask_slice = seg[:, :, i]

        X.append(image_slice)
        Y.append(mask_slice)

X = np.array(X)
Y = np.array(Y)

print("X shape:", X.shape)
print("Y shape:", Y.shape)