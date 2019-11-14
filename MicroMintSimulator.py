import sys
import hashlib
import random
import statistics
import math
import time

def getParameters():
    try:
        u = sys.argv[1]
        k = sys.argv[2]
        c = sys.argv[3]
        widthOfConfidenceInterval = sys.argv[4]
        if (u is False or k is False or c is False or widthOfConfidenceInterval is False):
            print("Invalid parameters")
            print("Usage:", '"MicroMintSimulator u k c w"')
            print("For example:", '"python3 MicroMintSimulator.py 16 2 10000 22"')
            exit()
        else:
            return {"u":u, "k":k, "c":c, "woci": widthOfConfidenceInterval}
    except:
        print("Invalid parameters")
        print("Usage:", '"MicroMintSimulator u k c w"')
        print("For example:", '"python3 MicroMintSimulator.py 16 2 10000 22"')
        exit()

def throwBalls(k, u, c):
    bins = {} # Dictonary, compare to Map. 
    mintedCoins = 0
    tossedBalls = 0
    usedBins = []
    while(mintedCoins < c):
        tossedBalls += 1
        binIndex = str(random.randrange(2**u))
        if(binIndex in bins):
            bins[binIndex] += 1 # If it exist we increment. 
        else:
            bins[binIndex] = 1 # Otherwise add it.
        
        if(bins[binIndex] == k and binIndex not in usedBins): # Bingo! we have a match and it is not used before
            mintedCoins +=1
            usedBins.append(binIndex)

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
    data = []
    simulationCounter = 0
    lambdaValue = 3.66
    calculatedWidth = widthOfConfidenceInterval + 1 # This way we will allways enter the while loop.
    print("Simulation starts!")
    start = time.time()
    while(calculatedWidth > widthOfConfidenceInterval):
        simulationCounter += 1
        data.append(throwBalls(k, u, c))
        if(len(data) < 2): # Without alleast 2 values we can't calculate deviation. 
            continue
        mean = statistics.mean(data)
        deviation = statistics.stdev(data)
        calculatedWidth = calculateConfidenceIntervalDifference(data, simulationCounter, mean, deviation, lambdaValue)
        print("Width of confidence interval:", calculatedWidth)
    end = time.time()
    print("The mean value is:", statistics.mean(data))
    print("Time of simulation:", (end - start) / 60, "minutes")


