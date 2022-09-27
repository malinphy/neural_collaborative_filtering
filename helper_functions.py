# helper functions for ncf
import pandas as pd 
import numpy as np



def encoder_2(df, col):
    df = df.sort_values(by = [col]).reset_index(drop = True)
    unique_features = df[col].unique()
    feature_2enc = {i:j for i,j in enumerate(df[col].unique())}
    enc_2feature = {j:i for i,j in enumerate(df[col].unique())}

    return feature_2enc, enc_2feature
	
def sequencer(df,col):
    var = df.groupby(col).aggregate(lambda tdf: tdf.unique().tolist()) 
    var = var.reset_index()

    return var
	
def train_test_maker(df,col): ### df will be in sequential format
    last_items = []
    for i in range(len(df)):
        last_items.append((df[col][i][-1]))

    mid_items = []
    for i in range(len(df)):
        mid_items.append(df[col][i][:-1])

    return (last_items, mid_items)