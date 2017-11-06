__author__ = 'sjaku'
import sklearn
#print (sklearn.__version__)

import pandas as pd


# load dataset
sales = pd.read_csv('home_data.csv')
price = sales['price'].mean()
print "Avg price: ", price