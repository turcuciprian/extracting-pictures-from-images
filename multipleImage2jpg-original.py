import os
from PIL import Image

def bmp_tif_to_jpg(source_folder, output_folder):
    """
    Recursively traverses all folders inside `source_folder`, extracts all BMP and TIF images, converts them to JPG images,
    and saves the JPG images to `output_folder` with unique file names starting from 0001.
    """
    i = 1
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.bmp') or file.lower().endswith('.tif') or file.lower().endswith('.tiff'):
                img_path = os.path.join(root, file)
                with Image.open(img_path) as im:
                    output_name = str(i).zfill(4) + '.jpg'
                    output_path = os.path.join(output_folder, output_name)
                    im.convert('RGB').save(output_path, 'JPEG')
                    i += 1
                    
source_folder = './input'
output_folder = './output'

bmp_tif_to_jpg(source_folder, output_folder)