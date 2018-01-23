def f1(a,b=0):
    return((a*a)+b)

def f2(c):
    list(c)
    if len(c) > 0:
        return c[0]
    else:
        return 'BUUUUM'

def f3(a):
     a=str(a)
     d = {'1': 'jeden', '2': 'dwa', '3' : 'trzy'}
     keys_list = d.keys()
     for i in keys_list:
         if a not in d:
             return 'other'
         else:
             for cyfra in d:
                 return d[a]
def f4(string1,string2=""):
    if string1 and string2:
        return (string1+" ma kota i "+string2)
    elif string1:
        return (string1+" ma kota")

def f5(arg1,arg2=1):
    lista=[]
    for 
