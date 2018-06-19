# Jenkins Job Script

This script seeks to get all the jenkins jobs  from the jenkins instance and store the statuses of the jobs in an SQLite database.

## Getting Started

To have a copy of the project, kindly do the following.
- Clone the repository using this command
```commandline
git clone https://github.com/paradisekelechi/python-script.git
```

### Prerequisites

The following prerequisites are needed for this project.
It is expected that the machine should have python installed and an account on Jenkins.

### Installing

To get the project up and running on your machine, kindly follow these instructions.
- Clone the repository using this command
```commandline
git clone https://github.com/paradisekelechi/python-script.git
```
- Import the project into your preferred editor
- Setup a virtual environment and install jenkinsapi
```commandline
pip install jenkinsapi
```
- Export the environment variables thus:
```commandline
export JENKINS_URL=''
export JENKINS_USERNAME=''
export JENKINS_PASSWORD=''
```
- Setup a database system thus:
```commandline
python3 Migration.py
```
- Execute script thus
```commandline
python3 Loader.py
```

## Authors

* **Kelechi Iheanyichukwu** - *Work done* - [ParadiseKelechi](https://github.com/ParadiseKelechi)
