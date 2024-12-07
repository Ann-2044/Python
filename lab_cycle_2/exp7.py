list1=input("Enter colors for list1 :")
list2=input("Enter colors for list2 :")
set1=set(list1.split(','))
set2=set(list2.split(','))
difference=set1-set2
print(f"colors in list1 but not in list2:{difference}")
