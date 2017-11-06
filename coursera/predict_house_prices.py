import math
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# load dataset
sales = pd.read_csv('home_data.csv')
# split data to train and test data
train_data, test_data = train_test_split(sales, train_size=0.8, test_size=0.2)

# print sizes to ensure that splitting was correct
print("sales size: {}".format(len(sales)))
print("test_data size: {}".format(test_data.shape))
print("train_data size: {}".format(train_data.shape))

# if train data contains one feature it should be reshaped
# with array.reshape(-1, 1) command
train_data_r = train_data['sqft_living'].values.reshape(-1, 1)
test_data_r = test_data['sqft_living'].values.reshape(-1, 1)

# create prediction model
lm = linear_model.LinearRegression()
model = lm.fit(train_data_r, train_data['price'])
# calculate predictions based on model and test data
prediction = lm.predict(test_data_r)

# print model score and rmse
# Score returns the coefficient of determination R^2 of the prediction.
print()
print("Score: {}".format(model.score(test_data_r, test_data['price'])))
# Calculate the RMSE
mse = mean_squared_error(test_data["price"], prediction)
print("RMSE: {}".format(math.sqrt(mse)))

# get model coefficient
print("Intercept: {}".format(lm.intercept_))
print("Coefficients: {}".format(lm.coef_))

# plot the result
# plt.plot(test_data['sqft_living'], test_data['price'], '.',
#         test_data['sqft_living'], prediction, '-')
# plt.show()

# create multi-features model
print("\n*** Multi-features model ***")
my_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']

mf_lm = linear_model.LinearRegression()
mf_model = mf_lm.fit(train_data[my_features], train_data["price"])
mf_prediction = mf_model.predict(test_data[my_features])

print("Score: {}".format(mf_model.score(test_data[my_features], test_data['price'])))
# Calculate the RMSE
mf_mse = mean_squared_error(test_data["price"], mf_prediction)
print("RMSE: {}".format(math.sqrt(mf_mse)))


# Programming assignment
print("\n*** Programming assignment ***")
# Ex 01
tmp = sales.ix[sales["zipcode"] == 98039]
print("Avg. price: {}".format((tmp["price"]).mean()))

# Ex 02
tmp = sales.ix[(sales["sqft_living"] > 2000) & (sales["sqft_living"] < 4000)]
print("Fraction: {}".format(len(tmp)/len(sales)))

# Ex 03
advanced_features = [
'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
'condition', # condition of house
'grade', # measure of quality of construction
'waterfront', # waterfront property
'view', # type of view
'sqft_above', # square feet above ground
'sqft_basement', # square feet in basement
'yr_built', # the year built
'yr_renovated', # the year renovated
'lat', 'long', # the lat-long of the parcel
'sqft_living15', # average sq.ft. of 15 nearest neighbors
'sqft_lot15', # average lot size of 15 nearest neighbors
]

af_lm = linear_model.LinearRegression()
af_model = af_lm.fit(train_data[advanced_features], train_data["price"])
af_prediction = af_model.predict(test_data[advanced_features])

mf_rmse = math.sqrt(mean_squared_error(test_data["price"], mf_prediction))
af_rmse = math.sqrt(mean_squared_error(test_data["price"], af_prediction))
print("Difference: {}".format(math.fabs(af_rmse - mf_rmse)))