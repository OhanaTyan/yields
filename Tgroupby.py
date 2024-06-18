import my_itertools
import itertools

def test_group_by():
    ls = []
    for k,v in itertools.groupby([1,2,2,3,3,1]):    
        print(k)
        print(v)
        ls.append((k, v,))
        for e in v:
            print(' ' + str(e))
    for l in ls:
        print(l[0])
        print(l[1])
        for e in l[1]:
            print('\t' + str(e))

# code from https://blog.csdn.net/carol_in_love/article/details/81435837

def test_my_group_by():
    ls = []
    for k,v in my_itertools.groupby([1,2,2,3,3,1]):    
        print(k)
        print(v)
        ls.append((k, v,))
        for e in v:
            print(' ' + str(e))
    for l in ls:
        print(l[0])
        print(l[1])
        for e in l[1]:
            print('\t' + str(e))


test_group_by()
test_my_group_by()