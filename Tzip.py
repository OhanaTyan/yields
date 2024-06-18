import my_itertools

for a in my_itertools.zip([1,2,3],[4,5],[6,7,8]):
    print(a)

for a in my_itertools.zip([1,2,3],[4,5,6],[6,7,8], strict=True):
    print(a)

try:
    for a in my_itertools.zip([1,2,3],[4,5,6],[7,8], strict=True):
        print(a)
except Exception as e:
    print(e)