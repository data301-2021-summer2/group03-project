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



def load_and_process(result):
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        result
    )
    df1 = df1[df1!= 'Unknown']
    
    # df1['Anime_ID'] = df1.index
    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (
        df1.drop(['MAL_ID','Producers', 'Licensors', 'English name', 'Japanese name'], axis=1)
        .dropna(axis='rows')
        # .rename(columns={"Duration": "Duration (Minutes)"})
            # .rename(columns={"Weather_Conditions": "Weather_Type", "Did_Police_Officer_Attend_Scene_of_Accident": "Police_Presense"})
            # .replace({'Police_Presense': {'Yes': True, 'No': False}})
            # .replace({'Day_of_Week': {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}})
            # .convert_dtypes()
            # .sort_values("Year", ascending=True)
    )
    #   df2['Date'] = pd.to_datetime(df2['Date'], format='%d/%m/%Y')
    for ind in df2.index:
        df2.loc[ind, 'Duration'] = convert(df2['Duration'][ind])

    return df2