
def checkio(data):
    
    some = sorted(data)

    m = len(some) / 2
    if len(some) % 2 == 0 :
        median = (data[m] + data[m+1]) // float(2)
    else:
        median = data[m]

    print m
    print median
    

def main():
    checkio([1,2,3,6,2,1])

if __name__ == '__main__':
    main()