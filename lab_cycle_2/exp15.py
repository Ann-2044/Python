my_dict={'banana':3,'apple':5,'orange':2,'kiwi':4}
keys_asc=dict(sorted(my_dict.items()))
print("Sorted by keys(ascending):",keys_asc)
keys_desc=dict(sorted(my_dict.items(),reverse=True))
print("Sorted by keys(descending):",keys_desc)
value_asc=dict(sorted(my_dict.items(),key=lambda item:item[1]))
print("Sorted by keys(ascending):",value_asc)
value_desc=dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))
print("Sorted by keys(descending):",value_desc)
