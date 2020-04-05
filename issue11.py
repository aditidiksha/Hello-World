try:
    num = int(input("Please enter the number: "))
    for i in range(num):
        print("Hello World")
except Exception as inst:
    print(inst)
