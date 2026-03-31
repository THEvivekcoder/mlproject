'''setup.py is a Python file used to package your project so it can be installed like a library.
setup.py is used to define project metadata and dependencies, allowing the project to be installed, distributed, and reused as a Python package.'''

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='vivek kumar',
author_email='vivekop8825@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

