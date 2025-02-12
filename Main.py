import os
import shutil
from pdf2image import convert_from_path

# Specify the path to the Poppler 'bin' folder
poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"  # Adjust this path for your system

# Specify the folder containing PDF files and images
input_folder = r'C:\Users\inc3061\Passports'

# Specify the output folder for saving images
output_folder = r'C:\Users\inc3061\Passports\image_passport'

# Ensure output folder exists, create it if it doesn't
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define supported image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    # Full path to the file
    file_path = os.path.join(input_folder, filename)

    if filename.lower().endswith(".pdf"):
        # Convert the PDF to images
        pages = convert_from_path(file_path, dpi=300, poppler_path=poppler_path)

        # Save each page as an image in the output folder
        for i, page in enumerate(pages):
            output_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_page_{i+1}.jpg")
            page.save(output_image_path, 'JPEG')

        print(f"Processed PDF: {filename}")

    elif filename.lower().endswith(image_extensions):
        # If it's an image file, move it directly to the output folder
        output_image_path = os.path.join(output_folder, filename)
        shutil.copy(file_path, output_image_path)

        print(f"Copied image: {filename}")

print("All PDFs and image files have been processed.")
