# take a column of the dataframe and return a list of the values in that column
def returnList(df, column):
    return df[column].tolist()


# print number of times a each word appears in a list
def countOccurances(list):
    counts = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


# count number of times unique key combinations comes up in a dictionary
def countUniqueCombinations(dict):
    counts = {}
    for key, value in dict.items():
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts


# split each key in a dictoinary into a list of words and count the number of times each word appears
def countWords(dict):
    counts = {}
    for key in dict:
        words = key.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts


# take a list of seasons and year and return the list of years
def getYears(list):
    years = []
    for item in list:
        year = item.split(" ")
        years.append(year[1])
    return years


# print(getYears(listOfYears))

# turn each key value pair in a dicitionary into a list of lists
def dictToLists(dict):
    lists = []
    for key, value in dict.items():
        lists.append([key, value])
    return lists


testDict = {
    "Action": 792,
    "Adventure": 500,
    "Comedy": 935,
    "Drama": 601,
    "Sci-Fi": 518,
    "Space": 99,
}
print(dictToLists(testDict))


# order dicitionary by value decreasing
def orderDict(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


from itertools import groupby
import os
import seaborn as sns
import matplotlib.pyplot as plt

# put a list back to one string
def listToString(list):
    string = ""
    for item in list:
        string += item + " "
    return string


# split a list of string into words, sort the words, then put the string back together
def splitStringToWords(list):
    words = []
    goodList = []
    for item in list:
        words.append(sorted(item.split(", ")))

    for item in words:
        goodList.append(listToString(item))

    return goodList


testList2 = ["Action, Adventure, Love", "Love, Action, Adventure"]
print(splitStringToWords(testList2))
