from pymatreader import read_mat
import scipy
import random
import numpy as np
from sklearn.metrics import zero_one_loss
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

data = None
Xtrain = None
Xtest = None

if True:
    data = read_mat('data\XwindowsDocData.mat')
    Xtrain = data['xtrain']
    Xtrain = scipy.sparse.csc_matrix.toarray(Xtrain)
    Xtest = data['xtest']
    Xtest = scipy.sparse.csc_matrix.toarray(Xtest)

'''
else:
    data = read_mat('data\20news_w100.mat')
    keys =  list(data.keys())
    X = random.shuffle(keys)
    Xtrain = X[1:60, :]; 
    Xtest = X[61:, :]; 
'''
ytrain = data['ytrain']
ytest = data['ytest']
model = GaussianNB()
ypred_train = model.fit(Xtrain, ytrain).predict(Xtrain)
err_train = np.mean(zero_one_loss(ytrain, ypred_train));
ypred_test = model.fit(Xtrain, ytrain).predict(Xtest)
err_test = np.mean(zero_one_loss(ytest, ypred_test))
print('misclassification rates  on train = '+str(err_train*100) +
      ' pc, on test = '+str(err_test*100)+' pc\n')


C = np.unique(data['ytrain']).size
for i in range (0, C):
    plt.bar(np.arange(0, 600, 1), model.theta_[i, :])
    plt.title('p(xj=1|y='+str(i)+')')
    #plt.savefig(r'..\figures\naiveBayesBow'+str(i)+'ClassCond')
    plt.show()