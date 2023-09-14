list1 = [1, 2, 3, 4, 5]
list2 = ['ab', 'ac', 'ad', 'ae']

list1.extend(list2) #adds list 2 to list 1
print(list1)

list2.append('az') #adds a value to list
print(list2)

list2.insert(1, 'cher') #adds a value to a index
print(list2)

list2.clear() #deletes the complete list
print(list2)

print(list1.index('ac')) #returns index of a value

print(list1.count('ac'))  #returns number of times value is repeated

list3 = [3, 9, 1, 12, 4]
list3.sort()    #sorts in ascending
print(list3)

list3.reverse()
print(list3) #reverse the list

list3.remove(9) #deleted the value
print(list3)