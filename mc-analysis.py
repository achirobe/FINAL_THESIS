import os
import matplotlib.pyplot as plt

# --- Path to the main folder containing subfolders of faulty image types ---
faulty_base_dir = "/Users/reamy/Desktop/THESIS/MC_dataset copy 2"

# --- List all folders representing different fault types ---
fault_types = [folder for folder in os.listdir(faulty_base_dir)
               if os.path.isdir(os.path.join(faulty_base_dir, folder))]

# --- Count images in each fault type folder ---
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
fault_counts = {}

for fault in fault_types:
    folder_path = os.path.join(faulty_base_dir, fault)
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    fault_counts[fault] = len(images)

# --- Plot histogram ---
plt.figure(figsize=(10, 6))
plt.bar(fault_counts.keys(), fault_counts.values(), color='salmon', edgecolor='black')
plt.title("Histogram of Faulty Image Categories", fontsize=16)
plt.xlabel("Fault Type", fontsize=14)
plt.ylabel("Number of Images", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("fault_histogram.png", dpi=300)
plt.show()