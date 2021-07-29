import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def convert(episodeLength):
    episodeLength = episodeLength.split()
    if episodeLength[1] == 'hr.':
        return (int(episodeLength[0]) * 60) + int(episodeLength[2]) 
    elif episodeLength[1] == 'min.':
        return int(episodeLength[0])
    else:
        return 0

    
def returnList(df, column):
    return df[column].tolist()


def countOccurances(listOfGenres):
    counts = {}
    for key in listOfGenres:
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts


def countWordsInDict(dictonary):
    counts = {}
    for key in dictonary:
        words = key.split(', ')
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts
 
    
def dictToLists(dictonary):
    lists = []
    for key, value in dictonary.items():
        lists.append([key, value])
    return lists


def load_and_process(result):
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        result
    )
    df1 = df1[df1!= 'Unknown']
   
    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (
        df1
        .drop(columns = ['MAL_ID', 'Producers', 'Licensors', 'English name', 'Japanese name', 'Score-10', 'Score-9', 'Score-8', 'Score-7', 'Score-6', 'Score-5', 'Score-4', 'Score-3', 'Score-2', 'Score-1'])
        .dropna(axis='rows')
        .rename(columns={"Duration": "Duration (Minutes)"})
        .reset_index(drop = True)
        .astype({"Episodes": int, "Ranked": float, "Score": float})  
    )
    

    return df2