import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import Model, Input, layers 
from tensorflow.keras.layers import *
class config:
	LATENT_DIM = 16 ### basically embedding_dimension
	DROP_RATE = 0.2 # dropout rate for dropout layer 
	TRAIN_NEG_NUM = 4 # negative examples for train set
	TEST_NEG_NUM = 100 # negative examples for test set
	NUM_EPOCHS = 10
	BATCH_SIZE = 256
    
    
def model(num_users, num_items):
    emb_dim = config.LATENT_DIM

    user_input = Input(shape = (1,), name = 'user_input')
    item_input = Input(shape = (1,), name = 'item_input')

    user_emb_mlp = Embedding(num_users+1, config.LATENT_DIM, name = 'user_emb_mlp')(user_input)
    item_emb_mlp = Embedding(num_items+1, config.LATENT_DIM, name = 'item_emb_mlp')(item_input)

    user_emb_gmf = Embedding(num_users+1, config.LATENT_DIM, name = 'user_emb_gmf')(user_input)
    item_emb_gmf = Embedding(num_items+1, config.LATENT_DIM, name = 'item_emb_gmf')(item_input)

    mult_layer = Multiply(name = 'element_wise_multiplication_gmf'
                    )([user_emb_gmf, item_emb_gmf])

    concat_layer = Concatenate()([user_emb_mlp,item_emb_gmf])

    dense_1 = Dense(64, activation = 'relu', name = 'dense_1_mlp')(concat_layer)
    dense_1 = Dropout(config.DROP_RATE)(dense_1)
    dense_2 = Dense(32, activation = 'relu', name = 'dense_2_mlp')(dense_1)
    dense_2 = Dropout(config.DROP_RATE)(dense_2)
    dense_3 = Dense(16, activation = 'relu', name = 'dense_3_mlp')(dense_2)
    dense_3 = Dropout(config.DROP_RATE)(dense_3)
    dense_4 = Dense(8, activation = 'relu')(dense_3)
    dense_4 = Dropout(config.DROP_RATE)(dense_4)
    # dense_5 = Dense(4, activation = 'relu')(dense_4)

    neuMF_layer = Concatenate(axis=-1, name = 'NeuMF_layer')([mult_layer,dense_4])

    final = Dense(1, activation = 'sigmoid', name = 'final_layer')(neuMF_layer)

    return Model(inputs = [user_input, item_input], outputs = [final])