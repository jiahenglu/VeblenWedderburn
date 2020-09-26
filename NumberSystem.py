listoflists = []
list = []
for i in range(0,10):
    list.append(i)
    if len(list)>3:
        list.remove(list[0])
        listoflists.append((list, list[0]))


def numeric_compare(alist1, alist2):
    list1 = alist1[0]
    list2 = alist2[0]
    for i in range(0,len(list1)):
        if list1[i] != list2[i]:
            return list1[i] - list2[i]
    return 0

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

list1 = [4,4,8]
list2 = [1,2,3]
list3 = [1,3,9]
alist1 = [list1,-1]
alist2 = [list2,1]
alist3 = [list3,-7]
listoflists = [alist1,alist2,alist3]

listoflists.sort(key=cmp_to_key(numeric_compare))

def multiply(onelist,varlist):
  for i in range(0,len(onelist)):
      partlist1 = (onelist[i])[0]
      partlist1.append(varlist[0])
      partlist1.sort()
      (onelist[i])[1] = (onelist[i])[1] * varlist[1]
      
  return onelist

varlist = [6, 2]
n = multiply(listoflists,varlist)
print(n)
        

