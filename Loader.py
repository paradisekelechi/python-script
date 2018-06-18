from jenkinsapi.jenkins import Jenkins
import os
from Database import *

jenkins_url = os.environ.get('JENKINS_URL', None)
jenkins_username = os.environ.get('JENKINS_USERNAME', None)
jenkins_password = os.environ.get('JENKINS_PASSWORD', None)


def get_server_instance():
    server = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)
    return server


def get_all_jobs():
    jobs = get_server_instance().get_jobs()
    return jobs


def get_job_data(job):
    job_name = job[0]
    job_instance = get_server_instance().get_job(job_name)
    job_status = job_instance.get_last_build().get_status()
    return [job_name, job_status]


def execute_check():
    jobs = get_all_jobs()
    for job in jobs:
        job_data = get_job_data(job)
        add_job_status(job_data)


execute_check()