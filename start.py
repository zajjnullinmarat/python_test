<<<<<<< HEAD
def check_duplicated(lst):
    return len(lst) != len(set(lst))
print(check_duplicated([1,2,3,4,5,4,6])) # True
print(check_duplicated([1,2,3])) # False
print(check_duplicated([1,2,3,4,9])) # False
=======
def check_duplicates(lst):
    return len(lst) != len(set(lst))
print(check_duplicates([1,2,3,4,5,4,6])) # True
print(check_duplicates([1,2,3])) # False
print(check_duplicates([1,2,3,4,9])) # False
>>>>>>> bogdan
print("success")