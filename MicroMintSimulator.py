import sys
import hashlib
def getParameters():
    try:
        u = sys.argv[1]
        k = sys.argv[2]
        c = sys.argv[3]
        widthOfConfidenceInterval = sys.argv[4]
        if (u is False or k is False or c is False or widthOfConfidenceInterval is False):
            print("Invalid parameters")
            exit()
        else:
            return {"u":u, "k":k, "c":c, "woci": widthOfConfidenceInterval}
    except:
        print("Invalid parameters")
        exit()

def createBins(u):
    bins = {}
    roof = 2**int(u)
    for i in range(0, roof):
        index = i.to_bytes(4, byteorder='big')
        bins[hashlib.md5(index).hexdigest()] = 0
    return bins

def throwBalls(bins, k, u, c):
    counter = 0
    while(counter < c):
        pass

if __name__ == "__main__":
    #parameters = getParameters()
    #u = parameters["u"]
    #k = parameters["k"]
    #c = parameters["c"]
    #widthOfConfidenceInterval = parameters["woci"]
    u = 12
    k = 12
    c = 12
    widthOfConfidenceInterval = 3
    bins = createBins(u)
    print(bins)
    throwBalls(bins, k, u, c)
    #Skapa lista med 2^n platser. 
    # Vi kastar ca k2n bollar

    #Räknare som vid varje kast kollar om ett nytt mynt har skapats och ökas?
    #Om ett mynt skapas i en plats så kommer denna plats stängas och inte ta emot fler bollar, Ha en separat lista som har koll på 
    # om platsen e stängd