from re import template
from alive_progress import alive_bar
from lib.config import *
from time import sleep
import os

def checkRequirement(templateHeader,templateVariant):
    template = templateConfig[templateVariant][templateHeader]
    requirementTitle = template['requirement']
    executableRequirement = template['checkRequirement']
    os.system('cls')

    print('Checking For Needed Requirement...')
    print(f'Checking These Following Requirement: {requirementTitle}')
    result = []

    for i in executableRequirement:
        if os.system(i) == 0:
            # Successful Checkup
            result.append(True)
        else:
            result.append(False)
    for i in result:
        if i != True:
        # Failed Requirement Test 
            return False
        # Successful Requirement Test 
    else: return True

# Executing Commands
def progressExecution(templateHeader, templateVariant, templateDir, templateName):
    # Execution of Commands
    for i in range(100):
        # Use If i for certain % for more specific
        if i == 5:
            print('2nd Time | Checking Required Requirement...')


        yield

# Main thread of project generation
def executionMainThread(selectionType,name,dir):
    '''Executing Project Generation from selected Configuration'''
    print('Initializing Project...')
    sleep(2)
    print('Loading Current Template')

    # Generating Loading Bar
    with alive_bar(100) as bar:
        for i in progressExecution(selectionType):
            bar()

    print('Checking for required Requirement...')

# Load the parents' category from template.config.json 
def categorizedTemplate(templateRoot):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    outputReturn = []
    for i in templateKeys:
        outputReturn.append(templateRoot[i]["name"])
    return outputReturn

# Load the requirements needed from modules
def templateLoader(templateRoot,templateName):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    for i in templateKeys:
        if templateRoot[i]["name"] == templateName:
            return i
    else:
        return None