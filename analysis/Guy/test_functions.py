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

# turn each key value pair in a dictionary into a list of tupples
def dictToTupples(dict):
    tupples = []
    for key, value in dict.items():
        tupples.append((key, value))
    return tupples


# turn each key balue pair in a dicitionary into a list of lists
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
