''' CORE COMPONENT OF THE PROJECT - RUN THIS APP INSTEAD :)'''
# Modules Libraries
import projectWizard
import projectExplorer

import inquirer

# TODO: Add First Time User Experience
# TODO: Add A Setting

# Core Main Menu
def mainMenu():
	# Action Selecting
	actionMenu = [inquirer.List("selectionOpt",
	message="Choose These Following Actions: ",
	choices=['Open A Project','Create A New Project','Recently Opens','Quick Text','Setting','Exit'])]
	actionMenu = inquirer.prompt(actionMenu)['selectionOpt']

	if actionMenu == 'Open A Project':
		# Opening Project Wizard
		print('Opening Project Menu')

	elif actionMenu == 'Create A New Project':
		# Starting New Project Wizard
		print('Creating A New Project')
		projectWizard.projectWizardSetup()

	elif actionMenu == 'Recently Opens':
		print('Recently Opens')
	elif actionMenu == 'Setting':
		print('Opening Setting')
	elif actionMenu == 'Quick Text':
		print('Quick Text')
	elif actionMenu == 'Exit':
		exit(0)




if __name__ == "__main__":
	print('PROJECT MANAGER v0.2 by MrUnknown6000')
	mainMenu()