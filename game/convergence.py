import matplotlib.pyplot as plt
import math
# imports the third party libraries used for this code

def taylor_sum(k, n):
    # for given k value of x, calculate the taylor sum with n terms
    if k <= -1 or k > 1:
        # left bound -1 is not included in valid range
        raise ValueError()
    taylor_sum = 0
    # starts the sum at 0
    for i in range(1, n+1):
        # iterates through values of i = 1, ..., n
        if i % 2 == 0: # even values of i
            taylor_sum -= ((k**i)/i)
        else: # odd values of i
            taylor_sum += ((k**i)/i)
    return taylor_sum

x_values = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# list of desired x values for each line plotted
y_values_1 = [] # n = 1
y_values_3 = [] # n = 3
y_values_5 = [] # n = 5
y_values_9 = [] # n = 9
y_values = [] # y = ln(x+1)
# defines the y values of each of the 5 lines

for x in x_values:
    # appends the y values associated to each of the x values, depending on the desired line
    y_values_1.append(taylor_sum(x, 1)) # y value for each x with n = 1
    y_values_3.append(taylor_sum(x, 3))
    y_values_5.append(taylor_sum(x, 5))
    y_values_9.append(taylor_sum(x, 9))
    y_values.append(math.log(x+1)) # y = ln(x+1) value for each x

plt.plot(x_values, y_values_1, label="n=1")
plt.plot(x_values, y_values_3, label="n=3")
plt.plot(x_values, y_values_5, label="n=5")
plt.plot(x_values, y_values_9, label="n=9")
# plots x values with corresponding y values for each line
# x_values, y_values are of type list
plt.plot(x_values, y_values, "k", linewidth=2, label="ln(x+1)")
# line of colour black, width 2

# all lines have been labelled accordingly

plt.title("Taylor sum vs ln(x+1)") # adds a title to graph
plt.legend()
# displays the legend with the label attributed to each line
plt.savefig("taylorsum.png")
# saves the graph in the same folder under taylorsum.png  