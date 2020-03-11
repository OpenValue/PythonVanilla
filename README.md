# Python Vanilla project
## Purpose
Provide a Python template project (also with docker config)

## Anaconda local environment support
Install Anaconda:

See https://www.anaconda.com/distribution/#download-section

Edit `environment.yml` file and specify needed libraries

Install Anaconda local environment as below:
```bash
./install-conda-environment.sh
```
Activate Anaconda local environment as below:
```bash
conda activate ${PWD}/.conda
```

## Parameters
- **Configuration files**: yaml files are provided
    - development.yml
    - staging.yml
    - production.yml

The configuration file that will be used is based on ENVIRONMENT variable:
- **ENVIRONMENT**: environment of run
    - development
    - staging
    - production
    - *Default*: development
    
## Format code before committing
```bash
./format.sh
```

## Run tests
We use pytest to run tests. Pytest expects our tests to be located in files whose 
names begin with `test_` or end with `_test.py`

To run tests, go to project root and run:
```bash
pytest
```

## Run code
Set environment variables to relevant values and run:
```bash
./entrypoint.sh
```

## Docker
Build image:
```bash
docker build . -t vanilla
```
Run:
```bash
docker run -it vanilla
```

## Install lib
Activate conda environment and run:
```bash
python setup.py install
```