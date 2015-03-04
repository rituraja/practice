# Summary
# A sequential search is O(n) for ordered and unordered lists.
# A binary search of an ordered list is O(logn) in the worst case.
# Hash tables can provide constant time searching.
# A bubble sort, a selection sort, and an insertion sort are O(n2) algorithms.
# A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n) and O(n2).
# A merge sort is O(nlogn), but requires additional space for the merging process.
# A quick sort is O(nlogn), but may degrade to O(n2) if the split points are not near the middle of the list. It does not require additional space.

def bubblesort(mylist):
  for i in range(0,len(mylist)):
    shuffle = False
    for j in range(0, len(mylist) - 1 - i):
      if mylist[j] > mylist[j + 1]:
        mylist[j] , mylist[j + 1] = mylist[j + 1] , mylist[j]  
        shuffle = True
    if not shuffle :
      # break
      pass

    print mylist
  
def selectionsort(mylist):

  for i in range(len(mylist),0, -1):
    max = mylist[0]
    k = 0
    for j in range(i):
      if max < mylist[j]:
        max = mylist[j]
        k = j

    mylist[j] , mylist[k] = mylist[k], mylist[j]
    print mylist

  print 'sorted.... ',mylist


def insertionsort(mylist):
  for i in range(1,len(mylist)):
    num = mylist[i]
    j = i
    while j > 0 and mylist[j-1] > num :
      mylist[j] = mylist[j-1]
      j = j - 1

    mylist[j] = num
    print mylist


#insertionsort([1,4,7,3,2])
# selectionsort([1,4,7,3,2])


def mergesort(alist):
  n = len(alist)
  if n <= 1 :
    return
  else :
    m = n / 2
    left = alist[:m]
    right = alist[m:]
    mergesort(left)
    mergesort(right)
    # merge left & right

    l = 0
    r = 0
    k = 0
    while l < len(left) and r < len(right):
      if left[l] < right[r] :
        alist[k] = left[l]
        l += 1
      else :
        alist[k] = right[r]
        r += 1
      k += 1

    while l < len(left):
      alist[k] = left[l]
      l += 1
      k += 1

    while r < len(right):
      alist[k] = right[r]
      r += 1
      k += 1

    print alist

# mergesort([5,3,8,4,9,0,1,2,7,6])

def findsplitpos(alist, pivot, i, j ):
  done = False
  while not done :
    while i <= j and alist[i] <= pivot :
      i += 1
    while i <= j and alist[j] >= pivot :
      j -= 1

    if i >= j :
      done = True
    else:  
      alist[i], alist[j] = alist[j] , alist[i]

  return j

def quicksort(alist, st, en):
  print 'list %s start %d end %d ' %(alist , st, en)
  if st < en :
    pivot = alist[st]
    k = findsplitpos(alist, pivot, st + 1, en)
    alist[k] , alist[st] = alist[st] , alist[k]
    print "k ", k
    quicksort(alist, st, k - 1 )
    quicksort(alist, k + 1, en)

  return
  
m = [5,2,4,7,8,1,9,3,0,6]
quicksort(m,0,len(m) -1)
print m