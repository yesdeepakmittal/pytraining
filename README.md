# Pytraining
*High Level Compact Overview of Advance Python*

---
### *Interview Q & A for Advance Python*
---
###### Q: Do Objects copied again in Python or same Objects passes as an Argument to the function?
*In Python, Objects do not copied again. For mutuable data types, we can update the Object right in the calling function and we even need not to return it explicitly if there is no brokage of Alaising.*

```python
def test_fn(arr):
    print(id(arr))  # arr is the same argument object 
    
    arr += [101]    #📌 Alias not broken + Addition of the new ele at same memory add. 
    print(id(arr))  #  object is added at memory location | No need to return anything


test_arr = [1,2,3,4,5]
print(id(test_arr))    # id of array before passing into the function

test_fn(test_arr)

print(test_arr)  # Even without returning anything, this array is updated

Output:
139928806989408
139928806989408
139928806989408
[1, 2, 3, 4, 5, 101]
```
```python
def test_fn(arr):
    print(id(arr))  # arr is the same argument object 
    
    arr = arr + [101]    #📌 Alias has broken now
    print(id(arr))      #  after broken of alias, arr needed to return now


test_arr = [1,2,3,4,5]
print(id(test_arr))    # id of array before passing into the function

test_fn(test_arr)

print(test_arr)  # Even without returning anything, this array is updated

Output:
139928716393440
139928716393440
139928807003312
[1, 2, 3, 4, 5]
```

---
### *Blogs & Other resources*
- [Asynchronous Programming in Python](https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb) 
- [Multithreading vs Multiprocessing in Python](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/)
- [Unpacking Dictionary](https://realpython.com/iterate-through-dictionary-python/#using-the-dictionary-unpacking-operator)
