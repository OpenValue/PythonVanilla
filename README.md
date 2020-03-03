# PROJECT NAME

## Purpose
Provide a Python template project (also with docker config)

## Anaconda local environment support
Install Anaconda:

See https://www.anaconda.com/distribution/#download-section

Edit `environment.yml` file 

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
## Run
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