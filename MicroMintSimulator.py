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

def throwBalls(k, u, c):
    bins = {}
    mintedCoins = 0
    tossedBalls = 0
    usedBins = []
    numberOfTossesNeededForMinting = []
    while(mintedCoins < c):
        tossedBalls += 1
        binIndex = random.randrange(2**u)
        #binHash = hashlib.md5(binIndex.to_bytes(100, byteorder='big')).hexdigest()
        binKey = "bin" + str(binIndex)
        if(binKey in bins):
            bins[binKey] += 1
        else:
            bins[binKey] = 1
        
        if(bins[binKey] == k and binKey not in usedBins):
            mintedCoins +=1
            numberOfTossesNeededForMinting.append(tossedBalls)
            tossedBalls = 0
            usedBins.append(binKey)
    #print(mintedCoins, "coins has been minted!")
    #print("Threw", tossedBalls, "balls in total")
    return numberOfTossesNeededForMinting

def calculateConfidenceIntervalDifference(data, simulationCounter, mean, deviation, lamda):
    minValue = mean - (lambdaValue * (deviation/math.sqrt(simulationCounter)))
    maxValue = mean + (lambdaValue * (deviation/math.sqrt(simulationCounter)))
    return maxValue - minValue
    

if __name__ == "__main__":
    #parameters = getParameters()
    #u = int(parameters["u"])
    #k = int(parameters["k"])
    #c = int(parameters["c"])
    #widthOfConfidenceInterval = int(parameters["woci"])
    u = 16
    k = 2
    c = 1
    widthOfConfidenceInterval = 22
    #bins = createBins(u)
    data = []
    simulationCounter = 0
    lambdaValue = 3.66
    calculatedWidth = widthOfConfidenceInterval + 1 # This way we will allways enter the while loop.
    while(calculatedWidth > widthOfConfidenceInterval):
        simulationCounter += 1
        data += throwBalls(k, u, c)
        if(len(data) < 2): # Without alleast 2 values we cant calculate deviation. 
            continue
        mean = statistics.mean(data)
        deviation = statistics.stdev(data)
        calculatedWidth = calculateConfidenceIntervalDifference(data, simulationCounter, mean, deviation, lambdaValue)
        print(calculatedWidth)
    print("The mean value is:", statistics.mean(data))


