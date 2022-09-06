'''PROJECT MANAGEMENT MODULE '''

# Import Basic Library
from lib.config import *
from lib.functions import *

# External Library
import os
import inquirer

# Get Some Basic Information
projectNamesList = list(projectConf.keys())


def exploreMenu():
    # Behind The Scene
    projectNamesList.append('More...')

    # The Scene
    os.system("cls")
    print('=========== PROJECT EXPLORER ==========')
    projectName = [inquirer.List('getProjectName',
                                 message='Select One Of These Project Below Or Choose "More..." for Additional Tools',
                                 choices=projectNamesList)]
    projectName = inquirer.prompt(projectName)['getProjectName']

    if projectName == "More...":
        os.system("cls")
        print('======= Advance Option Menu =======')
        advanceOpt = [inquirer.List("getAdvOpt",
                                    message='Select One Below',
                                    choices=['Purges Project List: Delete All Projects With Invalid Directory'])]
        advanceOpt = inquirer.Prompt(advanceOpt)['getAdvOpt']

        # ! Add Purge Option Functionality
        if advanceOpt == "urges Project List: Delete All Projects With Invalid Directory":
            print('Final Selection!!!')
    else:
        # Select Your Action After Choose Your Project
        print("=== PROJECT INFORMATION ===")
        optionChoose = []
        optionChoose.append("Open Project In "+ str(globalConfig["friendlyDefaultIDEName"]))
        optionChoose.append("Edit Project Config")
        optionChoose.append("Delete Project")
        selOpt = [inquirer.List(
            "selProjectAct",
            message=f"Select Your Action - \"{projectName}\"",
            choices=optionChoose)]
        selOpt = inquirer.prompt(selOpt)['selProjectAct']
        
        # TODO: Add Functionality
        if selOpt == optionChoose[0]:
            print("Opening in [IDE]")
        elif selOpt == optionChoose[1]:
            print("Editing Config")
        elif selOpt == optionChoose[2]:
            print("Confirmation")

if __name__ == "__main__":
    exploreMenu()
