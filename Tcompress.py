import my_itertools

def test_compress():
    for i in my_itertools.compress([i for i in range(3)], [True, False, True, False]):
        print(i)

test_compress()

