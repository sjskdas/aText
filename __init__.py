import os.path
import sys

def joke():
    return (u'This is a joke!')

def start_atext():
	python_dir, python_exe = os.path.split(sys.executable)
	jar_dir = python_dir + '/Lib/site-packages/aText/jar/PythonServer0.1.jar'
	import subprocess
	p = subprocess.call(['start', '/b', 'javaw', '-jar', jar_dir, 'Server.PythonServer'], shell=True)

def stop_atext():
	os.system('taskkill /f /im javaw.exe')