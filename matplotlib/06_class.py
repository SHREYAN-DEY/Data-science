# scatter graph using matplotlib

# scatter graph - Shows the relationship between two variables
#                 Helps to identify a correlation (+, -, None)
#                 Ex - Study hours vs test scores

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 10]
y = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]

plt.scatter(x, y)
plt.show()