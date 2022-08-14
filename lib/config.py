import json

# Loading Global Configuration
CONFIG_DIR = ".\\src\\global.config.json"
readData = open(CONFIG_DIR, "r", encoding="utf-8")
globalConfig = json.load(readData)
readData.close()

# Loading Template Configuration
TEMPLATE_DIR = ".\\src\\template.config.json"
readData = open(TEMPLATE_DIR, "r", encoding="utf-8")
templateConfig = json.load(readData)
readData.close()
