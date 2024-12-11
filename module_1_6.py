# работа со словарями
my_dict = {"Alex": 1986, "Vasiliy": 1993, "Dormidont": 1966}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get ('Ivan'))
my_dict.update({'Sofia': 2001, 'Ben': 2012})
print(my_dict)
del_ = my_dict.pop('Alex')
print(del_)
print(my_dict)
# работа с множествами
my_set = {1,2,3,4,'Alex', 5,1,2,1,3,5,3,'Alex', True}
print(my_set)
#my_set.add(555)
#my_set.add('Ivan') способ 1
my_set.update({'Ivan'},{555}) #способ 2
my_set.remove(1)
print(my_set)








