two_d_list = [
  [1, 2, 4],
  [12, 43, 134],
  [3432, 121, 94]
]

print(two_d_list)
print(two_d_list[0][1])

#print the rows
for lists in two_d_list:
  print(lists)

#prints each elements of 2 d list
for i in two_d_list:
  for j in i:
    print(j)