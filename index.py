# Supress Warnings

import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package

import numpy as np
import pandas as pd

# Data Visualisation
import matplotlib.pyplot as plt 
import seaborn as sns
# from sklearn.linear_model import LinearRegression

hours_studied=[1.5,3.0,4.5,6.0,7.5]
test_scores=[55,65,75,85,95]
# Calculating a mean of hours studied
mean_of_hours_studied=np.mean(hours_studied)
print(f"mean of hours studied is{mean_of_hours_studied}")
# Calculating a mean of test scores
mean_of_test_scores=np.mean(test_scores)
print(f"mean of test scores is {mean_of_test_scores}")
#Finding a deviation of mean of hours studied
deviation_of_hours_studied=[x - mean_of_hours_studied for x in hours_studied]
print(f"deviation of hours studied is {deviation_of_hours_studied}")
#Finding a deviation of mean of test scores
deviation_of_test_scores=[y - mean_of_test_scores for y in test_scores]
print(f"deviation of test score is {deviation_of_test_scores}")

# Calculating a product of deviation of hours studied and deviation of test scores
product_of_deviation=[a*b for a,b in zip(deviation_of_hours_studied,deviation_of_test_scores)]
print(f"product of deviation are: {product_of_deviation}")

#sum of product of deviation
sum_of_product_of_deviation=0
for i in product_of_deviation:
    sum_of_product_of_deviation+= i
print(f"sum of product of deviation is {sum_of_product_of_deviation}")

# Calculating a square of deviation of hours of studied
square_of_deviation_of_hours_studied=[a**2 for a in deviation_of_hours_studied]
print(f"square of deviation of hours studied is {square_of_deviation_of_hours_studied}")

# Calculating a slope of the line
slope_of_line=sum_of_product_of_deviation/sum(square_of_deviation_of_hours_studied)
print(f"slope of the line is {slope_of_line}")

# Calculating a intercept of the line
intercept_of_line=mean_of_test_scores -( slope_of_line * mean_of_hours_studied)
print(f"intercept of the line is {intercept_of_line}")

# Predicting a test score
predicted_test_score=0
X = 7 # hours studied
if X >= 8.9:
    predicted_test_score=100
    print(f"predicted test score is {predicted_test_score}")
elif X < 0:
    print("Invalid input. Hours studied cannot be negative.")
else:
    predicted_test_score=slope_of_line*X + intercept_of_line
    print(f"predicted test score is {predicted_test_score}")

