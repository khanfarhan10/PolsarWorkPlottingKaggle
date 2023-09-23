import sys
import os
from PIL import Image
import cv2

INPUT_PATH = "/home/koireader/work/PolsarWorkPlottingKaggle/docs/Urban Polsar- Enhancement paper3_reduced_images"

import os, fnmatch
def find(pattern, path):
    """Utility to find files wrt a regex search"""
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result



def reduce_img_size(image_path):
    ext = os.path.splitext(os.path.basename(image_path))[1].lstrip(".")
    print(f"image_path = {image_path}")
    pil_image = Image.open(image_path)
    # output_image_path = image_path
    output_image_path = os.path.join(os.path.dirname(image_path), os.path.splitext(os.path.basename(image_path))[0] + ".jpeg")
    # pil_image.save(fp = image_path, format = ext, quality = 75, optimize=True)
    if pil_image.mode in ("RGBA", "P"):
        pil_image = pil_image.convert("RGB")
    (height, width) = pil_image.size
    pil_image = pil_image.resize((height//10, width//10), resample=Image.LANCZOS) 
    os.remove(image_path)
    pil_image.save(fp = output_image_path, format = f'JPEG', quality = 25, optimize=True)



file_path = INPUT_PATH

EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
]

all_files = find('*.*', INPUT_PATH)
# print(f"all_files = {all_files}")

if os.path.isdir(file_path):
    print("\nIt is a directory")
    list(map(reduce_img_size, [ each_filename for each_filename in all_files if any([each_filename.lower().endswith(ext) for ext in EXTENSIONS])]))

elif os.path.isfile(file_path):  
    reduce_img_size(file_path)
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
