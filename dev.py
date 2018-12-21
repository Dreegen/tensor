# data preprocessing
import pandas as pd
# produces a prediction model in the form of an ensemble of weak prediction models, typically decision tree
import xgboost as xgb
# the outcome (dependent variable) has only a limited number of possible values.
# Logistic Regression is used when response variable is categorical in nature.
from sklearn.linear_model import LogisticRegression
# A random forest is a meta estimator that fits a number of decision tree classifiers
# on various sub-samples of the dataset and use averaging to improve the predictive
# accuracy and control over-fitting.
from sklearn.ensemble import RandomForestClassifier
# a discriminative classifier formally defined by a separating hyperplane.
from sklearn.svm import SVC
# displayd data
from IPython.display import display
%matplotlib inline

# Read data and drop redundant column.
data = pd.read_csv('results.csv')

# # Preview data.
# display(data.head())

# what is the win rate for the home team?

# Total number of matches.
n_matches = data.shape[0]

# Calculate number of features. -1 because we are saving one as the target variable (win/lose/draw)
n_features = data.shape[1] - 1

# Calculate matches won by home team.
n_homewins = len(data[data.ftr == '1'])

# Calculate win rate for home team.
win_rate = (float(n_homewins) / (n_matches)) * 100

# -------------- #
# Print the results
print("Total number of matches: {}".format(n_matches))
print("Number of features: {}".format(n_features))
print("Number of matches won by home team: {}".format(n_homewins))
print("Win rate of home team: {:.2f}%".format(win_rate))
# ---------------- #
