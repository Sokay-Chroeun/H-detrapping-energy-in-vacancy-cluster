import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_excel('Epi_Hou.xlsx')

x1 = np.linspace(1,7, 50)
y1 = -0.0152*x1**2 + 0.029*x1 + 1.3743+0.19

x1 = np.linspace(1,6, 50)
y1 = -0.004*x1**3 + 0.0205*x1**2 - 0.11*x1 + 1.5

x2 = np.linspace(1,11, 50)
y2 = -0.0053*x2**2 - 0.0179*x2 + 1.6814+0.19

x3 = np.linspace(1,15, 50)
y3 = -0.0023*x3**2 - 0.0307*x3 + 1.8121+0.19
y3 = -0.0004*x3**2 - 0.0678*x3 + 1.9681+0.19

x4 = np.linspace(1,19, 50)
y4 = -0.0017*x4**2 - 0.022*x4 + 1.8651+0.19
#y4 = -0.0027*x4**2 + 0.00001*x4 + 1.8051+0.19

x5 = np.linspace(1,23, 50)
y5 = -0.0011*x5**2 - 0.0169*x5 + 1.849+0.19

x6 = np.linspace(1,27, 50)
y6 = -0.001*x6**2 - 0.0146*x6 + 1.8864+0.19

x7 = np.linspace(1,31, 50)
y7 = -0.0007*x7**2 - 0.0146*x7 + 1.8835+0.19

x8 = np.linspace(1,34, 50)
y8 = -0.0007*x8**2 - 0.0116*x8 + 1.8996+0.19

x9 = np.linspace(1,38, 50)
y9 = -0.0004*x9**2 - 0.0153*x9 + 1.9063+0.19

#=====================================================
x1 = np.linspace(0,7, 50)
y1 = -0.0152*x1**2 + 0.029*x1 + 1.37+ 0.19

x1 = np.linspace(0,6, 50)
y1 = -0.004*x1**3 + 0.0205*x1**2 - 0.11*x1 + 1.5

y = []
for i in range(len(x1)):
    x = x1[i]
    if x>1:
        y.append(y1[i])
    else:
        y.append(1.4)
y1 = y

x2 = np.linspace(0,11, 50)
y2 = -0.009*x2**2 + 0.035*x2 + 1.58 + 0.19

y = []
for i in range(len(x2)):
    x = x2[i]
    if x>2:
        y.append(y2[i])
    else:
        y.append(max(y2))
y2 = y

x3 = np.linspace(0,15, 50)
y3 = -0.0053*x3**2 + 0.0200*x3 + 1.70 + 0.19 

y = []
for i in range(len(x3)):
    x = x3[i]
    if x>1.5:
        y.append(y3[i])
    else:
        y.append(max(y3))
y3 = y

x4 = np.linspace(0,19, 50)
y4 = -0.0034*x4**2 + 0.0180*x4 + 1.71 + 0.19

y = []
for i in range(len(x4)):
    x = x4[i]
    if x>2:
        y.append(y4[i])
    else:
        y.append(max(y4))
y4 = y

x5 = np.linspace(0,23, 50)
y5 = -0.0025*x5**2 + 0.0160*x5 + 1.72 + 0.19

y = []
for i in range(len(x5)):
    x = x5[i]
    if x>3:
        y.append(y5[i])
    else:
        y.append(max(y5))
y5 = y

x6 = np.linspace(0,27, 50)
y6 = -0.0019*x6**2 + 0.015*x6 + 1.74 + 0.19

y = []
for i in range(len(x6)):
    x = x6[i]
    if x>4:
        y.append(y6[i])
    else:
        y.append(max(y6))
y6 = y

x7 = np.linspace(0,31, 50)
y7 = -0.0013*x7**2 + 0.0090*x7 + 1.75 + 0.19

y = []
for i in range(len(x7)):
    x = x7[i]
    if x>4:
        y.append(y7[i])
    else:
        y.append(max(y7))
y7 = y

x8 = np.linspace(0,34, 50)
y8 = -0.0011*x8**2 + 0.0065*x8 + 1.76 + 0.19

y = []
for i in range(len(x8)):
    x = x8[i]
    if x>2:
        y.append(y8[i])
    else:
        y.append(max(y8))
y8 = y

x9 = np.linspace(0,38, 50)
y9 = -0.0009*x9**2 + 0.006*x9 + 1.77 + 0.19

y = []
for i in range(len(x9)):
    x = x9[i]
    if x>3:
        y.append(y9[i])
    else:
        y.append(max(y9))
y9 = y
#=====================================================


plt.plot(x1,y1,label='V1',color='black')
plt.plot(x2,y2,color='tab:blue')
plt.plot(x3,y3,color='tab:orange')
plt.plot(x4,y4,color='tab:green')
plt.plot(x5,y5,color='tab:red')
plt.plot(x6,y6,color='tab:purple')
plt.plot(x7,y7,color='tab:brown')
plt.plot(x8,y8,color='tab:pink')
plt.plot(x9,y9,color='tab:cyan')

#plt.scatter([1, 2, 3, 4, 5, 6], [1.44, 1.43, 1.17, 1.11, 0.85, 0.75], label = 'V1')
#plt.scatter(data1.v1, np.array(data1.Ep1)+0.19, label='V1')
plt.scatter(data1.v2, np.array(data1.Ep2)+0.19, label='V2',color='tab:blue')
plt.scatter(data1.v3, np.array(data1.Ep3)+0.19, label='V3',color='tab:orange')
plt.scatter(data1.v4, np.array(data1.Ep4)+0.19, label='V4',color='tab:green')
plt.scatter(data1.v5, np.array(data1.Ep5)+0.19, label='V5',color='tab:red')
plt.scatter(data1.v6, np.array(data1.Ep6)+0.19, label='V6',color='tab:purple')
plt.scatter(data1.v7, np.array(data1.Ep7)+0.19, label='V7',color='tab:brown')
plt.scatter(data1.v8, np.array(data1.Ep8)+0.19, label='V8',color='tab:pink')
plt.scatter(data1.v9, np.array(data1.Ep9)+0.19, label='V9',color='tab:cyan')

plt.legend(ncol=2)
plt.xlabel('Number of trapped H atoms $\\alpha_i$',fontsize=12)
plt.ylabel('Detrapping Energy $E_P$ [eV]',fontsize=12)
plt.ylim([0.6,2.4])
plt.xlim([1,40])
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
#plt.savefig("Ep_Hou.png",bbox_inches='tight')