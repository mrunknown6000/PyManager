"""
    THIS IS NOT THE MAIN EXECUTABLE FILE, PLEASE USE main.py INSTEAD
    ========== CREATE PROJECT WIZARD ==========
"""
# External Library
import os
from lib.config import *
from lib.functions import *

# UI Library
import inquirer

# Acquire Directory Lists

def projectWizardSetup():
    dirList = list(globalConfig["specificTypeDir"].values())
    dirList.append("Custom Specific Directory...")

    ''' ============= MAIN RUNNING THREAD ============== '''
    # Introduction Guide
    print('PROJECT GENERATOR CLI v0.1')

    # Selection
    projectType = [inquirer.List("projectType",
                                 message="Choose your project\'s type for specific template",
                                 choices=["Web Development", "CLI Application", "GUI Application"])]
    projectType = inquirer.prompt(projectType)['projectType']
    projectVariant = ''
    # Project Switch
    if projectType == 'Web Development':
        projectVariant = "web-dev"
    elif projectType == 'CLI Application':
        projectVariant = 'cli-app'
    elif projectType == 'GUI Application':
        projectVariant = 'gui-app'

    # Web Development Different Templates
    projectLang = [inquirer.List("projectLang",
                                 message="Choose a template for your project",
                                 choices=categorizedTemplate(templateConfig[projectVariant]))]
    projectLang = inquirer.prompt(
        projectLang)['projectLang']  # Returned as String

    # Checking Needed Requirement For The Installation
    if checkRequirement(templateLoader(templateConfig[projectVariant], projectLang), projectVariant) == False:
        exit('ERROR: A Needed Requirement For This Template is Missing')

    # Acquirer Project Name
    projectName = input('Please type your project\'s name: ')
    # Project Directory
    projectDir = [inquirer.List("projectDir",
                                message="Choose a directory for your project. NOTE: This will be a sub-directory for defaultRepoDir",
                                choices=dirList)]
    projectDir = inquirer.prompt(
        projectDir)['projectDir']  # Returned as String

    # TODO: Add the defaultRepo into the start of directory
    projectDir = globalConfig["defaultRepoDir"] + projectDir
    ''' 
    TODO: Add Git Repository Integration
    TODO: Add VScode Integration
    '''
    '''Final Confirmation'''
    print('==== FINAL SUMMARY ====')
    print(f'Project Name: {projectName}')
    print(f'Project Type: {projectType}')
    print(f'Project Template: {projectLang}')
    print(f'Directory for your Project: {projectDir}')
    print('=======================')

    finalConfirm = [inquirer.Confirm("confirmation",
                    message="Do you want to continue?",
                    default="True")]
    # Confirmed
    if inquirer.prompt(finalConfirm)['confirmation']:
        # Parameter: ProjectName, Directory and Installer
        # TODO: Add PyScript Support
        executionMainThread(projectName, projectDir, 
        templateConfig[projectVariant][templateLoader(templateConfig[projectVariant], projectLang)]["batchInstaller"],
        templateConfig[projectVariant][templateLoader(templateConfig[projectVariant], projectLang)]["wizardPyScript"])
    else:
        # Exit out of the program
        print('Setup is now Canceled...')
        pause(2)
        exit()


# DEBUGGING SPECIFIC FEATURE MODE
if __name__ == '__main__':
    print('''WARNING: This file is running as a standalone file instead of library. \n
            Use this if you wish to debug the projectWizard.py''')
    debuggerConfirmation = [inquirer.Confirm('debugMode',
                            message="Do you want to continue in debug mode?",
                            default="False")]
    if inquirer.prompt(debuggerConfirmation):
        isDebug()
        os.system('cls')
        projectWizardSetup()
    else:
        exit()
