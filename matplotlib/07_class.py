''' Histogram - Histogram is a visual representation of the distribution
              data. They group values into bins (intervals)
              and counts how many fall in each range.
'''
import matplotlib.pyplot as plt
import numpy as np

score = np.random.normal(loc=80, scale=10, size=100)
score = np.clip(score, 0, 100)

plt.hist(score, bins=10,
                color="Red",
                edgecolor="Yellow")
plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("No of students")

plt.show()