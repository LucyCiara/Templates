import matplotlib.pyplot as plt
import numpy as np
from ast import literal_eval

# Function for extracting data from file.
def dataFromFileExtraction(fileName: str):
    with open(fileName, "r") as inputFile:
        tempList = inputFile.readlines()
        dataDict = {}

        # Creating the keys from the top item of each column.
        for item in tempList[0][:-1].split(","):
            dataDict[item] = []

        # Creating the items for each key.
        for row in tempList[1:]:
            if '"Washington, D.C."' in row:
                row = row.replace('"Washington, D.C."', 'Washington D.C')
            row = row[:-1].split(",")
            tempList = []
            for item in row:
                try:
                    item = literal_eval(item)
                except:
                    pass
                tempList.append(item)
            row = tempList
            for i in range(len(dataDict.keys())):
                dataDict[list(dataDict.keys())[i]].append(row[i])
    return dataDict

# Function for extracting data from file, but making the keys the name of the column
def dataFromFileExtractionRowed(fileName: str, keyNameIndex: int):
    with open(fileName, "r") as inputFile:
        tempList = inputFile.readlines()
        dataDict = {}
        for row in tempList:
            rowList = []
            if '"Washington, D.C."' in row:
                row = row.replace('"Washington, D.C."', 'Washington D.C')
            for item in row.split(","):
                try:
                    item = int(item)
                except:
                    pass
                rowList.append(item)
            key = rowList[keyNameIndex]
            rowList.pop(keyNameIndex)
            dataDict[key] = rowList
    return dataDict

# Function for sorting something by number.
def sortingByNumber(dataDict: dict, numberKey: str, nameKey: str, reverseBool: bool, amountInt: int):
    sortedValues = sorted(dataDict[numberKey], reverse=reverseBool)
    outputStr = ""

    for place in range(amountInt):
        for i in range(len(dataDict[numberKey])):
            if dataDict[numberKey][i] == sortedValues[place]:
                outputStr += f"{dataDict[nameKey][i]}={dataDict[numberKey][i]}\n"
    
    return outputStr

# A function for plotting values on a graph.
# The "section" list is used to choose a range of columns depending on the dataset used.
def graphing(dataDict: dict, xKey: str, yKey: str, section: list):
    # Collects relevant values for the graph.
    xValues = [int(item[:5]) for item in dataDict[xKey][section[0]:section[1]+1]]
    yValues = dataDict[yKey][section[0]:section[1]+1]
    
    # Various pyplot functions for displaying the graph.
    plt.plot(xValues, yValues)
    plt.title("...")
    plt.xlabel("$x$ (...)")
    plt.ylabel("$y$ (...)")
    plt.grid()
    plt.show()

# A function for plotting values on a bar diagram.
# The "section" list is used to choose a range of columns depending on the dataset used.
def barGraphing(dataDict: dict, xKey: str, yKey: str, section: list):
    # Collects relevant values for the graph.
    xValues = [int(item[:5]) for item in dataDict[xKey][section[0]:section[1]+1]]
    yValues = dataDict[yKey][section[0]:section[1]+1]
    
    # Various pyplot functions for displaying the diagram.
    plt.bar(xValues, yValues)
    plt.title("...")
    plt.grid()
    plt.show()

dataDict = dataFromFileExtraction("world_population.csv")
dataDictRowed = dataFromFileExtractionRowed("world_population.csv", 2)
print(sortingByNumber(dataDict, "2022 Population", "Country/Territory", True, 3))
graphing(dataDictRowed, "Country/Territory", "United States", [4, 11])
barGraphing(dataDictRowed, "Country/Territory", "United States", [4, 11])
