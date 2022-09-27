## ncf model config file
class config:
	LATENT_DIM = 16 ### basically embedding_dimension
	DROP_RATE = 0.2 # dropout rate for dropout layer 
	TRAIN_NEG_NUM = 4 # negative examples for train set
	TEST_NEG_NUM = 100 # negative examples for test set
	NUM_EPOCHS = 10
	BATCH_SIZE = 256