from alive_progress import alive_bar
from lib.config import *

def progressExecution(executionOrder):
    # Execution of Commands
    for i in range(100):
        # Use If i for certain % for more specific


        yield

def executionMainThread(selectionType):
    '''Executing Project Generation from selected Configuration'''
    print('Creating your Project...')
    
    # Generating Loading Bar
    with alive_bar(100) as bar:
        for i in progressExecution(selectionType):
            bar()

    print('Checking for required Requirement...')

def categorizedTemplate(templateRoot):
    templateKeys = list(templateRoot.keys())
    del templateKeys[0]
    outputReturn = []
    for i in templateKeys:
        outputReturn.append(templateRoot[i]["name"])
    return outputReturn