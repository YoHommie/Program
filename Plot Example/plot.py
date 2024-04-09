import matplotlib.pyplot as plt  # improting the matplotlib

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]
plt.plot(x, y, label="First Line")  # for adding labels
plt.plot(x2, y2, label="Second line")

plt.xlabel("Plot Number")  # for showing the x-axis label
plt.ylabel("Improtant Var")  # for showing the y-axis label


plt.title("Important Title\nCheck it out")
plt.legend()  # for showing the ledgends
plt.show()
