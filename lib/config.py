import json

''' === STRUCTURE OF SPECIFIC CONFIG FILES ===
 1.=== template.config.json ===*
	root {							: Template Root
	<branchID> {					: Built In Branches <Hard Coded>
		templateOrigin: "<dir>"		: The Root Folder Of All Templates		
		<templateID>: {				
			name					: Display Name <Required>
			description				: Description For Template <Required>
			requirement				: List of Requirement For Template
			checkRequirement		: Command Lines Codes to Check Requirement

			batchInstaller			: Directory of A Set Of Command That Will
									be Used to Create A New Project
			wizardPyScript			: Location Of A Python Script That Will
									Allow More Wizard Selection
			NOTE 1: INSTALLATION FILE HAVE TO BE IN:
			"src//<root>.template//<templateName>
			NOTE 2: PYSCRIPT HAVE HIGHER PRIORITIZE THAN BATCH INSTALLER.
			IF PYSCRIPT IS NOT FOUND, IT WILL AUTOMATICALLY SWITCH TO BATCH INSTEAD
		}
	}
	}
'''


# Loading Global Configuration
CONFIG_DIR = ".\\src\\config\\config.json"
readData = open(CONFIG_DIR, "r", encoding="utf-8")
globalConfig = json.load(readData)
readData.close()

# Loading Template Configuration
TEMPLATE_DIR = ".\\src\\config\\template.config.json"
readData = open(TEMPLATE_DIR, "r", encoding="utf-8")
templateConfig = json.load(readData)
readData.close()
