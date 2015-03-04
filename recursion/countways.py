# boy climbing n step stairs , he can hop 1 step, 2 steps, 3 steps at a time. find all the combinations.

def countways(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return countways(n-1) + countways(n - 2) + countways(n-3)

# robot on NxN grid can move right or down. find ways

def robotways(m,n):
  if (m == 0 or n == 0) :
    return 1

  return robotways(m-1 , n ) + robotways(m , n-1 )

# subsets of a set
def findsubset(currset):
   
  if len(currset) == 0 :
    setlist = []
    setlist.append(set())
    return setlist
  else:
    elem = currset.pop()
    subsetlist = findsubset(currset)
    setlist = []
    for sub in subsetlist:
        x = sub.union(elem)
        setlist.append(sub)
        setlist.append(x)
    return setlist

def findAnagrams(currstr):
  if len(currstr) <= 1 :
    return [currstr]
  else:
    ch = currstr[-1:]
    substrlist = findAnagrams(currstr[:-1])
    newlist = [ch]
    for item in substrlist:
      newlist.append(item)
      i = 0
      
      for pos in range(0,len(item)+1):
        newlist.append(item[:pos] + ch + item[pos:])
    return newlist

def printpar(n):
  if n == 1 :
    return set(['()'])
  if n < 1:
    return ''
  newset = set()
  oldset = printpar(n-1)
  for item in oldset:
    # print item
    newset =  newset | addPar(item)
    print 'new' , newset
  
  return newset

def addPar(somestr):
  par = '()'
  combos = set()
  for i in range(0, len(somestr) + 1):
    combos.add(somestr[:i] + par + somestr[i:])
  print 'combos', combos
  return combos


def change(n, deno, combi):
  denos = [25, 10, 5]
  if n < 0: 
    combi = ""
    return 0
  if n == 0: 
    print combi
    return 1
  count = 0
  
  # print 'money left %s, current deno %s' % (n , deno)
  for m in denos: 
    if m <= deno :
      count += change(n - m, m, combi + " " + str(m))
  return count

def main():
  print change(100, 25, "")

if __name__ == '__main__':
  main()