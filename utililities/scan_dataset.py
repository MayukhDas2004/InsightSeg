from pathlib import Path

dataset_path = Path(r"C:\Users\megha\Downloads\BraTS\BraTS2021_Training_Data")

patients = [p for p in dataset_path.iterdir() if p.is_dir()]

print("Number of patients:", len(patients))

print("\nFirst 5 patients:")
for p in patients[:5]:
    print(p.name)