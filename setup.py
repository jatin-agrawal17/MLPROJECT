
# Importing necessary functions and types
from setuptools import find_packages, setup  # Used to package and install Python projects
from typing import List  # Used to specify the return type of a function

# Defining a constant for checking '-e .' in requirements.txt
HYPEN_E_DOT = '-e .'

# Function to read and return the list of requirements from requirements.txt
# -> is return type
def get_requirements(file_path: str) -> List[str]:  
    '''
    This function will return a list of packages mentioned in the requirements file
    '''
    requirements = []  # Empty list to store each requirement
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines from the file
        # for readlines it use \n so  in next line we have to replace new line to blank
        requirements = [req.replace("\n", "") for req in requirements]  # Remove newline characters

        # Remove '-e .' if it's in the list (it's only needed during development, not installation)
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements  # Return the cleaned list of requirements


# Calling the setup function to define the package details
setup(
    name='ML Project',  # Name of your project
    version='0.0.1',  # Version of your project (can be changed as you update)
    author='jatin',  # Your name as the author
    author_email='agrawaljatin405@gmail.com',  # Your contact email
    packages=find_packages(),  # Automatically find all packages (folders with __init__.py)
    install_requires=get_requirements('requirements.txt')  # Install dependencies listed in requirements.txt
)
