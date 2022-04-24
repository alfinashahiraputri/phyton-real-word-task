#!/usr/bin/env python3

import os
import requests

def generate_message(filename){
    keys = ['name', 'weight', 'description']
    data = {}
    with open(filename, 'r') as f:
        lines = f.readlines().strip()
        lines[2] = int(lines[2].strip(' lbs'))
        data = {k,v for k,v in zip(keys, lines)}
        data['image_name'] = filename.replace('.txt', '.jpeg')
    return data
}

def upload_infos():
    dir = '~/supplier-data/descriptions/'
    # Change the IP
    url = 'http://IP/fruits/'
    filenames = os.listdir(dir)
    for filename in filenames:
        msg = generate_message(os.path.join(dir,filename))
        response = requests.post(url=url, data=msg)
        if response.status_code==201:
            print('Success!')
        else:
            print('ERROR CODE : {}'.format(response.status_code))

if __name__ == "__main__":
    upload_infos()