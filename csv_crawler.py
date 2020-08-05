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
<<<<<<< HEAD
cityName = ['·s¥_¥« New Taipei', '»O¥_¥« Taipei', '®ç¶é¥« Taoyuan', '»O¤¤¥« Taichung', '»O«n¥« Tainan', '°ª¶¯¥« Kaohsiung', '©yÄõ¿¤ Yilan',
     '·s¦Ë¿¤ Hsinchu', '­]®ß¿¤ Miaoli', '¹ü¤Æ¿¤ Changhua', '«n§ë¿¤ Nantou', '¶³ªL¿¤ Yunlin', '¹Å¸q¿¤ Chiayi', '«ÌªF¿¤ Pingtung', '»OªF¿¤ Taitung',
     'ªá½¬¿¤ Hualien', '¼ê´ò¿¤ Penghu', '°ò¶©¥« Keelung','·s¦Ë¥« Hsinchu','¹Å¸q¥« Chiayi', 'ª÷ªù¿¤ Kinmen', '³s¦¿¿¤ Lianjiang']
Doctor = 0
  master = 0
college = 0
=======
j = ['æ–°åŒ—å¸‚ New Taipei', 'è‡ºåŒ—å¸‚ Taipei', 'æ¡ƒåœ’å¸‚ Taoyuan', 'è‡ºä¸­å¸‚ Taichung', 'è‡ºå—å¸‚ Tainan', 'é«˜é›„å¸‚ Kaohsiung', 'å®œè˜­ç¸£ Yilan',
     'æ–°ç«¹ç¸£ Hsinchu', 'è‹—æ —ç¸£ Miaoli', 'å½°åŒ–ç¸£ Changhua', 'å—æŠ•ç¸£ Nantou', 'é›²æž—ç¸£ Yunlin', 'å˜‰ç¾©ç¸£ Chiayi', 'å±æ±ç¸£ Pingtung', 'è‡ºæ±ç¸£ Taitung',
     'èŠ±è“®ç¸£ Hualien', 'æ¾Žæ¹–ç¸£ Penghu', 'åŸºéš†å¸‚ Keelung','æ–°ç«¹å¸‚ Hsinchu','å˜‰ç¾©å¸‚ Chiayi', 'é‡‘é–€ç¸£ Kinmen', 'é€£æ±Ÿç¸£ Lianjiang']
Doc = 0
Master = 0
University = 0
>>>>>>> origin/lenny0805
Acollege = 0
high = 0
Juniorhigh = 0
Elementary = 0
k = -1
x = -1
age15 = 0
age19 = 0
<<<<<<< HEAD
age19to24 = 0
age29 = 0
age34 = 0
=======
age24 = 0
age25to29 = 0
age30to34 = 0
>>>>>>> origin/lenny0805
age39 = 0
age44 = 0
age45to49 = 0
age50up = 0
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

<<<<<<< HEAD
<<<<<<< HEAD
def printresult(k, Doc, master, college, Acollege, high, sec, ele):
    print(ciytName[k],'\n')
    print('³Õ¤h²¦·~:', Doc, '¤H')
    print('ºÓ¤h²¦·~:', master, '¤H')
    print('¤j¾Ç²¦·~:', college, '¤H')
    print('±M¬ì²¦·~:', Acollege, '¤H')
    print('°ª¤¤²¦·~:', high, '¤H')
    print('°ê¤¤²¦·~:', sec, '¤H')
    print('°ê¤p¥H¤U²¦·~:', ele, '¤H')
=======
def printresult(k, Doc, master, college, Acollege, high, Juniorhigh, Elementary):
=======
def printresult(k, Doc, Master, University, Acollege, high, sec, ele):
>>>>>>> origin/lenny0805
    print(j[k],'\n')
    print('åšå£«ç•¢æ¥­:', Doc, 'äºº')
    print('ç¢©å£«ç•¢æ¥­:', Master, 'äºº')
    print('å¤§å­¸ç•¢æ¥­:', University, 'äºº')
    print('å°ˆç§‘ç•¢æ¥­:', Acollege, 'äºº')
    print('é«˜ä¸­ç•¢æ¥­:', high, 'äºº')
    print('åœ‹ä¸­ç•¢æ¥­:', Juniorhigh, 'äºº')
    print('åœ‹å°ä»¥ä¸‹ç•¢æ¥­:', Elementary, 'äºº')
>>>>>>> origin/Leo_0805
    DOC.append(Doc)
    MASTER.append(Master)
    COLLEGE.append(University)
    ACOLLEGE.append(Acollege)
    HIGH.append(high)
<<<<<<< HEAD
    SEC.append(Juniorhigh)
    ELE.append(Elementary)
    loc.append(Doc + master + college + Acollege + high + Juniorhigh + Elementary)
    print()
    
<<<<<<< HEAD
def printage(age15,age19,age19to24,age29,age34,age39,age44,age49,age50):
    print('¥¼º¡15·³:', age15, '¤H')
    print("15¡ã19·³:", age19, '¤H')
    print("20¡ã24·³:", age19to24, '¤H')
    print("25¡ã29·³:", age29, '¤H')
    print("30¡ã34·³:", age34, '¤H')
    print("35¡ã39·³:", age39, '¤H')
    print("40¡ã44·³:", age44, '¤H')
    print("45¡ã49·³:", age49, '¤H')
    print("50·³¥H¤W:", age50, '¤H')
=======
def printage(age15, age19, age24, age29, age34, age39, age44, age45to49, age50up):
=======
    SEC.append(sec)
    ELE.append(ele)
    loc.append(Doc+Master+University+Acollege+high+sec+ele)
    print()
    
def printage(age15, age19, age24, age25to29, age30to34, age39, age44, age49, age50):
>>>>>>> origin/lenny0805
    print('æœªæ»¿15æ­²:', age15, 'äºº')
    print("15ï½ž19æ­²:", age19, 'äºº')
    print("20ï½ž24æ­²:", age24, 'äºº')
    print("25ï½ž29æ­²:", age25to29, 'äºº')
    print("30ï½ž34æ­²:", age30to34, 'äºº')
    print("35ï½ž39æ­²:", age39, 'äºº')
    print("40ï½ž44æ­²:", age44, 'äºº')
    print("45ï½ž49æ­²:", age45to49, 'äºº')
    print("50æ­²ä»¥ä¸Š:", age50up, 'äºº')
>>>>>>> origin/Leo_0805
    Age15.append(age15)
    Age19.append(age19)
<<<<<<< HEAD
    Age24.append(age19to24)
    Age29.append(age29)
    Age34.append(age34)
=======
    Age24.append(age24)
    Age29.append(age25to29)
    Age34.append(age30to34)
>>>>>>> origin/lenny0805
    Age39.append(age39)
    Age44.append(age44)
<<<<<<< HEAD
    Age49.append(age49)
    Age50.append(age50)
<<<<<<< HEAD
    locAge.append(age15+age19+age19to24+age29+age34+age39+age44+age49+age50)
=======
    Age49.append(age45to49)
    Age50.append(age50up)
    locAge.append(age15 + age19 + age24 + age29 + age34 + age39 + age44 + age45to49 + age50up)
>>>>>>> origin/Leo_0805
=======
    locAge.append(age15+age19+age24+age25to29+age30to34+age39+age44+age49+age50)
>>>>>>> origin/lenny0805

for i in range(2,len(result)):
    if result[i][6] == '³Õ¤h²¦·~' and int(result[i][7]) > 0:
        Doc += int(result[i][7])
<<<<<<< HEAD
    elif result[i][6] == 'ºÓ¤h²¦·~' and int(result[i][7]) > 0:
        master += int(result[i][7])
    elif result[i][6] == '¤j¾Ç²¦·~' and int(result[i][7]) > 0:
        college += int(result[i][7])
    elif result[i][6] == '±M¬ì²¦·~' and int(result[i][7]) > 0:
=======
    elif result[i][6] == 'ç¢©å£«ç•¢æ¥­' and int(result[i][7]) > 0:
        Master += int(result[i][7])
    elif result[i][6] == 'å¤§å­¸ç•¢æ¥­' and int(result[i][7]) > 0:
        University += int(result[i][7])
    elif result[i][6] == 'å°ˆç§‘ç•¢æ¥­' and int(result[i][7]) > 0:
>>>>>>> origin/lenny0805
        Acollege += int(result[i][7])
    elif result[i][6] == '°ª¤¤²¦·~' and int(result[i][7]) > 0:
        high += int(result[i][7])
<<<<<<< HEAD
    elif result[i][6] == '°ê¤¤²¦·~' and int(result[i][7]) > 0:
        sec += int(result[i][7])
    elif result[i][6] == '°ê¤p²¦·~¥H¤U' and int(result[i][7]) > 0:
        ele += int(result[i][7])
=======
    elif result[i][6] == 'åœ‹ä¸­ç•¢æ¥­' and int(result[i][7]) > 0:
        Juniorhigh += int(result[i][7])
    elif result[i][6] == 'åœ‹å°ç•¢æ¥­ä»¥ä¸‹' and int(result[i][7]) > 0:
        Elementary += int(result[i][7])
>>>>>>> origin/Leo_0805

    if result[i][5] == '¥¼º¡15·³' and int(result[i][7]) > 0:
        age15 += int(result[i][7])
    elif result[i][5] == '15¡ã19·³' and int(result[i][7]) > 0:
        age19 += int(result[i][7])
<<<<<<< HEAD
    elif result[i][5] == '20¡ã24·³' and int(result[i][7]) > 0:
        age19to24 += int(result[i][7])
    elif result[i][5] == '25¡ã29·³' and int(result[i][7]) > 0:
        age29 += int(result[i][7])
    elif result[i][5] == '30¡ã34·³' and int(result[i][7]) > 0:
        age34 += int(result[i][7])
    elif result[i][5] == '35¡ã39·³' and int(result[i][7]) > 0:
=======
    elif result[i][5] == '20ï½ž24æ­²' and int(result[i][7]) > 0:
        age24 += int(result[i][7])
    elif result[i][5] == '25ï½ž29æ­²' and int(result[i][7]) > 0:
        age25to29 += int(result[i][7])
    elif result[i][5] == '30ï½ž34æ­²' and int(result[i][7]) > 0:
        age30to34 += int(result[i][7])
    elif result[i][5] == '35ï½ž39æ­²' and int(result[i][7]) > 0:
>>>>>>> origin/lenny0805
        age39 += int(result[i][7])
    elif result[i][5] == '40¡ã44·³' and int(result[i][7]) > 0:
        age44 += int(result[i][7])
<<<<<<< HEAD
    elif result[i][5] == '45¡ã49·³' and int(result[i][7]) > 0:
        age49 += int(result[i][7])
    elif result[i][5] == '50·³¥H¤W' and int(result[i][7]) > 0:
        age50 += int(result[i][7])
    if i!=len(result)-1:
        if result[i][2][0:2] != result[i+1][2][0:2]:
            k = k + 1
<<<<<<< HEAD
            printresult(k, Doc, master, college, Acollege, high, sec, ele)
            printage(age15, age19, age19to24, age29, age34, age39, age44, age49, age50)
=======
    elif result[i][5] == '45ï½ž49æ­²' and int(result[i][7]) > 0:
        age45to49 += int(result[i][7])
    elif result[i][5] == '50æ­²ä»¥ä¸Š' and int(result[i][7]) > 0:
        age50up += int(result[i][7])
    if i!=len(result)-1:
        if result[i][2][0:2] != result[i+1][2][0:2]:
            k = k + 1
            printresult(k, Doc, master, college, Acollege, high, Juniorhigh, Elementary)
            printage(age15, age19, age24, age29, age34, age39, age44, age45to49, age50up)
>>>>>>> origin/Leo_0805
=======
            printresult(k, Doc, Master, University, Acollege, high, sec, ele)
            printage(age15, age19, age24, age25to29, age30to34, age39, age44, age49, age50)
>>>>>>> origin/lenny0805
            print('\n')
            Doc = 0
            Master = 0
            University = 0
            Acollege = 0
            high = 0
            Juniorhigh = 0
            Elementary = 0
            age15 = 0
            age19 = 0
<<<<<<< HEAD
            age19to24 = 0
            age29 = 0
            age34 = 0
=======
            age24 = 0
            age25to29 = 0
            age30to34 = 0
>>>>>>> origin/lenny0805
            age39 = 0
            age44 = 0
            age45to49 = 0
            age50up = 0
    else:
        k = k + 1
<<<<<<< HEAD
<<<<<<< HEAD
        printresult(k, Doc, master, college, Acollege, high, sec, ele)
        printage(age15, age19, age19to24, age29, age34, age39, age44, age49, age50)
=======
        printresult(k, Doc, master, college, Acollege, high, Juniorhigh, Elementary)
        printage(age15, age19, age24, age29, age34, age39, age44, age45to49, age50up)
>>>>>>> origin/Leo_0805
=======
        printresult(k, Doc, Master, University, Acollege, high, sec, ele)
        printage(age15, age19, age24, age25to29, age30to34, age39, age44, age49, age50)
>>>>>>> origin/lenny0805
        print('\n\n')

#%% ¦~ÄÖ¼hªºªø±ø¹Ï
myfont = FontProperties(fname='C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf')
X = [12,17,22,27,32,37,42,47,52]
Y = [sum(Age15),sum(Age19),sum(Age24),sum(Age29),sum(Age34),sum(Age39),sum(Age44),sum(Age49),sum(Age50)]
G = ["<15","15~19","20~24","25~29","30~34","35~39","40~44","45~49",">=50"]

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="lightblue",tick_label=G)
plt.xlabel("¦~ÄÖ¼h",fontproperties = myfont,size=12)
plt.ylabel("¤H¼Æ",fontproperties = myfont,size=12)
plt.title("108¦~·s¥Í¨à¥À¿Ë¦~ÄÖ¼h¤À§G",fontproperties = myfont,size=15)
plt.savefig('1.jpg', dpi=300)
#%% ¦~ÄÖ¼hªº¶ê»æ¹Ï
Y = [sum([sum(Age15),sum(Age19),sum(Age49),sum(Age50)]),sum(Age24),sum(Age29),sum(Age34),sum(Age39),sum(Age44)]
G = ["<20 and >=45","20~24","25~29","30~34","35~39","40~44"]
color=["#CCEEFF","#77DDFF","#33CCFF","#0088A8","#009FCC","#00BBFF"]

plt.pie(Y,labels=G,colors=color,explode=(0.1,0,0,0,0,0),autopct="%1.1f%%")
plt.title("108¦~·s¥Í¨à¥À¿Ë¦~ÄÖ¼h¤À§G¤ñ¨Ò¹Ï",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('2.jpg', dpi=300)

#%% ¾Ç¾úªºªø±ø¹Ï
#plt.rcParams['font.sans-serif'] = 'C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf'
X = [10,20,30,40,50,60,70]
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's","Bachelor's","Associate","high","middle","elementary"]

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=5,color="pink",tick_label=G) #orientation = horizontal
plt.xlabel("¾Ç¾ú",fontproperties = myfont,size=12)
plt.ylabel("¤H¼Æ",fontproperties = myfont,size=12)
plt.title("108¦~·s¥Í¨à¥À¿Ë¾Ç¾ú¤À§G",fontproperties = myfont,size=15)
plt.savefig('3.jpg', dpi=300)

#%% ¾Ç¾úªº¶ê»æ¹Ï
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's degree","Bachelor's degree","Associate degree","senior high school","middle school","elementary\nschool"]
color=["#C63300","#FFA488","#FF8888","#FF7744","#FF5511","#E63F00","#FFCCCC"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108¦~·s¥Í¨à¥À¿Ë¾Ç¾ú¤ñ¨Ò¹Ï",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('4.jpg', dpi=300)

#%% ¥X¥Í«°¥« Top 7ªø±ø¹Ï
Dict={}
Y=[]
G=[]
for i in range(len(j)):
    Dict["{0}".format(cityName[i])] = loc[i]
y = sorted(Dict.items(), key=lambda x:x[1],reverse=True)
for i in range(7):
    Y.append(y[i][1])
    G.append(y[i][0])
G = ['New Taipei','Taoyuan', 'Taichung', 'Taipei', 'Kaohsiung','Changhua', 'Tainan'] #Åã¥Ü¤£¤F¤¤¤åQQ

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="#CCBBFF",tick_label=G) #orientation = horizontal tick_label=j
plt.xlabel("«°¥«",fontproperties = myfont,size=13)
plt.ylabel("¤H¼Æ",fontproperties = myfont,size=13)
plt.title("108¦~·s¥Í¨à¥X¥Í«°¥« Top 7",fontproperties = myfont,size=15)
plt.savefig('5.jpg', dpi=300)

#%% ¥_¤¤«nªFÂ÷®q ¶ê»æ¹Ï
N = loc[0]+loc[1]+loc[2]+loc[6]+loc[7]+loc[17]+loc[18]
W = loc[3]+loc[8]+loc[9]+loc[10]
S = loc[4]+loc[5]+loc[11]+loc[12]+loc[13]+loc[19]
E = loc[14]+loc[15]
O = loc[16]+loc[20]+loc[21]
Y = [N,W,S,E,O]
G = ["North","West","South","East","offshore islands"]
color=["#FFEE99","#FFDD55","#FFCC22","#EEEE00","#DDAA00"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108¦~¦U¦a°Ï·s¥Í¨à¤ñ¨Ò",fontproperties = myfont,size=13,loc="right")
plt.axis("equal")
plt.savefig('6.jpg', dpi=300)
#%% ¥xÆW¦U¿¤¥«¦a¹Ï
county_shp = gpd.read_file(r'D:\NCKU\108-2\Coding-X_Python\map2\COUNTY_MOI_1081121.shp')
#county_shp.plot(cmap='RdBu')

num = [145,3053,12249,3135,4194,4706,2062,3871,20986,27965,21209,11711,22493,3050,4422,1676,2937,1194,14317,1467,2411,988]
county_shp['number'] = np.array(num)
county_shp = county_shp.drop([18],axis=0) #§â°ª¶¯§R±¼
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

