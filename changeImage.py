#!/usr/bin/env python3

from PIL import Image
import glob

dir = "~/supplier-data/images"

files = glob.glob(dir+'/*')

for filename in files:
    with Image.open(filename) as img:
        img = img.convert('RGB')
        img = img.resize((600,400))

        # Change format
        out_name = filename.replace('.tiff', '.jpeg')

         # Save image
         img.save(out_name)
         
