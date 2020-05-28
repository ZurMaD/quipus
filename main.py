# %%
import normalization as norm
import networkBuilding as nBuilding
import drawGraph as draw
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import KFold, ShuffleSplit, StratifiedKFold
import operator
# %%


def getDataCSV(url, className="Class"):
    dataset = {}
    data = pd.read_csv(url, keep_default_na=False,  na_values=np.nan)
    if(len(data.values[0]) == 1):
        data = pd.read_csv(url, ";", keep_default_na=False,  na_values=np.nan)
    dataset['target'] = data[className].values
    dataset['data'] = data.drop(className, axis=1).values
    return dataset


# %%
dataset = getDataCSV("./dataset/redwine.csv")
X_train, X_predict, Y_train, Y_predict = train_test_split(
    dataset['data'], dataset["target"], test_size=0.8)
(X_train, X_predict) = norm.preprocess(X_train, X_predict)

# %%
g, nbrs = nBuilding.networkBuildKnn(
    X_train, Y_train, knn=11, eQuartile=0.50, labels=True)
# draw.drawGraph(g)
nBuilding.insertNode(g, nbrs, X_train[0], Y_train[0])
# draw.drawGraph(g)

def _nNeighbors(g,index,label,deep,result):
    if(deep==0):
        result.append(index)
        return
    index = str(index)
    neighbors = list(nx.neighbors(g, index))
    colors=g.graph["colors"]
    classNames=g.graph["classNames"]
    for node in neighbors:
        color=colors[classNames.index(label)]
        g.edges[str(index),str(node)]["color"]=color
        _nNeighbors(g,node,label,deep-1,result)

def nNeighbors(g,index,deep):
    result = []
    label=g.nodes()[str(index)]["label"]
    _nNeighbors(g,index,label,deep,result)
    result=list(set(result))
    return result
# def secondNeighbors(g, index):
#     index = str(index)
#     neighbors = list(nx.neighbors(g, index))
#     sNeighbors = []
#     sNeighbors.append(neighbors)
#     for n in neighbors:
#         tmpNeighbors = list(nx.neighbors(g, n))
#         sNeighbors.append(tmpNeighbors)
#     sNeighbors = sum(sNeighbors,[])
#     print("secondNeighbors: ",sNeighbors)
#     sNeighbors = list(set(sNeighbors))
#     print("secondNeighbors: ",sNeighbors)
# secondNeighbors(g, g.graph["lnNet"])

neighbors=nNeighbors(g, g.graph["lnNet"],2)
print("neighbors: ",neighbors)
# draw.drawGraph(g)
g1=g.copy()
for node in g.nodes():
    if(not node in neighbors):
        g1.remove_node(node)
print(Y_train[0], g.graph["colors"][Y_train[0]] )
draw.drawGraph(g1)

# %%
