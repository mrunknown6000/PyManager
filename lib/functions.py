from asyncio.windows_events import NULL
from asyncore import write
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


# Reading Requirements
def checkRequirement(templateHeader, templateVariant):
    template = templateConfig[templateVariant][templateHeader]
    requirementTitle = template['requirement']
    executableRequirement = template['checkRequirement']
    os.system('cls')

    print('Checking For Needed Requirement...')
    pause(1)
    print(f'Checking These Following Requirement: {requirementTitle}')
    result = []

    for i in executableRequirement:
        i += " > NUL"
        if os.system(i) == 0:
            # Successful Checkup
            result.append(True)
        else:
            result.append(False)
    for i in result:
        if i == True:
            # Failed Requirement Test
            print('''YAY, Your System Met The Requirement For This Template. ''')
            return True
        # Successful Requirement Test
    else:
        return False

# The Main Progress Bar with Executions
def progressExecution(templateName, templateDir, templateInstaller, pyScript, projectType):
    # Preparing For Installation
    batchInstallerStatus = availChecker(templateInstaller)
    pyScriptStatus = availChecker(pyScript)

    # Batch Command Line
    # param
    executionOrder = f"cd \"{templateInstaller}\" && installer.bat \"{templateDir}\" \"{templateName}\""

    # Execution of Commands
    for i in range(100):
        # Use If i for certain % for more specific
        if i == 5:              # ========== INITIALIZING PREP =========
            print('Preparing Installation...')

            # CHECKING FOR AVAILABILITY
            print(f"Batch Installer Status: {batchInstallerStatus}")
            print(f"PyScript Installer Status: {pyScriptStatus}")    
        if i == 10:             # ========= GENERATING PROJECT =========        
            print('Installation Is Now Ready!')
            pause(1)
            if not pyScriptStatus:
                print('PyScript Not Available | Initializing Batch Installer...')
                if os.system(executionOrder) == 1:
                    print('ERROR: An Error Occurred While Using Batch Installer, Please Fix Installer File For Your Specific Configuration')
                    break
            else:
                # ! TEST THE PYSCRIPT INSTALLER
                exec(open(pyScript).read())
        if i == 60:             # ========= ADDING TO JSON FILE ========
            print('Listing Project Into A Compatible Save File...')
            projectConf[templateName] = {"directory": templateDir+templateName, "projectType": projectType}
            writeProjectData(projectConf)
        if i == 80:
            print('Finalizing Installation...')
        yield

# User Interface Installation Progress
def executionMainThread(name, prgdir, installer, pyScript, projectType):
    '''Executing Project Generation from selected Configuration'''
    print('Initializing Project...')
    pause(2)
    print('Loading Current Template')

    # Generating Loading Bar
    with alive_bar(100) as bar:
        for i in progressExecution(name, prgdir, installer, pyScript, projectType):
            bar()



# Template File Filter
def categorizedTemplate(templateRoot):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    outputReturn = []
    for i in templateKeys:
        outputReturn.append(templateRoot[i]["name"])
    return outputReturn
def templateLoader(templateRoot, templateName):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    for i in templateKeys:
        if templateRoot[i]["name"] == templateName:
            return i
    else:
        return None


