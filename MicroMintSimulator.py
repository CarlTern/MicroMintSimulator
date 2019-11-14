import sys
import hashlib
import random
import statistics
import math

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
        print(tossedBalls)
        binIndex = random.randrange(2**int(u))
        #binHash = hashlib.md5(binIndex.to_bytes(100, byteorder='big')).hexdigest()
        bins[str(binIndex)] += 1
        if(bins[binIndex] == k and str(binIndex) not in usedBins):
            mintedCoins +=1
            usedBins.append(str(binIndex))
    print(mintedCoins, "coins has been minted!")
    #print("Threw", tossedBalls, "balls in total")
    return tossedBalls

def calculateConfidenceIntervalDifference(data, simulationCounter, mean, deviation, lamda):
    minValue = mean - (lambdaValue * (deviation/math.sqrt(simulationCounter)))
    maxValue = mean + (lambdaValue * (deviation/math.sqrt(simulationCounter)))
    return maxValue - minValue
    

if __name__ == "__main__":
    parameters = getParameters()
    u = int(parameters["u"])
    k = int(parameters["k"])
    c = int(parameters["c"])
    widthOfConfidenceInterval = int(parameters["woci"])
    #bins = createBins(u)
    data = []
    simulationCounter = 0
    lambdaValue = 3.66
    calculatedWidth = widthOfConfidenceInterval + 1 # This way we will allways enter the while loop.
    while(calculatedWidth > widthOfConfidenceInterval):
        simulationCounter += 1
        data.append(throwBalls([], k, u, c))
        if(len(data) < 2): # Without alleast 2 values we cant calculate deviation. 
            continue
        mean = statistics.mean(data)
        deviation = statistics.stdev(data)
        calculatedWidth = calculateConfidenceIntervalDifference(data, simulationCounter, mean, deviation, lambdaValue)
        print(calculatedWidth)
    print(statistics.mean(data))


