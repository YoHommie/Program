import matplotlib.pyplot as plt

# to show scatter plot
x=[1,2,3,4,5,6,7,3,2,3,14,1]
y=[1,5,2,1,6,6,21,6,10,8,7,12]


plt.scatter(x,y,label="Skitscat", color='r', marker="o",s=200)

plt.xlabel('x')
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.legend()
plt.show()