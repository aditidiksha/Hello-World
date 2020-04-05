import ConfigParser
import webbrowser
configParser = ConfigParser.RawConfigParser()
configParser.read("/home/aditi/check.conf")
num = configParser.get('userinput-config', 'num')
num2 = int(num)
message = "hello world"
f = open('test.txt', 'w')
f.write(message*num2)
f.close()