countries = ['United Kingdom', 'India', 'Nigera', 'Australia', 'France']

print(countries)
print(countries[1])

#print range
print(countries[1:]) #from index 1 to end
print(countries[1:4]) #from index 1 to 4 , it exclued index 4

#acces element and change value

countries[0] = 'United States'
countries[2] = 'New Zealand'

print(countries)

#access element from last 
print(countries[-2])  #last 2nd

#length of list
print(len(countries))

#we can add different datatypes in list