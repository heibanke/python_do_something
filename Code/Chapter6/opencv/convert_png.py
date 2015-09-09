
import pandas as pd
import numpy as np
from PIL import Image

# load data
train = pd.read_csv('train.csv')

# now draw the numbers
for ind, row in train.iloc[1:10].iterrows():
    i = row[0]
    # white background
    arr = np.array(255 - row[1:], dtype=np.uint8)
    #arr = np.array(row[1:], dtype=np.uint8)
    arr.resize((28, 28))
    #save to file
    im = Image.fromarray(arr)
    im.save("./train_pics/%s-%s.png" % (ind, i))

