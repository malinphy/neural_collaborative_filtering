# -*- coding: utf-8 -*-
"""SciBERT demo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HUoQiRKgwlTfZv44ZT8vrJqtSY9B2sXE
"""

### ncf_model prediction
from model import model
import numpy as np 
import tensorflow as tf
import pickle

a_file = open("enc_2item.pkl", "rb")
enc_2item = pickle.load(a_file)

a_file = open("item_2title.pkl", "rb")
item_2title = pickle.load(a_file)

num_users = 943
num_items = 1682

ncf_model = model(num_users, num_items)
ncf_model.load_weights('mlp_model_weights.h5')

def predict(user_id):

    p_user = np.full((num_items-1), user_id, dtype='int32').reshape(-1, 1)  
  
    user_preds = ncf_model.predict([p_user, np.arange(1,num_items).reshape(-1,1)])

    user_preds = tf.math.top_k(tf.squeeze(tf.squeeze(user_preds, axis = 1), axis =1),k =10)[1]
    for i in (np.array(user_preds)):
        print(item_2title[enc_2item[i]])

user_id = 3
predict(user_id)

