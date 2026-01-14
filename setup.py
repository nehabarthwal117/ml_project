from setuptools import setup, find_packages
from typing import List

#  we dont want -e .
x = "-e ."
def get_requirements(filepath:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements =[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if x in requirements:
            requirements.remove(x)



setup(
    name="ml project",
    version="0.0.1",
    author="Neha Barthwal",
    author_email="nbarthwal@constructor.university",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)