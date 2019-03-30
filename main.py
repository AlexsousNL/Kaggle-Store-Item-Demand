# NEW DATA CHALLENGE #
# URL : https://www.kaggle.com/c/demand-forecasting-kernels-only/data

import pandas as pd
import numpy as np
import fbprophet as prophet
import sklearn

train = pd.read_csv('train.csv')
train.head()

print('End of Program')

