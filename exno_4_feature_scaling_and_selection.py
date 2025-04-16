# -*- coding: utf-8 -*-
"""EXNO:4-Feature Scaling and Selection

Automatically generated by Colaboratory.

Original file is located at
https://colab.research.google.com/drive/1B0d8nz2WoAoDoVJ11BZ2_FIreEEYSidC?usp=sharing
**Feature Scaling**
"""

import pandas as pd
from scipy import stats
import numpy as np

df=pd.read_csv("/content/bmi.csv")

df.head()

df.dropna()

# TYPE CODE TO FIND MAXIMUM VALUE FROM HEIGHT AND WEIGHT FEATURE

from sklearn.preprocessing import MinMaxScaler

#Perform minmax scaler

from sklearn.preprocessing import StandardScaler

#Perform standard scaler

from sklearn.preprocessing import Normalizer

#Perform Normalizer

from sklearn.preprocessing import MaxAbsScaler

#Perform MaxAbsScaler

from sklearn.preprocessing import RobustScaler

#Perform RobustScaler

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import chi2

df=pd.read_csv('/content/titanic_dataset.csv')

df.columns

df.shape

X = df.drop("Survived", 1)       # feature matrix
y = df['Survived']

#drop the following columns -"Name", "Sex", "Ticket", "Cabin", "Embarked" and store it in df1

df1.columns

df1['Age'].isnull().sum()

#fill null values of age column using forward fill method

df1['Age'].isnull().sum()

feature=SelectKBest(mutual_info_classif,k=3)

df1.columns

#Replace the columns from  ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare'] to ['PassengerId', 'Fare', 'Pclass', 'Age', 'SibSp', 'Parch', 'Survived']

X=df1.iloc[:,0:6]
y=df1.iloc[:,6]

X.columns

y=y.to_frame()

y.columns

X = df1.drop("Survived", 1)       # feature matrix
y = df1['Survived']

feature.fit(X,y)

#perform feature selections techniques