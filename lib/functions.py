from asyncio.windows_events import NULL
from re import template
from alive_progress import alive_bar
from lib.config import *
from time import sleep
import os

# External Tools for easier Code
isDebugging = False

def availChecker(script):
    if script != None:
        return True
    else: return False


def isDebug():
    global isDebugging
    isDebugging = True


def pause(sec=3):
    global isDebugging
    if isDebugging == False:
        sleep(3)
    else:
        print('INFO || DEBUG MODE - PAUSE IGNORED')


def checkRequirement(templateHeader, templateVariant):
    template = templateConfig[templateVariant][templateHeader]
    requirementTitle = template['requirement']
    executableRequirement = template['checkRequirement']
    os.system('cls')

    print('Checking For Needed Requirement...')
    pause(2)
    print(f'Checking These Following Requirement: {requirementTitle}')
    result = []
    pause(2)

    for i in executableRequirement:
        if os.system(i) == 0:
            # Successful Checkup
            result.append(True)
        else:
            result.append(False)
    for i in result:
        if i == True:
            # Failed Requirement Test
            os.system("cls")
            print('''YAY, Your System Met The Requirement For This Template. 
            \n You will be redirected to the next section in 3 seconds...''')
            pause(3)
            return True
        # Successful Requirement Test
    else:
        return False

# Executing Commands


def progressExecution(templateName, templateDir, templateInstaller, pyScript):
    # Loading Batch Script
    batchInstallerStatus = availChecker(templateInstaller)
    pyScriptStatus = availChecker(pyScript)


    executionOrder = f"cd \"{templateInstaller}\" && installer.bat \"{templateDir}\" \"{templateName}\""

    # Execution of Commands
    for i in range(100):
        # Use If i for certain % for more specific
        if i == 5:                                  # ========== INITIALIZING PREP =========
            print('Preparing Installation...')

            # CHECKING FOR AVAILABILITY
            print(f"Batch Installer Status: {batchInstallerStatus}")
            print(f"PyScript Installer Status: {pyScriptStatus}")    

        if i == 10:
            print('Installation Is Now Ready!')
            pause(1)
            if not pyScriptStatus:  
                print('PyScript Not Available | Initializing Batch Installer...')
                if os.system(executionOrder) == 1:
                    print('ERROR: An Error Occurred While Using Batch Installer, Please Fix Installer File For Your Specific Configuration')
                    break
            else:
                exec(open(pyScript).read())
        if i == 80:
            print('Installation Is Completed! YAY')
        yield

# Main thread of project generation


def executionMainThread(name, prgdir, installer, pyScript):
    '''Executing Project Generation from selected Configuration'''
    print('Initializing Project...')
    pause(2)
    print('Loading Current Template')

    # Generating Loading Bar
    with alive_bar(100) as bar:
        for i in progressExecution(name, prgdir, installer, pyScript):
            bar()

# Load the parents' category from template.config.json


def categorizedTemplate(templateRoot):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    outputReturn = []
    for i in templateKeys:
        outputReturn.append(templateRoot[i]["name"])
    return outputReturn

# Load the requirements needed from modules


def templateLoader(templateRoot, templateName):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    for i in templateKeys:
        if templateRoot[i]["name"] == templateName:
            return i
    else:
        return None


