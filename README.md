# CarPricePrediction

A car price model is made by using independent variables which are giving the logical results. That model will provide a possibility to observe the dynamics on pricing for the future markets.

## USED DATA: 
The data set that is going to be used has 26 attributes which are: car ID, symbolling, wheel base, car length, car width, car height, curb wight, engine size, bore
ratio, stroke, compression ratio , horse power, peakepm, citympg, highwaympg and price.
Source of using the data: : https://www.kaggle.com/goyalshalini93/car-data
The algorithms that are going to be used: Simple Linear Regression and Random Forrest 

### Data Preparation: 
• Thirteen attributes are elected from 25 independent values because those attributes have an impact on pricing then others. In other words, only necessary attributes are derived from the dataset and which are:
'fueltype', 'aspiration', 'doornumber', 'carbody',' drivewheel',
'enginelocation', 'wheelbase', 'enginetype', 'cylindernumber',
'enginelocation', 'enginesize', 'fuelsystem', 'horsepower'
• -Price column is determined as dependent variable.
• Other columns are dropped in order to process the determined attributes only.
• Get_dummies() function from pandas library in order to create a new data frame which consists of zeros and ones and make the data processable.

### MODELING 
Skicit-learn is used to split data into training and testing sets.
Data are divided into 25% test, 75% train set. (That is changeable in order to optimize the result.

### LINEAR REGRESSION 
Linear regression is a basic and widely used prediction analysis. Cannot be used in 
categorical data. It enables to establish a relationship between numeric input and output values.
The simplest form of the regression equation with a dependent and an independent variable is defined by the formula:
y = ax + b.
y = dependent variable, a = coefficient, x = independent variable, c = constant.
The amount of error is the distance between a point of real value and a line.


### RANDOM FORREST REFRESSION 
Random Forrest Regression operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. In this study regression feature is used of random Forrest algorithm.
