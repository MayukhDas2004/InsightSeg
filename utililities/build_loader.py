from pathlib import Path

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patients = [p for p in dataset_path.iterdir() if p.is_dir()]

patient = patients[0]

flair = list(patient.glob("*_flair.nii.gz"))[0]
t1 = list(patient.glob("*_t1.nii.gz"))[0]
t1ce = list(patient.glob("*_t1ce.nii.gz"))[0]
t2 = list(patient.glob("*_t2.nii.gz"))[0]
seg = list(patient.glob("*_seg.nii.gz"))[0]

print("Patient:", patient.name)
print("FLAIR:", flair.name)
print("T1:", t1.name)
print("T1CE:", t1ce.name)
print("T2:", t2.name)
print("SEG:", seg.name)