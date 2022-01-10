#Dictionaries are defined with curly brackets

my_dictionary={}
print(my_dictionary,type(my_dictionary))

#THis is an example my_dictionary

my_dictionary={'myFruit':'Banana','mySecondFruit':'Apple'}
print(my_dictionary['myFruit'])

#To check if a given dictionary has a particular key in it, use this methods

print(my_dictionary.get('dupa'))

#To add a new item into the dictionary, you do the following. It will also work for updating the current value
#to a key that is already inside the dictionary

my_dictionary['myAnimal']='Giraffe'
print(my_dictionary)

#THis one prints all the keys and / or  values in a given my_dictionary

print(my_dictionary.keys())
print(my_dictionary.values())

#THis one prints all the keys and value sets from a given my_dictionary

print(my_dictionary.items())

#This one updates one dictionary with entries from a different my_dictionary

my_new_dic={'myFavGame':'God of War'}
my_dictionary.update(my_new_dic)
print(my_dictionary)

#This one deletes a key / value entry from a my_dictionary

my_dictionary.pop('mySecondFruit')
print(my_dictionary)

#This one removes the last added entry into the dictionary and converts the removed key / value set to Tuple
removed_item=my_dictionary.popitem()
print(removed_item,type(removed_item))

#This one creates a dictionary from a list

my_list=[1,4,3,2,'dupa',190]
my_new_dic=dict.fromkeys(my_list)
print(my_new_dic)
#This one allows to add a new key to the existing dictionaty with a default value. If the given key already exists,
#it will not have its value updated

my_new_dic.setdefault('cipa','ciasna')
print(my_new_dic)
