import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

### 1
# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [4, 3, 1, 8, 12]

# plt.plot(x, y1, '-o', c='red',  label='line 1')
# plt.plot(x, y2, '-.o', c='green', label='line 2')
# plt.legend()
# plt.show()


#### 2
# x = np.arange(1, 6)
# y1 = [1, 7, 6, 3, 5]
# y2 = [9, 4, 2, 4, 9]
# y3 = [-7, -4, 2, -4, -7]
# plt.subplot(2, 2, (1,2))
# plt.plot(x, y1)
# plt.subplot(2, 2, 3)
# plt.plot(x, y2)
# plt.subplot(2, 2, 4)
# plt.plot(x, y3)
# plt.show()



#### 3
# fig, ax = plt.subplots()
# x = np.linspace(-5, 5, 15)
# y = x**2
# ax.plot(x, y)
# ax.annotate('min', xy=(0,0), xytext=(0,10), arrowprops=dict(facecolor='green'))
# plt.show()



#### 4
# data=np.random.rand(7,7)*10
# fig, ax = plt.subplots(figsize=(11,6))
# c=ax.pcolor(data)
# axs=inset_axes(ax, width='8%', height='50%', loc='lower left', bbox_to_anchor=(1.0, -0.05, 1, 1), bbox_transform=ax.transAxes, borderpad=1.5)
# plt.colorbar(c, cax=axs)
# plt.show()


#### 5

# fig, ax =plt.subplots()
# x=np.linspace(0,5,1000)
# y=np.cos(x*np.pi)
# ax.plot(x,y,color='red')
# ax.fill_between(x,y)
# plt.show()


#### 6

# fig, ax = plt.subplots()
# x1=np.arange(0,0.75,0.0001)
# x2=np.arange(1.25,2.75,0.0001)
# x3=np.arange(3.25,4.75,0.0001)
# y1=-2.75*x1**2+1
# y2=-2.75*(x2-2)**2+1
# y3=-2.75*(x3-4)**2+1
# plt.ylim(-1,1)
# ax.plot(x1,y1, 'b')
# ax.plot(x2,y2, 'b')
# ax.plot(x3,y3, 'b')
# plt.show()


### 7

# fig, axes = plt.subplots(1,3, figsize=(10,4))
# x=np.arange(0,7)
# axes[0].step(x,x, '-go')
# axes[0].grid()
# axes[1].step(x,x, '-go', where='post')
# axes[1].grid()
# axes[2].step(x,x, '-go', where='mid')
# axes[2].grid()
# plt.show()


#### 8
# fig, ax = plt.subplots()
# x=np.arange(0,11,1)
# y1=-0.2*(x-5)**2+5
# y2=-0.3*(x-5)**2+7.7
# y3=-0.15*(x-8)**2+10
# #y2=-0.5*(x-5)**2-15
# ax.stackplot(x,y1,y2, y3)
# plt.legend(['y1', 'y2', 'y3'], loc='upper left')
# plt.show()


##### 9

# fig, ax=plt.subplots()
# vals=[19, 9,37.5, 12.5, 22]
# labels=[ 'Ford','Toyota','BMV', 'AUDI', 'Jaguar']
# exp=[0,0,0.1,0,0]
# ax.pie(vals, labels=labels, explode=exp)
# plt.show()


#### 10

# fig, ax=plt.subplots()
# vals=[19, 9,37.5, 12.5, 22]
# labels=[ 'Ford','Toyota','BMV', 'AUDI', 'Jaguar']
# ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))
# plt.show()
