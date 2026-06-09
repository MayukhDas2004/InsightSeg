from pathlib import Path
import nibabel as nib

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patient = [p for p in dataset_path.iterdir() if p.is_dir()][0]

flair = nib.load(list(patient.glob("*_flair.nii.gz"))[0]).get_fdata()
t1 = nib.load(list(patient.glob("*_t1.nii.gz"))[0]).get_fdata()
t1ce = nib.load(list(patient.glob("*_t1ce.nii.gz"))[0]).get_fdata()
t2 = nib.load(list(patient.glob("*_t2.nii.gz"))[0]).get_fdata()
seg = nib.load(list(patient.glob("*_seg.nii.gz"))[0]).get_fdata()

print("FLAIR:", flair.shape)
print("T1:", t1.shape)
print("T1CE:", t1ce.shape)
print("T2:", t2.shape)
print("SEG:", seg.shape)