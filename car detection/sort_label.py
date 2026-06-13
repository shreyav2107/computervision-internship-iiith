import os
import shutil

train_images = set(os.path.splitext(f)[0] for f in os.listdir("dataset/images/train"))
val_images = set(os.path.splitext(f)[0] for f in os.listdir("dataset/images/val"))

exported_labels = "temp/labels"

for label in os.listdir(exported_labels):
    if not label.endswith(".txt"):
        continue

    name = os.path.splitext(label)[0]
    src = os.path.join(exported_labels, label)

    if name in train_images:
        shutil.copy(src, "dataset/labels/train")

    elif name in val_images:
        shutil.copy(src, "dataset/labels/val")

print("Done!")