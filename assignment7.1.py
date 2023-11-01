def chop(lst):
    if lst:
        lst.pop(0)
        lst.pop()
    return None

def middle(lst):
    if lst:
        lst.pop(0)
        lst.pop()
    return lst

lst = [1, 2, 3, 4, 5]
print("Original list:", lst)
chop(lst)
print("After chop:", lst)
print("Middle list:", middle(lst))
