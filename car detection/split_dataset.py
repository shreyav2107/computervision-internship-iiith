import os
import shutil

source = "frames"

os.makedirs("dataset/images/train", exist_ok=True)
os.makedirs("dataset/images/val", exist_ok=True)
os.makedirs("dataset/images/test", exist_ok=True)

files = sorted([f for f in os.listdir(source) if f.endswith(".jpg")])

for i, file in enumerate(files):
    src = os.path.join(source, file)

    if i % 3 == 0 and len(os.listdir("dataset/images/train")) < 100:
        shutil.copy(src, "dataset/images/train")
    elif len(os.listdir("dataset/images/val")) < 40:
        shutil.copy(src, "dataset/images/val")
    else:
        shutil.copy(src, "dataset/images/test")

print("Done!")