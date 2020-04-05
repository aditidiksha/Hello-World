import webbrowser
message = """<<html><head>
</head><body><p>Hello world</p></body>
</html>"""
f = open('helloworld.html', 'w')
f.write(message)
f.close()
webbrowser.open("C://Users/aditi/Documents/Python Scripts/helloworld.html")
