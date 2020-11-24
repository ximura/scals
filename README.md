# scals

### Usage

```
python .\scals\scals.py [ GR 1 test_sets/c.txt [ EQ 3 test_sets/a.txt test_sets/a.txt test_sets/b.txt ] ]
{2, 3}
python .\scals\scals.py [ LE 2 test_sets/a.txt [ GR 1 test_sets/b.txt test_sets/c.txt ] ]
{1, 4}
```

### Testing

#### Run unit tests

```
python -m pytest
============================================================================== test session starts ============================================================================== 
platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: E:\git-repo\scals
collected 3 items                                                                                                                                                                 

tests\test_scals.py ...                                                                                                                                                    [100%] 

=============================================================================== 3 passed in 0.07s =============================================================================== 
```
