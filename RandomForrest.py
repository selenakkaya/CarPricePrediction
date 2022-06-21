#1. kutuphaneler
import matplotlib.pyplot as plt
import pandas as pd

#2.1. Veri Yukleme
data = pd.read_csv('Car.csv')


X = data[['fueltype','aspiration','doornumber','carbody','drivewheel', 'enginelocation','wheelbase', 'enginetype', 'cylindernumber','enginelocation','enginesize', 'fuelsystem', 'horsepower']]
X.count()
y = data['price'] 

X.reset_index(inplace=True)
X = X.drop(columns=['index'])


features = pd.get_dummies(X)


# Use numpy to convert to arrays
import numpy as np
# Labels are the values we want to predict
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

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels);


# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')


# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')




fig = plt.figure()
plt.scatter(test_labels,predictions)
fig.suptitle('test vs pred', fontsize=20)              # Plot heading 
plt.xlabel('test', fontsize=18)                          # X-label
plt.ylabel('pred', fontsize=16)   



