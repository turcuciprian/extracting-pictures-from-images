import os
from PIL import Image

def bmp_tif_to_jpg(source_folder, output_folder):
    """
    Recursively traverses all folders inside `source_folder`, extracts all BMP and TIF images, converts them to JPG images,
    and saves the JPG images to `output_folder` with unique file names reflecting the directory structure they are in.
    """
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.bmp') or file.lower().endswith('.tif') or file.lower().endswith('.tiff'):
                img_path = os.path.join(root, file)
                with Image.open(img_path) as im:
                    # Convert image to black and white and then back to RGB
                    bw = im.convert('L')
                    im = bw.convert('RGB')

                    # Construct the output name based on the directory structure
                    relative_path = os.path.relpath(root, source_folder)
                    base_name = os.path.splitext(file)[0]  # Get the filename without the extension
                    relative_path_name = relative_path.replace(os.sep, '_')
                    output_name = f"{relative_path_name}_{base_name}.jpg"
                    output_path = os.path.join(output_folder, output_name)

                    # Ensure output directory exists
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)

                    im.save(output_path, 'JPEG')

source_folder = './input'
output_folder = './output'

bmp_tif_to_jpg(source_folder, output_folder)
