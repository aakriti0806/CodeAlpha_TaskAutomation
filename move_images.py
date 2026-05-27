import os
import shutil

# ---- SETTINGS ----
source_folder = "C:/Users/HP/Desktop/PROJECT/CodeAlpha_TaskAutomation/Download"        # folder where .jpg files are
destination_folder = "C:/Users/HP/Desktop/PROJECT/CodeAlpha_TaskAutomation/images"      # new folder to move them into
# ------------------

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Count how many files moved
count = 0

# Loop through all files in source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        shutil.move(source_path, destination_path)
        print(f"✅ Moved: {filename}")
        count += 1

if count == 0:
    print("❌ No .jpg files found in the folder!")
else:
    print(f"\n🎉 Done! {count} file(s) moved to '{destination_folder}' folder.")