import lib.functions as tester
import lib.config as tester_config


testConfig = {
	"inName": "test",
	"inDir": "%UserProfile%\\.src-code\\Web Developments",
	"insDir": tester_config["web-dev"]["vanillaHTML"]["batchInstaller"]
}

"""
- NOTE FOR ALL ACRONYMS:
	+ in  = INPUT
	+ ins = INSTALLER
	+ dir = DIRECTORY
- TODO: well, this suck ._.
"""

def testExecuteThread():
	print('EXECUTION TEST')

	# @param: Parameter is inName inDir insDir
	tester.executionMainThread(testConfig["inName"],testConfig["inDir"],testConfig["insDir"])