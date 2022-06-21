#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri Onisleme

#2.1. Veri Yukleme
data = pd.read_csv('Car.csv')



x = data[['fueltype','aspiration','doornumber','carbody','drivewheel', 'enginelocation','wheelbase', 'enginetype', 'cylindernumber','enginelocation','enginesize', 'fuelsystem', 'horsepower']]#independant value
y = data['price'] #dependant value


x.reset_index(inplace=True)
x = x.drop(columns=['index'])

features = pd.get_dummies(x)


labels = np.array(y)

# Saving feature names for later use
feature_list = list(features.columns)
# Convert to numpy array
features = np.array(features)


# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

# model inşası (linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_features,train_labels)

y_pred = lr.predict(test_features)

# Calculate the absolute errors
errors = abs(y_pred - test_labels)
# Calculate mean absolute percentage error (MAPE)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

fig = plt.figure()
plt.scatter(test_labels,y_pred)
fig.suptitle('y_test vs y_pred', fontsize=20)              # Plot heading 
plt.xlabel('y_test', fontsize=18)                          # X-label
plt.ylabel('y_pred', fontsize=16)   




