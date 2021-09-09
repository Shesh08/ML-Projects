import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz

dataset = np.array( 
[['Asset Flip', 100, 1000], 
['Text Based', 500, 3000], 
['Visual Novel', 1500, 5000], 
['2D Pixel Art', 3500, 8000], 
['2D Vector Art', 5000, 6500], 
['Strategy', 6000, 7000], 
['First Person Shooter', 8000, 15000], 
['Simulator', 9500, 20000], 
['Racing', 12000, 21000], 
['RPG', 14000, 25000], 
['Sandbox', 15500, 27000], 
['Open-World', 16500, 30000], 
['MMOFPS', 25000, 52000], 
['MMORPG', 30000, 80000] 
]) 
print(dataset)
X = dataset[:, 1:2].astype(int)
print(X)

y = dataset[:, 2].astype(int)
print(y)

regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

export_graphviz(regressor, out_file ='tree.dot', 
               feature_names =['Production Cost'])  
X_grid = np.arange(min(X), max(X) ,0.01)
X_grid = X_grid.reshape((len(X_grid) ,1))
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')  
plt.title("Profit to production cost (Decision Tree Regression)")
plt.xlabel('Production Cost')
plt.ylabel('Profit')
plt.show()


