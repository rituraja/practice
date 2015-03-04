
def rnum(ch):
    if ch == 'I':
        n = 1
    if ch == 'V' :
        n = 5
    if ch == 'X' :
        n = 10
    if ch == 'L' :
        n = 50
    return n
    
    
def convertRoman(s):
    num = 0
    l = len(s)
    print s, l
    for i in range(l-1, 0-1, -1):
        
        ch = s[i]
        n = rnum(ch)
        print 'ch', ch, n
        if i == l -1 :
            num = n
        else:
            rn = rnum(s[i+1])
            print "rn" , rn
            if n >= rn  :
                num += n            
            else:
                num -= n
                      
    return num

def main():
     print convertRoman('LV')

if __name__ == '__main__':
    main()