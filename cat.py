import sys
file_name =  sys.argv[1]
file = open(f"{file_name}","r")
text = file.read()
print(text)
