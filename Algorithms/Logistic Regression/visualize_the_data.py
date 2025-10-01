import pandas as pd 
import matplotlib.pyplot as plt  #Required to show the graph, Without this we will not be albe to see the grraph.

data = pd.read_csv('Algorithms/Logistic Regression/study_hours_pass.csv')

print(data.head())
data.plot(x='study_hours', y='passed', kind='scatter')
plt.show()