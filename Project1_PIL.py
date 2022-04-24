#!/usr/bin/env python3

import glob
from PIL import Image
import os

src_dir = "/home/student-01-3a2e6672a372/images/"
files = glob.glob(src_dir+'*')

dst_dir = "/opt/icons/"

def edit_and_save(src):
        dst = src.replace(src_dir, dst_dir) + '.jpeg'
        with Image.open(src) as img:
                img = img.convert('RGB')
                img = img.rotate(270)
                img = img.resize((128,128))
                img.save(dst, 'JPEG')
for file in files:
        edit_and_save(file)
