import my_itertools

def test_dropwhile():
    for i in my_itertools.dropwhile(lambda a: a<5, range(10)):
        print(i)

test_dropwhile()

