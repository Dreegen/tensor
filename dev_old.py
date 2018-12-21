import numpy as np
import pandas as pd

# def PreprocessDataset():
from sklearn import preprocessing
data = pd.read_csv('allrecords.csv', index_col=False, low_memory=False)
data = data.reindex(np.random.permutation(data.index))
cols = data.columns

print(f"{data.columns}")
#
# x_columns = cols.drop("match_result")
#
# x = data[x_columns]
# y = data['match_result']
#
# train_max_row = int(data.shape[0]*0.9)
#
# x_train = x.iloc[:train_max_row]
# x_test = x.iloc[train_max_row:]
#
# y_train = y.iloc[:train_max_row]
# y_test = y.iloc[train_max_row:]
#
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
#
# ################Pre-processing###########
# x_train = preprocessing.scale(x_train)
# x_test = preprocessing.scale(x_test)
#
# return x_train, x_test, y_train, y_test
# x_train, x_test, y_train, y_test = PreprocessDataset()
