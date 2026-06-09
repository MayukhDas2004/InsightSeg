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

# Pick one slice containing tumor
slice_num = 70

image_slice = np.stack([
    flair[:, :, slice_num],
    t1[:, :, slice_num],
    t1ce[:, :, slice_num],
    t2[:, :, slice_num]
], axis=-1)

mask_slice = seg[:, :, slice_num]

print("Image slice shape:", image_slice.shape)
print("Mask slice shape:", mask_slice.shape)
print("Mask labels:", np.unique(mask_slice))