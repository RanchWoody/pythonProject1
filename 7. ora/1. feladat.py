import matplotlib.pyplot as plt
from matplotlib.pyplot import *


x,y,y1,y2 = [], [], [], []


for i in range(11):
    x.append(i)
    y.append(i**2)
    y1.append(i**3)
    y2.append(i**4)


plt.plot(x, y)
plt.show()

plot(x, y, "r--" , label="y")
plot(x, y1, "go", label="y1")
plot(y, y2, "bs", label="y2")
axis([0,10,0,100])
title("My diagram")
xlabel("ezazix")
ylabel("ezazypszilon")
grid(True)
legend()
show()