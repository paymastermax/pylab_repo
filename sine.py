#import the pylab module.
from pylab import*
#comment on the python script.
title("The sine, cosine and the tan curve")
ylabel("Sine values of corresponding angles")

xlabel(r"Angles 0$\degree$ through 360$\degree$")

def dealer(x):

	#data should be coverted to radian form for calculation to tae place

	x=(x/57.2978)

	return sin(x)


def deale(x):

	#data should be coverted to radian form for calculation to take place

	x=(x/57.2978)

	return cos(x)

data=list()

for y in range(0,390,30):

	data.append(y)

def tane_fun(x):
	x=(x/57.2978)
	return tan(x)

x=list(map(dealer,data))

dat=list(map(deale,data))

tan_values=list(map(tane_fun,data))

ylim(x[0]-2,x[-1]+2)

xlim(data[0],data[-1])

plot(data,x,label="The sine",color="#4c44c4",linestyle="-",linewidth=1.0)
plot(data,tan_values,label="tan values",color="yellow",linewidth=1,linestyle="-")
plot(data,dat,label="The cosine",color="#666666",linestyle="dashed",linewidth=1.0)

legend(loc="upper left")

grid(True)

xticks((0,30,60,90,120,150,180,210,240,270,300,330,360))

show()