from pathlib import Path

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patients = [p for p in dataset_path.iterdir() if p.is_dir()]

patient = patients[0]

print("Patient:", patient.name)

for file in patient.iterdir():
    print(file.name)