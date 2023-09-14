cou_file = open('countries.txt', 'r')
print(cou_file.readable())  #returns boolean value
print(cou_file.readline())  #returns first line
print(cou_file.readline())  #return next line
print(cou_file.readlines()) #returns list of lines

for lines in cou_file.readlines():
  print(lines)
cou_file.close()

#writing in Files

co_file = open('countries.txt', 'w')
co_file.write("This is a new text")
co_file.close
