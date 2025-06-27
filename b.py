file = open('codingal.txt','r')
print(file.read())
file.close()

file = open('codingal.txt','r')
print("\n Read in parts\n")
print(file.read(19))
file.close()

file = open('codingal.txt','a')
file.write("Hi I am Pengiun and I am 1yr old.")
file.close()