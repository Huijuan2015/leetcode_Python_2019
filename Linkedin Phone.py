Linkedin Phone
Event bubbling
Prototype vs. class
Accessibility
Callback vs. promise

1. write a program to list factors of a given number
e.g. for 12, factors are 1, 2., 3, 4, 6, 12
def listFactors(self, num):
  res = []
  for i in range(num): / for i in range(sqrt(n)+1)
    if not (num%i):
      res.append(i)
  return res

2. LinkedIn | Phone Screen | Compact Tree Builder
https://leetcode.com/discuss/interview-question/124893/LinkedIn-or-Phone-Screen-or-Compact-Tree-Builder

3. LinkedIn | Phone Screen | Union of two sorted arrays
https://leetcode.com/discuss/interview-question/349701/LinkedIn-or-Phone-Screen-or-Union-of-two-sorted-arrays
def unionArrays(a, b): # a[] b[]
  [1,2,3,4] [4,5,6,7]
Follow up: Given access to multicore processor, how would you implment the same function so that we can do an union faster 
(in terms of time complexity)
Hint: split the inputs to perform union and merge them back in O(1) time.


4.LinkedIn | N-dimensional list
You are given an N-Dimensional list with 2 methods:
i) getDim -> returns the dimensions .e.g [5,4,3].
ii) getElement([i,j,k]) -> return list[i][j][k] . You have to implement a method to sum all elements in the list.

dims = getDim()
def get_all_elements(dims):
    def get_perms(dims):
        if len(dims) == 1:
            return map(lambda x: [x], list(range(dims[0])))
        else:
            res = []
            for head in range(dims[0]):
                for sub_arr in get_perms(dims[1:]):
                    res.append([head] + sub_arr)
        return res
    elements = [getElement(pos) for pos in get_perms(dims)]
    return elements

Basic--> 
Java memory space, heap stack 
2. interface, abstract 
Synchronized 
4. Throwable: Error, Exception 
5. java garbage collection 
6. synchronized vs ReentrantLock 
7. HTTP TCP UDP 
8. deadlock 
9. mutex Vs semaphore 
10. final finalize finally

 heap vs stack process vs thread





















