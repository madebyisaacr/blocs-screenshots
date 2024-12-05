import os
from PIL import Image
import csv
from pathlib import Path


def get_aspect_ratio(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width / height


def process_images(folder_path):
    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".png")]

    # Prepare data for CSV
    data = []
    for file_name in png_files:
        print(f"Processing: {file_name}")
        full_path = os.path.join(folder_path, file_name)
        aspect_ratio = get_aspect_ratio(full_path)
        data.append([file_name, aspect_ratio])

    # Write data to CSV file
    csv_path = os.path.join(folder_path, "aspect_ratios.csv")
    with open(csv_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["fileName", "aspectRatio"])  # Write header
        csv_writer.writerows(data)

    print(f"CSV file has been saved to: {csv_path}")


# Get the folder path from user input
folder_path = "."

# Validate folder path
if not os.path.isdir(folder_path):
    print("Invalid folder path. Please provide a valid directory.")
else:
    process_images(folder_path)
