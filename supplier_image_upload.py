#!/usr/bin/env python3

import requests
import glob

url = "http://localhost/upload/"

path = '~/supplier-data/images/*.jpeg'
files = glob.glob(dir)

for filename in files:
    with open(filename, 'rb') as opened:
        r = requests.post(url, files={'file': opened})