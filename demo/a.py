import time

def my_zip(l1, l2):
    l1 = iter(l1)
    l2 = iter(l2) 
    try:
        while True:
            yield next(l1), next(l2),
    except StopIteration:
        return

def my_zip(l1, l2):
    for i in range(min(len(l1), len(l2))):
        yield l1[i], l2[i]
    
l = list(range(10000000))

start = time.perf_counter()
ssum = 0
for i, j in zip(l, l):
    ssum += i+j
print(f"ssum = {ssum}")
end = time.perf_counter()
runtime = end-start
print(f"Python built-in zip time cost: {runtime}s")

start = time.perf_counter()
ssum = 0
for i, j in my_zip(l, l):
    ssum += i+j
print(f"ssum = {ssum}")
end = time.perf_counter()
runtime = end-start
print(f"Python my_zip time cost: {runtime}s")



