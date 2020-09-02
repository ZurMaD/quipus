#%%
from quipus import HLNB_BC,Quipus
import tools

# from main import Quipus,getDataCSV
# import normalization as norm
# import networkBuilding as nBuilding
# import predict as predict
import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt
# import math
# import pandas as pd
# from datetime import datetime
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import KFold, ShuffleSplit, StratifiedKFold

# from sklearn.model_selection import GridSearchCV
dataset = tools.getDataFromCSV("./dataset/zoo.csv")
#%%
# X_train, X_predict, Y_train, Y_predict = train_test_split(
#     dataset['data'], dataset["target"], test_size=0.20)
# (X_train, X_predict) = norm.preprocess(X_train, X_predict,1)
#%%
# knnTest = 7
# ePercentile = 0.0
# bnnTest = 3
# quipusClass = Quipus(knn=knnTest, ePercentile=ePercentile, bnn=bnnTest, alpha=0.5)
# kfold = KFold(n_splits=5, random_state=42, shuffle=True)
# scores = cross_val_score(
#     quipusClass, dataset["data"], dataset["target"], scoring="accuracy", cv=kfold
# )
# print(scores)
# print("Accuracy: %0.5f (+/- %0.5f)" % (scores.mean(), scores.std() * 2))
#%%

X_train, X_predict, Y_train, Y_predict = train_test_split(
    dataset["data"], dataset["target"], test_size=0.70, stratify= dataset["target"]
)
knnTest = 5
ePercentile = 0.0
bnnTest = 3
print('Quipus')
quipusClass = Quipus(knn=knnTest, ePercentile=ePercentile, bnn=bnnTest, alpha=0.5)
quipusClass.fit(X_train=X_train, Y_train=Y_train)
quipusClass.predict(X_test=X_predict, Y_test=Y_predict)
print('HLBNC')
bnnTest = 1
knnTest = 1
quipusClass = HLNB_BC(knn=knnTest, ePercentile=ePercentile, bnn=bnnTest, alpha=0.5)
quipusClass.fit(X_train=X_train, Y_train=Y_train)
quipusClass.predict(X_test=X_predict, Y_test=Y_predict)
#%%
# tools.drawGraphs(quipusClass.graphs)

#%%
# k=np.array([1,2,3,4,5,6])
# asd=np.reshape(k,(-1,1))
#%%
# test=3
# total=[]
# knnTest=8
# eRadiusTest=0.5
# bnnTest=5
# print ("knn: ",knnTest)
# print ("e-radius: ",eRadiusTest)
# print ("bnnTest: ",bnnTest)
# for alphaTest in [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]:
#     print("alpha: ",alphaTest)
#     quipusClass=Quipus(knn=knnTest,eRadius=eRadiusTest,bnn=bnnTest,alpha=1.0)
#     kfold = KFold(n_splits=5, random_state=42, shuffle=True)
#     scores = cross_val_score(quipusClass,dataset['data'],dataset['target'],scoring="accuracy",cv=kfold)
#     # scores = cross_val_score(quipusClass,dataset['data'],dataset['target'],scoring="accuracy", cv=5)
#     total.append(scores)
#     print(scores)
#     print("Accuracy: %0.5f (+/- %0.5f)" % (scores.mean(), scores.std() * 2))
# total=np.array(total)
# print("----\n->Accuracy Total: %0.5f (+/- %0.5f)" % (total.mean(), total.std() * 2))

# np.savetxt("AlphaVariation"+str()+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),np.array(total),delimiter=",")

# %%
