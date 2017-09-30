import random
from datetime import datetime
import numpy as np

random.seed(datetime.now())

filename = "data_final"

N = 6

W1 =[]
b1 = []
W1.append([[0.0, 0.00979, 0.00545,  -0.00474, -0.0116,  -0.0147],[0.0, 0.0199,  0.0372, 0.048,  0.0516, 0.0513],[0.0, 0.00152,  0.0179, 0.0481, 0.0641, 0.0733],[0.0, 0.00645,  0.0169, 0.0322, 0.0401, 0.0431],[0.0, 0.00717,  0.0088, 0.000599, 0.0061, 0.0143],[1.0, 0.969,  0.94, 0.912,  0.886,  0.863]])
W1.append([[0.00, 0.0146, 0.0181, 0.0226, 0.0269, 0.031],[0.00, 0.00416,  0.0106, 0.00442,  -0.00143, -0.00624],[0.00,  0.0125, 0.042,  0.0675, 0.0794, 0.0867],[0.00,  0.00677,  0.0136, 0.0167, 0.0191, 0.0239],[0.00,  0.00733,    0.0100,   0.0222,   0.0384,   0.0503],[1.00,  0.971,  0.937,  0.907,  0.879,  0.853]])
W1.append([[0.00, 0.00777,  0.00958,  0.0125, 0.0134, 0.0124],[0.00,  0.0135, 0.0149, 0.00677,  0.00475,  0.00365],[0.00, 0.0189, 0.0402, 0.0586, 0.0694, 0.0781],[0.00,  0.00426,  0.00654,  0.0138, 0.0201, 0.0236],[0.00,  0.00487,   0.0150,   0.0267,   0.0372,   0.0451],[1.00, 0.967,  0.939,  0.91, 0.886,  0.865]])
W1.append([[0.00, 0.0049, -0.00153, -0.00396, -0.00544, -0.009],[0.00,  0.0153, 0.0245, 0.0274, 0.0281, 0.0287],[0.00,  0.00958,  0.0326, 0.0515, 0.0642, 0.0752],[0.00,  0.0134, 0.0245, 0.0252, 0.0201, 0.013],[0.00,  0.00312,   0.00901,  0.0199,   0.0345,   0.0481],[1.00, 0.97, 0.939,  0.91, 0.884,  0.859]])
W1.append([[0.00, 0.00728,  0.00759,  0.00695,  0.00366,  -0.00297],[0.00,  0.0193, 0.0242, 0.0197, 0.0188, 0.0207],[0.00,  0.0062, 0.032,  0.0634, 0.0864, 0.104],[0.00, 0.00748,  0.00741,  0.00789,  0.0107, 0.0135],[0.00,  0.00862,   0.0187,   0.0271,   0.0328,   0.0383],[1.00, 0.966,  0.934,  0.904,  0.874,  0.849]])
b1.append([-4.19,-4.1577,-4.127,-4.0979,-4.071,-4.046])
b1.append([-4.19,-4.1593,-4.1241,-4.0924,-4.063,-4.036])
b1.append([-4.19,-4.1558,-4.1261,-4.0964,-4.071,-4.048])
b1.append([-4.19,-4.1591,-4.1264,-4.096,-4.068,-4.043])
b1.append([-4.19,-4.1548,-4.1213,-4.09,-4.058,-4.032])

###############################################
################ data reading #################
###############################################

#f = open("data_remove_duplicate2.csv","r")
#for title remove

for j in range(5):
  f = open(filename+str(j)+".csv","r")
  head = f.readline()
  head = "now, 10min, 20min, 30min, 40min, 50min, result\n"
  xlist = []
  ylist = []
  while True:
    tx = []
    ty = []
    line = f.readline()
    if not line: break
    data = line.split(',')
    for i in range(N):
      tx.append(float(data[i]))
    tmp = float(data[N])
    if(tmp>4.19):
      tmp=1.0
    else:
      tmp=0.0
    ty.append(tmp)
    z = np.dot(tx, W1[j])
    z = z+b1[j]
    for k in range(N):
      if(z[k]>0):
        z[k]=1
      else:
        z[k]=0
    xlist.append(z)
    ylist.append(ty)
  f.close()

  f = open("4"+filename+str(j)+".csv","w")
  f.write(head)
  xlist_len = len(xlist)
  for i in range(xlist_len):
    tmp_str=""
    for k in range(N):
      tmp_str+=str(xlist[i][k])+","
    tmp_str+=str(ylist[i][0])+"\n"
    f.write(tmp_str)
  f.close()
