# neural_collaborative_filtering
Requirements
-------
```
python_version : 3.7.14
numpy_version : 1.21.6
pandas_version : 1.3.5
sklearn_version : 1.0.2
tensorflow_version : 2.8.2
keras_version : 2.8.0
```
Training & Prediction
-------
For ncf_train.py all helper functions, encoding files and model will be imported and model weights and dictionaires will be saved.
<br>
For deployment purpose model nc_predict.py is shared. Model, model weights, and dictionaries will imported and final prediction will performed for selected user.

Dataset
-------
For training and evaluation process ml 100K was used and can be downloaded from links below:
<br>
https://github.com/malinphy/datasets/tree/main/ml100K
<br>
https://grouplens.org/datasets/movielens/100k/
<br>

Evaluation
-------
HR@10 ~=0.70 with 4 random negative samples for training

Reference
-------
```
@inproceedings{10.1145/3038912.3052569,
author = {He, Xiangnan and Liao, Lizi and Zhang, Hanwang and Nie, Liqiang and Hu, Xia and Chua, Tat-Seng},
title = {Neural Collaborative Filtering},
year = {2017},
isbn = {9781450349130},
publisher = {International World Wide Web Conferences Steering Committee},
address = {Republic and Canton of Geneva, CHE},
url = {https://doi.org/10.1145/3038912.3052569},
doi = {10.1145/3038912.3052569},
abstract = {In recent years, deep neural networks have yielded immense success on speech recognition, computer vision and natural language processing. However, the exploration of deep neural networks on recommender systems has received relatively less scrutiny. In this work, we strive to develop techniques based on neural networks to tackle the key problem in recommendation --- collaborative filtering --- on the basis of implicit feedback.Although some recent work has employed deep learning for recommendation, they primarily used it to model auxiliary information, such as textual descriptions of items and acoustic features of musics. When it comes to model the key factor in collaborative filtering --- the interaction between user and item features, they still resorted to matrix factorization and applied an inner product on the latent features of users and items.By replacing the inner product with a neural architecture that can learn an arbitrary function from data, we present a general framework named NCF, short for Neural network-based Collaborative Filtering. NCF is generic and can express and generalize matrix factorization under its framework. To supercharge NCF modelling with non-linearities, we propose to leverage a multi-layer perceptron to learn the user-item interaction function. Extensive experiments on two real-world datasets show significant improvements of our proposed NCF framework over the state-of-the-art methods. Empirical evidence shows that using deeper layers of neural networks offers better recommendation performance.},
booktitle = {Proceedings of the 26th International Conference on World Wide Web},
pages = {173–182},
numpages = {10},
keywords = {collaborative filtering, implicit feedback, deep learning, matrix factorization, neural networks},
location = {Perth, Australia},
series = {WWW '17}
}
```
