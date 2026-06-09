import nibabel as nib
import matplotlib.pyplot as plt

flair_path = r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data\BraTS2021_01165\BraTS2021_01165_flair.nii.gz"

seg_path = r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data\BraTS2021_01165\BraTS2021_01165_seg.nii.gz"

flair = nib.load(flair_path).get_fdata()
seg = nib.load(seg_path).get_fdata()

# CHANGE THIS NUMBER
slice_num = 132

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(flair[:, :, slice_num], cmap="gray")
plt.title(f"FLAIR MRI - Slice {slice_num}")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(seg[:, :, slice_num], cmap="gray")
plt.title(f"Mask - Slice {slice_num}")
plt.axis("off")

plt.show()