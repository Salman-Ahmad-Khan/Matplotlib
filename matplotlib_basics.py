"""  Why Data Visualisation???
Human brain can process information easily when it is in pictorial or graphical form
Data Visualisation allows us to quickly interpret the data and adjust different variables to see their effects.

What is Data Visualisation???
Data Visualisation is the presentation of data in a pictorial or graphical format.

What is Matplotlib???
Matplotlib is a Python package used for 2D graphics

Types of Plots:
1.Bar graph
2.Histogram
3.Scatter plot
4.Pie plot
5.Hexagonal bin plot
6.Area plot
"""

"""First_code:Linear graphs"""
# 1
"""from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.show()

x = [5, 8, 10]
y = [12, 16, 6]

plt.plot(x, y)"""

# 2
"""from matplotlib import pyplot as plt
plt.title("Info")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

plt.show()"""


# 3
# Adding style  to our graph
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x1=[5,8,10]
y1=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x1,y1,'g',label="line one",linewidth=5)
plt.plot(x2,y2,'r',label="line two",linewidth=5)
plt.title("Epic Info")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.legend()
plt.grid(True,color='r')
plt.show()
