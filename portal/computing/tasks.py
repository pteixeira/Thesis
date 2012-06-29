from celery.task import task
from celery.signals import task_sent
from subprocess import call
import subprocess 

@task(name="computing.tasks.add")#portal.computing.tasks.add
def add():
    subprocess.call(['sudo', "/home/pedro/Desktop/scripts/test.sh"]) 
    
    
    return 102893
    
