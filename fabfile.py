import os 
from fabric.api import run, lcd, task, hosts, local, serial

SCALA_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGE_TAG = 'scala'

@task
@host('localhost')
def build(version):
    image_name = 'localhost:5000/%s:%s' %(IMAGE_TAG, version)

    with lcd(SCALA_ROOT):
        local('docker build -t %s .' %image_name)
        local('docker push %s' %image_name)

@task
@serial
def install(version):
    run ('docker run -ti localhost:5000/%s:%s') %(IMAGE_TAG, version)

