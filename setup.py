import setuptools
import yaml

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("./environment.yml", "r") as requirements_file:
    conda_environment = yaml.load(requirements_file, Loader=yaml.FullLoader)

requirements = list()
for elem in conda_environment['dependencies']:
    if isinstance(elem, str):
        if "python" not in elem:
            requirements.append(elem)
    elif isinstance(elem, dict) and 'pip' in elem:
        requirements.extend(elem['pip'])

setuptools.setup(
    name='Vanilla project',
    version='1.0.0',
    scripts=['main.py'],
    author="François Valadier",
    author_email="francois.valadier@gmail.com",
    description="Vanilla project description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenValue/PythonVanilla.git",
    packages=setuptools.find_packages(),
    install_requires=requirements,  # same libs as environment.yml
    classifiers=[
        "Development Status :: 2 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: TF1 :: All rights reserved"],
)
