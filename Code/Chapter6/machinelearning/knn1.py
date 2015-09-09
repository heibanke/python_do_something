# -*- coding: utf-8 -*-
# CopyRight by heibanke

import pandas as pd
import numpy as np
import time

def normalize(x):
    """
    linalg.norm(x), return sum(abs(xi)**2)**0.5
    apply_along_axis(func, axis, x),
    """
    norms = np.apply_along_axis(np.linalg.norm, 1, x) + 1.0e-7
    return x / np.expand_dims(norms, -1)

def normalize2(x):
    """
    linalg.norm(x), return sum(abs(xi)**2)**0.5
    apply_along_axis(func, axis, x),
    """
    norms = np.apply_along_axis(np.mean, 1, x) + 1.0e-7
    return x - np.expand_dims(norms, -1)

    
def nearest_neighbor(norm_func,train_x, train_y, test_x):
    train_x = norm_func(train_x)
    test_x = norm_func(test_x)
    
    # cosine
    corr = np.dot(test_x, np.transpose(train_x))
    argmax = np.argmax(corr, axis=1)
    preds = train_y[argmax]

    return preds

def validate(preds, test_y):
    count = len(preds)
    correct = (preds == test_y).sum()
    return float(correct) / count

if __name__=='__main__':
    TRAIN_NUM = 22000
    TEST_NUM = 42000
    # Read data 42000
    data = pd.read_csv('train.csv')
    train_data = data.values[0:TRAIN_NUM,1:]
    train_label = data.values[0:TRAIN_NUM,0]
    test_data = data.values[TRAIN_NUM:TEST_NUM,1:]
    test_label = data.values[TRAIN_NUM:TEST_NUM,0]

    norm_funcs = [normalize,normalize2]
    for norm_f in norm_funcs:
        t = time.time()
        preds = nearest_neighbor(norm_f,train_data, train_label, test_data)
        acc = validate(preds, test_label)
        print("%s Validation Accuracy: %f, %.2fs" % (norm_f.__name__,acc, time.time() - t))


    # 2200 , 91.9%
    # 22000, 96.6%

