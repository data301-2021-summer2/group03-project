# take a column of the dataframe and return a list of the values in that column
def returnList(df, column):
    return df[column].tolist()

# print number of times a word appears in a list

def countOccurences(word, list):
    count = 0
    for item in list:
        if item == word:
            count += 1
    return count
