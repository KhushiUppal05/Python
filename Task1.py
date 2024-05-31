#Python program to create a list
my_list = [1,2,3,4,5]
print('Original List:' , my_list)
#Adding an element to the list
my_list.append(6)
print('Updated List:' , my_list)
#Removing an element from the list
my_list.remove(3)
print('Updated List:' , my_list)
#Modifying an element in the list
my_list[1]=8
print('Updated List:' , my_list)

#Python program to create a dictionary
my_dict={'Name':'Khushi','Age':18,'City':'Delhi'}
print('Original Dictionary:' , my_dict)
#Adding
my_dict['gender'] = 'Female'
print('Updated Dictionary:' , my_dict)
#Removing
del my_dict['City']
print('Updated Dictionary:' , my_dict)
#Modifying
my_dict['Age'] = 19
print('Updated Dictionary:' , my_dict)

#Python program to create a set
my_set ={5,6,7,8,9}
print('Original Set:' , my_set)
#Adding
my_set.add(10)
print('Updated Set:' , my_set)
#Removing
my_set.remove(9)
print('Updated Set:' , my_set)
#Modifying
my_set.discard(7)
my_set.add(11)
print('Updated Set:' , my_set)