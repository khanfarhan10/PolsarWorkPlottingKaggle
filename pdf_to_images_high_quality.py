from pdf2image import convert_from_path
# pages = convert_from_path('/home/koireader/work/digitize-orders/tests/aa/0L9NBPQZ3F9UCB.pdf', dpi = 600)
# # Saving pages in jpeg format

# for i, page in enumerate(pages):
#     page.save(f'out_{i}.jpg', 'JPEG')


#The pdf2image library can be used
#You can install it simply using,

# pip install pdf2image
#Once installed you can use following code to get images.

# Install poppler and add it to path variable
# https://blog.alivate.com.au/poppler-windows/

import sys
import os
# import src.utils.settings

# poppler_path = os.getenv('POPPLER_PATH')
# if poppler_path and os.path.exists(poppler_path):
#     poppler_path = os.path.realpath(poppler_path)
#     print(f"poppler_path: {poppler_path}")
#     sys.path.insert(0, poppler_path)
# else:
#     print(f"POPPLER not found! Please install it and add it to path variable, poppler_path: {poppler_path}")
    
from pdf2image import convert_from_path

def convert_image_to_png(image_path, file_format = "PNG"):
    pages = convert_from_path(image_path, dpi = 600)
    # pages = convert_from_path(image_path)

    # Saving pages in jpeg format

    for page_num, page_pil_image in enumerate(pages):
        base_image_name = os.path.splitext(image_path)[0]
        page_pil_image.save(fp = f'{base_image_name}_{str(page_num+1).zfill(3)}.{file_format.lower()}', format = f'{file_format}', quality = 100, optimize=True)
        # optimize = True, quality = 85

file_path = sys.argv[1]

if os.path.isdir(file_path):  
    print("\nIt is a directory")  
    list(map(convert_image_to_png, [os.path.join(file_path, each_filename) for each_filename in os.listdir(file_path) if each_filename.endswith(".pdf") or each_filename.endswith(".PDF")]))
elif os.path.isfile(file_path):  
    convert_image_to_png(file_path)
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
