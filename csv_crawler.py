# -*- coding: cp950 -*-
import requests
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from io import StringIO
import geopandas as gpd
import pandas as pd
import numpy as np
import adjustText as aT

url = 'http://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=C4A5FB3B-1807-4741-A1C0-CF73E49220D7'
data = requests.get(url, verify=False)
result = list(csv.reader(StringIO(data.text)))
cityName = ['�s�_�� New Taipei', '�O�_�� Taipei', '��饫 Taoyuan', '�O���� Taichung', '�O�n�� Tainan', '������ Kaohsiung', '�y���� Yilan',
     '�s�˿� Hsinchu', '�]�߿� Miaoli', '���ƿ� Changhua', '�n�뿤 Nantou', '���L�� Yunlin', '�Ÿq�� Chiayi', '�̪F�� Pingtung', '�O�F�� Taitung',
     '�Ὤ�� Hualien', '��� Penghu', '�򶩥� Keelung','�s�˥� Hsinchu','�Ÿq�� Chiayi', '������ Kinmen', '�s���� Lianjiang']
Doctor = 0
  master = 0
college = 0
Acollege = 0
high = 0
sec = 0
ele = 0
k = -1
x = -1
age15 = 0
age19 = 0
age19to24 = 0
age29 = 0
age34 = 0
age39 = 0
age44 = 0
age49 = 0
age50 = 0
##
DOC=[]
MASTER=[]
COLLEGE=[]
ACOLLEGE=[]
HIGH=[]
SEC=[]
ELE=[]
Age15 = []
Age19 = []
Age24 = []
Age29 = []
Age34 = []
Age39 = []
Age44 = []
Age49 = []
Age50 = []
loc=[]
locAge=[]
##

def printresult(k, Doc, master, college, Acollege, high, sec, ele):
    print(ciytName[k],'\n')
    print('�դh���~:', Doc, '�H')
    print('�Ӥh���~:', master, '�H')
    print('�j�ǲ��~:', college, '�H')
    print('�M�첦�~:', Acollege, '�H')
    print('�������~:', high, '�H')
    print('�ꤤ���~:', sec, '�H')
    print('��p�H�U���~:', ele, '�H')
    DOC.append(Doc)
    MASTER.append(master)
    COLLEGE.append(college)
    ACOLLEGE.append(Acollege)
    HIGH.append(high)
    SEC.append(sec)
    ELE.append(ele)
    loc.append(Doc+master+college+Acollege+high+sec+ele)
    print()
    
def printage(age15,age19,age19to24,age29,age34,age39,age44,age49,age50):
    print('����15��:', age15, '�H')
    print("15��19��:", age19, '�H')
    print("20��24��:", age19to24, '�H')
    print("25��29��:", age29, '�H')
    print("30��34��:", age34, '�H')
    print("35��39��:", age39, '�H')
    print("40��44��:", age44, '�H')
    print("45��49��:", age49, '�H')
    print("50���H�W:", age50, '�H')
    Age15.append(age15)
    Age19.append(age19)
    Age24.append(age19to24)
    Age29.append(age29)
    Age34.append(age34)
    Age39.append(age39)
    Age44.append(age44)
    Age49.append(age49)
    Age50.append(age50)
    locAge.append(age15+age19+age19to24+age29+age34+age39+age44+age49+age50)

for i in range(2,len(result)):
    if result[i][6] == '�դh���~' and int(result[i][7]) > 0:
        Doc += int(result[i][7])
    elif result[i][6] == '�Ӥh���~' and int(result[i][7]) > 0:
        master += int(result[i][7])
    elif result[i][6] == '�j�ǲ��~' and int(result[i][7]) > 0:
        college += int(result[i][7])
    elif result[i][6] == '�M�첦�~' and int(result[i][7]) > 0:
        Acollege += int(result[i][7])
    elif result[i][6] == '�������~' and int(result[i][7]) > 0:
        high += int(result[i][7])
    elif result[i][6] == '�ꤤ���~' and int(result[i][7]) > 0:
        sec += int(result[i][7])
    elif result[i][6] == '��p���~�H�U' and int(result[i][7]) > 0:
        ele += int(result[i][7])

    if result[i][5] == '����15��' and int(result[i][7]) > 0:
        age15 += int(result[i][7])
    elif result[i][5] == '15��19��' and int(result[i][7]) > 0:
        age19 += int(result[i][7])
    elif result[i][5] == '20��24��' and int(result[i][7]) > 0:
        age19to24 += int(result[i][7])
    elif result[i][5] == '25��29��' and int(result[i][7]) > 0:
        age29 += int(result[i][7])
    elif result[i][5] == '30��34��' and int(result[i][7]) > 0:
        age34 += int(result[i][7])
    elif result[i][5] == '35��39��' and int(result[i][7]) > 0:
        age39 += int(result[i][7])
    elif result[i][5] == '40��44��' and int(result[i][7]) > 0:
        age44 += int(result[i][7])
    elif result[i][5] == '45��49��' and int(result[i][7]) > 0:
        age49 += int(result[i][7])
    elif result[i][5] == '50���H�W' and int(result[i][7]) > 0:
        age50 += int(result[i][7])
    if i!=len(result)-1:
        if result[i][2][0:2] != result[i+1][2][0:2]:
            k = k + 1
            printresult(k, Doc, master, college, Acollege, high, sec, ele)
            printage(age15, age19, age19to24, age29, age34, age39, age44, age49, age50)
            print('\n')
            Doc = 0
            master = 0
            college = 0
            Acollege = 0
            high = 0
            sec = 0
            ele = 0
            age15 = 0
            age19 = 0
            age19to24 = 0
            age29 = 0
            age34 = 0
            age39 = 0
            age44 = 0
            age49 = 0
            age50 = 0
    else:
        k = k + 1
        printresult(k, Doc, master, college, Acollege, high, sec, ele)
        printage(age15, age19, age19to24, age29, age34, age39, age44, age49, age50)
        print('\n\n')

#%% �~�ּh��������
myfont = FontProperties(fname='C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf')
X = [12,17,22,27,32,37,42,47,52]
Y = [sum(Age15),sum(Age19),sum(Age24),sum(Age29),sum(Age34),sum(Age39),sum(Age44),sum(Age49),sum(Age50)]
G = ["<15","15~19","20~24","25~29","30~34","35~39","40~44","45~49",">=50"]

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="lightblue",tick_label=G)
plt.xlabel("�~�ּh",fontproperties = myfont,size=12)
plt.ylabel("�H��",fontproperties = myfont,size=12)
plt.title("108�~�s�ͨ���˦~�ּh���G",fontproperties = myfont,size=15)
plt.savefig('1.jpg', dpi=300)
#%% �~�ּh������
Y = [sum([sum(Age15),sum(Age19),sum(Age49),sum(Age50)]),sum(Age24),sum(Age29),sum(Age34),sum(Age39),sum(Age44)]
G = ["<20 and >=45","20~24","25~29","30~34","35~39","40~44"]
color=["#CCEEFF","#77DDFF","#33CCFF","#0088A8","#009FCC","#00BBFF"]

plt.pie(Y,labels=G,colors=color,explode=(0.1,0,0,0,0,0),autopct="%1.1f%%")
plt.title("108�~�s�ͨ���˦~�ּh���G��ҹ�",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('2.jpg', dpi=300)

#%% �Ǿ���������
#plt.rcParams['font.sans-serif'] = 'C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf'
X = [10,20,30,40,50,60,70]
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's","Bachelor's","Associate","high","middle","elementary"]

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=5,color="pink",tick_label=G) #orientation = horizontal
plt.xlabel("�Ǿ�",fontproperties = myfont,size=12)
plt.ylabel("�H��",fontproperties = myfont,size=12)
plt.title("108�~�s�ͨ���˾Ǿ����G",fontproperties = myfont,size=15)
plt.savefig('3.jpg', dpi=300)

#%% �Ǿ�������
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's degree","Bachelor's degree","Associate degree","senior high school","middle school","elementary\nschool"]
color=["#C63300","#FFA488","#FF8888","#FF7744","#FF5511","#E63F00","#FFCCCC"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108�~�s�ͨ���˾Ǿ���ҹ�",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('4.jpg', dpi=300)

#%% �X�ͫ��� Top 7������
Dict={}
Y=[]
G=[]
for i in range(len(j)):
    Dict["{0}".format(cityName[i])] = loc[i]
y = sorted(Dict.items(), key=lambda x:x[1],reverse=True)
for i in range(7):
    Y.append(y[i][1])
    G.append(y[i][0])
G = ['New Taipei','Taoyuan', 'Taichung', 'Taipei', 'Kaohsiung','Changhua', 'Tainan'] #��ܤ��F����QQ

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="#CCBBFF",tick_label=G) #orientation = horizontal tick_label=j
plt.xlabel("����",fontproperties = myfont,size=13)
plt.ylabel("�H��",fontproperties = myfont,size=13)
plt.title("108�~�s�ͨ�X�ͫ��� Top 7",fontproperties = myfont,size=15)
plt.savefig('5.jpg', dpi=300)

#%% �_���n�F���q ����
N = loc[0]+loc[1]+loc[2]+loc[6]+loc[7]+loc[17]+loc[18]
W = loc[3]+loc[8]+loc[9]+loc[10]
S = loc[4]+loc[5]+loc[11]+loc[12]+loc[13]+loc[19]
E = loc[14]+loc[15]
O = loc[16]+loc[20]+loc[21]
Y = [N,W,S,E,O]
G = ["North","West","South","East","offshore islands"]
color=["#FFEE99","#FFDD55","#FFCC22","#EEEE00","#DDAA00"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108�~�U�a�Ϸs�ͨ���",fontproperties = myfont,size=13,loc="right")
plt.axis("equal")
plt.savefig('6.jpg', dpi=300)
#%% �x�W�U�����a��
county_shp = gpd.read_file(r'D:\NCKU\108-2\Coding-X_Python\map2\COUNTY_MOI_1081121.shp')
#county_shp.plot(cmap='RdBu')

num = [145,3053,12249,3135,4194,4706,2062,3871,20986,27965,21209,11711,22493,3050,4422,1676,2937,1194,14317,1467,2411,988]
county_shp['number'] = np.array(num)
county_shp = county_shp.drop([18],axis=0) #�Ⱚ���R��
county_shp["center"] = county_shp["geometry"].centroid
TW_points = county_shp.copy()
TW_points.set_geometry("center", inplace=True)
texts = []
ax = county_shp.plot(cmap="gray_r",column='number',legend=True,  scheme='quantiles')
plt.legend(loc='best')
plt.axis("off")

for x, y, label in zip(TW_points.geometry.x, TW_points.geometry.y, TW_points.COUNTYENG):
    texts.append(plt.text(x, y, label, fontsize=5))
 
aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(2, 2), expand_text=(1, 1),
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))
plt.savefig('map.jpg', dpi=300)

