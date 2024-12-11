# module_1_5
immutable_var = (1,2,'три',1.5)
print(immutable_var)
# immutable_var [0] = 12
       # print(immutable_var) - immutable_var [0] = 12
          # TypeError: 'tuple' object does not support item assignment
mutable_list = [6, 7, 'восемь', 3.5]
print(mutable_list)
mutable_list[0] = 9
mutable_list[1] = 10
mutable_list[2] = 5.5
mutable_list[3] = 'одинадцать'
print(mutable_list)

