# basic function plots two lists as x and y values
# other data structures more powerful, but using list to demo this
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin quad') # must make figure active before invoking label
plt.clf() # clear frame to make sure not used previously somewhere else
plt.ylim(0, 1000) # set the y-axis limit
# plt.title('Linear')
# plt.xlabel('sample points')
# plt.ylabel('linear function') 
plt.plot(mySamples, myLinear, 'b-', label='linear') # b and r are colors and - and o are the point data displays
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0) # size of pixels on the graph for line width
plt.legend(loc='upper left') # plt.legend() <-- lets pylab decide
plt.title('Linear vs. Quadratic')

# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cube')
# plt.plot(mySamples, myCubic)
# plt.figure('expo')
# plt.plot(mySamples, myExponential)