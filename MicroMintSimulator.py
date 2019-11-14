import sys
import hashlib
import random
import statistics

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
    mintedCoins = 0
    tossedBalls = 0
    usedBins = []
    while(mintedCoins < c):
        tossedBalls += 1
        binIndex = random.randrange(2**int(u))
        binHash = hashlib.md5(binIndex.to_bytes(4, byteorder='big')).hexdigest()
        bins[binHash] += 1
        if(bins[binHash] == k and binHash not in usedBins):
            mintedCoins +=1
            usedBins.append(binHash)
    print(mintedCoins, "coins has been minted!")
    print("Threw", tossedBalls, "balls in total")
    return tossedBalls

def calculateConfidenceInterval(data, simulationCounter, mean, deviation):
    

if __name__ == "__main__":
    #parameters = getParameters()
    #u = parameters["u"]
    #k = parameters["k"]
    #c = parameters["c"]
    #widthOfConfidenceInterval = parameters["woci"]
    u = 16
    k = 2
    c = 1
    widthOfConfidenceInterval = 3
    bins = createBins(u)
    data = []
    simulationCounter = 0
    lambdaValue = 3.66
    calculatedWidth = widthOfConfidenceInterval + 1 # This way we sill allways enter the while loop.
    while(calculatedWidth > widthOfConfidenceInterval):
        simulationCounter += 1
        data.append(throwBalls(bins, k, u, c))
        mean = statistics.mean(data)
        deviation = statistics.stdev(data)
        confInterval = calculateConfidenceInterval(data, simulationCounter, mean, deviation)


