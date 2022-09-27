### negative makers for ncf
import numpy as np 
import pandas as pd

def train_neg_maker(num_neg, df,col,unique_item_enc):
    num_neg = num_neg
    neg3 = []
    ui= 0
    us = []
    for i in df[col]:
        pos_set = i
        neg2 = []
  
        for j in range(num_neg):
            neg1 = []
            for k in pos_set:
      
                neg_candidate = np.random.randint(1,len(unique_item_enc))
                while neg_candidate in pos_set:
                    neg_candidate = np.random.randint(1,len(unique_item_enc))
                us.append(ui)
      
                neg1.append((neg_candidate))
            neg2.append(np.array(neg1))
        ui += 1
        neg3.append(neg2)
    
    return us, neg3
	
def test_negative_maker(num_neg,df,col,unique_item_enc):
    num_neg = num_neg
    neg3 = []
    ui= 0
    us = []
    neg2 = []
    for i in df[col]:
        pos_set = i
  
        neg1 = []
        for j in range(num_neg):
    
            neg_candidate = np.random.randint(1,len(unique_item_enc))

            while neg_candidate == pos_set:

                neg_candidate = np.random.randint(1,len(unique_item_enc))
            us.append(ui)
      
            neg1.append((neg_candidate))
        neg2.append(np.array(neg1))

    return neg2