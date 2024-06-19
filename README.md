# yields

Do you know yield in Python?

## Introduction

This repo attempts to re-write some built-in Python functions and classes using the `yield` statement **just for fun**.

The running result of the file `demo/a.py` proves that using the `yield` statement for rewriting actually makes the execution slower.

```bash
# result on my computer
ssum = 99999990000000
Python built-in zip time cost: 1.657429700018838s
ssum = 99999990000000
Python my_zip time cost: 2.7339518000371754s
```