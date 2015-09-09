# -*- coding: utf-8 -*-
# CopyRight by heibanke

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import time



if __name__=='__main__':
    # maximum num is 42000
    TRAIN_NUM = 22000
    TEST_NUM = 42000
    """
    train_data:  训练数据
    train_label: 训练数据的正确输出
    test_data:   测试数据
    test_label:  测试数据的正确输出
    """
    data = pd.read_csv('train.csv')
    train_data = data.values[0:TRAIN_NUM,1:]
    train_label = data.values[0:TRAIN_NUM,0]
    test_data = data.values[TRAIN_NUM:TEST_NUM,1:]
    test_label = data.values[TRAIN_NUM:TEST_NUM,0]


    
    t = time.time()
    # PCA, principal components analysis
    # http://blog.jobbole.com/86905/
    # http://ufldl.stanford.edu/wiki/index.php/%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90
    pca = PCA(n_components=0.8)
    train_x = pca.fit_transform(train_data)
    test_x = pca.transform(test_data)

    #knn regression
    neighbor = KNeighborsClassifier(n_neighbors=4)
    neighbor.fit(train_x, train_label)
    preds = neighbor.predict(test_x)

    acc = float((preds == test_label).sum())/len(test_x)
    print("KNN Validation Accuracy: %f, %.2fs" % (acc, time.time() - t))

    # 22000, 96.7%
    


    #svm（Support Vector Machine） regression
    # 统计学习方法
    # PRML

    t = time.time()
    pca = PCA(n_components=0.8,whiten=True)
    train_x = pca.fit_transform(train_data)
    test_x = pca.transform(test_data)

    svc = svm.SVC(kernel='rbf',C=10)
    svc.fit(train_x, train_label)
    preds = svc.predict(test_x)    
    
    acc = float((preds == test_label).sum())/len(test_x)
    print("SVM Validation Accuracy: %f, %.2fs" % (acc, time.time() - t))

    # 22000, 97.8%
