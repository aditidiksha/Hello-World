import ConfigParser
configParser = ConfigParser.RawConfigParser()
configFilePath = "/home/aditi/github_repositories/config/check.conf"
configParser.read(configFilePath)
num = configParser.get('userinput-config', 'num')
for i in range(int(num)):
    print("hello world")
	