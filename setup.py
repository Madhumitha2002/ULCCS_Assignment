from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)-> List[str]:
    #function returns list of requirements
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n','') for r in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements

setup(
    name = 'ULCCS_Assignment',
    version = '0.0.1',
    author = 'Madhumitha',
    author_email = 'ME20BTECH11022@iith.ac.in',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')
)