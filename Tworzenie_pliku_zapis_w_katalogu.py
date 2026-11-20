import os

webaddresses = []

line = input("Enter your address www or if you want finish section, please press 'ENTER':")

while line != "":

    webaddresses.append(line)
    line = input("Enter you second address: ")

    if line == "":
        print("Thank for you address, they will be save!")
        break

print(webaddresses)

dirname = r'C:\Users\kamsob\Desktop\addresses'

filename = input("Enter your file name: ")

filepath = os.path.join(dirname,filename)

file = open(filepath, '+w') 

for webadress in webaddresses:
    file.write(webadress + '\n')
file.close