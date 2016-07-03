import os 
from fabric.api import run, lcd, task, hosts, local, serial

PYTHON_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_TAG = 'python_3.5.2'

@task
@hosts('localhost')
def build(version):
    image_name = 'localhost:5000/%s:%s' %(IMAGE_TAG, version)

    with lcd(PYTHON_ROOT):
        local('docker build -t %s .' %image_name)
        local('docker push %s' %image_name)

@task
@serial
def install(version):
    run('docker run -ti localhost:5000/%s:%s' %(IMAGE_TAG, version))
