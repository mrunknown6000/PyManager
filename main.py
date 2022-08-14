""" ========= Library For The Application ========== """
# External Library
from lib.config import *
from lib.functions import *

# UI Management
import inquirer


# ============= MAIN RUNNING THREAD ==============
# Introduction Guide
print('PROJECT GENERATOR CLI v0.1')

# Selection
projectType = [inquirer.List("projectType",
                             message="Choose your project\'s type for specific template :)",
                             choices=["Web Development", "CLI Application", "GUI Application"])]
projectType = inquirer.prompt(projectType)['projectType']

# Project Switch
if projectType == 'Web Development':
    projectLang = [inquirer.List("projectLang",
                            message="Choose a template for your project :D",
                            choices=categorizedTemplate(templateConfig["web-dev"]))]
    projectLang = inquirer.prompt(projectLang)['projectLang']
elif projectType == 'CLI Application':
    print('CLI')
elif projectType == 'GUI Application':
    print('GUI')



