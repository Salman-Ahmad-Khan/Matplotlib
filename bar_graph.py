# Bar graph
# 

from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label="example one")

plt.bar([2,4,6,8,10],[8,6,2,5,6],label="example two,color='r")
plt.legend()
plt.xlabel("Bar number")
plt.ylabel("Bar Height")
plt.title("Sample Bar Graph")

plt.show()