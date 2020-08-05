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
cityName = ['∑s•_•´ New Taipei', 'ªO•_•´ Taipei', 'ÆÁ∂È•´ Taoyuan', 'ªO§§•´ Taichung', 'ªO´n•´ Tainan', '∞™∂Ø•´ Kaohsiung', '©yƒıø§ Yilan',
     '∑s¶Àø§ Hsinchu', '≠]Æﬂø§ Miaoli', 'π¸§∆ø§ Changhua', '´nßÎø§ Nantou', '∂≥™Lø§ Yunlin', 'π≈∏qø§ Chiayi', '´Ã™Fø§ Pingtung', 'ªO™Fø§ Taitung',
     '™·Ω¨ø§ Hualien', 'ºÍ¥Úø§ Penghu', '∞Ú∂©•´ Keelung','∑s¶À•´ Hsinchu','π≈∏q•´ Chiayi', '™˜™˘ø§ Kinmen', '≥s¶øø§ Lianjiang']
Doctor = 0
  master = 0
college = 0
=======
j = ['Êñ∞ÂåóÂ∏Ç New Taipei', 'Ëá∫ÂåóÂ∏Ç Taipei', 'Ê°ÉÂúíÂ∏Ç Taoyuan', 'Ëá∫‰∏≠Â∏Ç Taichung', 'Ëá∫ÂçóÂ∏Ç Tainan', 'È´òÈõÑÂ∏Ç Kaohsiung', 'ÂÆúËò≠Á∏£ Yilan',
     'Êñ∞Á´πÁ∏£ Hsinchu', 'ËãóÊ†óÁ∏£ Miaoli', 'ÂΩ∞ÂåñÁ∏£ Changhua', 'ÂçóÊäïÁ∏£ Nantou', 'Èõ≤ÊûóÁ∏£ Yunlin', 'ÂòâÁæ©Á∏£ Chiayi', 'Â±èÊù±Á∏£ Pingtung',
     'Ëá∫Êù±Á∏£ Taitung',
     'Ëä±ËìÆÁ∏£ Hualien', 'ÊæéÊπñÁ∏£ Penghu', 'Âü∫ÈöÜÂ∏Ç Keelung', 'Êñ∞Á´πÂ∏Ç Hsinchu', 'ÂòâÁæ©Â∏Ç Chiayi', 'ÈáëÈñÄÁ∏£ Kinmen', 'ÈÄ£Ê±üÁ∏£ Lianjiang']
Doc = 0
<<<<<<< HEAD
Master = 0
University = 0
>>>>>>> origin/lenny0805
Acollege = 0
high = 0
Juniorhigh = 0
Elementary = 0
k = -1
=======
master = 0
college = 0
Acollege = 0
high = 0
sec = 0
ele = 0
City_order = -1
>>>>>>> Chi_0805
x = -1
under_age15 = 0
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
DOC = []
MASTER = []
COLLEGE = []
ACOLLEGE = []
HIGH = []
SEC = []
ELE = []
under_Age15 = []
Age19 = []
Age24 = []
Age29 = []
Age34 = []
Age39 = []
Age44 = []
Age49 = []
Age50 = []
loc = []
locAge = []


##

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def printresult(k, Doc, master, college, Acollege, high, sec, ele):
    print(ciytName[k],'\n')
    print('≥’§h≤¶∑~:', Doc, '§H')
    print('∫”§h≤¶∑~:', master, '§H')
    print('§jæ«≤¶∑~:', college, '§H')
    print('±M¨Ï≤¶∑~:', Acollege, '§H')
    print('∞™§§≤¶∑~:', high, '§H')
    print('∞Í§§≤¶∑~:', sec, '§H')
    print('∞Í§p•H§U≤¶∑~:', ele, '§H')
=======
def printresult(k, Doc, master, college, Acollege, high, Juniorhigh, Elementary):
=======
def printresult(k, Doc, Master, University, Acollege, high, sec, ele):
>>>>>>> origin/lenny0805
    print(j[k],'\n')
=======
def Printeducation(City_order, Doc, master, college, Acollege, high, sec, ele):
    print(j[City_order], '\n')
>>>>>>> Chi_0805
    print('ÂçöÂ£´Áï¢Ê•≠:', Doc, '‰∫∫')
    print('Á¢©Â£´Áï¢Ê•≠:', Master, '‰∫∫')
    print('Â§ßÂ≠∏Áï¢Ê•≠:', University, '‰∫∫')
    print('Â∞àÁßëÁï¢Ê•≠:', Acollege, '‰∫∫')
    print('È´ò‰∏≠Áï¢Ê•≠:', high, '‰∫∫')
    print('Âúã‰∏≠Áï¢Ê•≠:', Juniorhigh, '‰∫∫')
    print('ÂúãÂ∞è‰ª•‰∏ãÁï¢Ê•≠:', Elementary, '‰∫∫')
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
    print('•º∫°15∑≥:', age15, '§H')
    print("15°„19∑≥:", age19, '§H')
    print("20°„24∑≥:", age19to24, '§H')
    print("25°„29∑≥:", age29, '§H')
    print("30°„34∑≥:", age34, '§H')
    print("35°„39∑≥:", age39, '§H')
    print("40°„44∑≥:", age44, '§H')
    print("45°„49∑≥:", age49, '§H')
    print("50∑≥•H§W:", age50, '§H')
=======
def printage(age15, age19, age24, age29, age34, age39, age44, age45to49, age50up):
=======
    SEC.append(sec)
    ELE.append(ele)
<<<<<<< HEAD
    loc.append(Doc+Master+University+Acollege+high+sec+ele)
    print()
    
def printage(age15, age19, age24, age25to29, age30to34, age39, age44, age49, age50):
>>>>>>> origin/lenny0805
    print('Êú™Êªø15Ê≠≤:', age15, '‰∫∫')
=======
    loc.append(Doc + master + college + Acollege + high + sec + ele)
    print()


def Printage(under_age15, age19, age24, age29, age34, age39, age44, age49, age50):
    print('Êú™Êªø15Ê≠≤:', under_age15, '‰∫∫')
>>>>>>> Chi_0805
    print("15ÔΩû19Ê≠≤:", age19, '‰∫∫')
    print("20ÔΩû24Ê≠≤:", age24, '‰∫∫')
    print("25ÔΩû29Ê≠≤:", age25to29, '‰∫∫')
    print("30ÔΩû34Ê≠≤:", age30to34, '‰∫∫')
    print("35ÔΩû39Ê≠≤:", age39, '‰∫∫')
    print("40ÔΩû44Ê≠≤:", age44, '‰∫∫')
<<<<<<< HEAD
    print("45ÔΩû49Ê≠≤:", age45to49, '‰∫∫')
    print("50Ê≠≤‰ª•‰∏ä:", age50up, '‰∫∫')
>>>>>>> origin/Leo_0805
    Age15.append(age15)
=======
    print("45ÔΩû49Ê≠≤:", age49, '‰∫∫')
    print("50Ê≠≤‰ª•‰∏ä:", age50, '‰∫∫')
    under_Age15.append(under_age15)
>>>>>>> Chi_0805
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
    if result[i][6] == '≥’§h≤¶∑~' and int(result[i][7]) > 0:
=======
    locAge.append(under_age15 + age19 + age24 + age29 + age34 + age39 + age44 + age49 + age50)


for i in range(2, len(result)):
    if result[i][6] == 'ÂçöÂ£´Áï¢Ê•≠' and int(result[i][7]) > 0:
>>>>>>> Chi_0805
        Doc += int(result[i][7])
<<<<<<< HEAD
    elif result[i][6] == '∫”§h≤¶∑~' and int(result[i][7]) > 0:
        master += int(result[i][7])
    elif result[i][6] == '§jæ«≤¶∑~' and int(result[i][7]) > 0:
        college += int(result[i][7])
    elif result[i][6] == '±M¨Ï≤¶∑~' and int(result[i][7]) > 0:
=======
    elif result[i][6] == 'Á¢©Â£´Áï¢Ê•≠' and int(result[i][7]) > 0:
        Master += int(result[i][7])
    elif result[i][6] == 'Â§ßÂ≠∏Áï¢Ê•≠' and int(result[i][7]) > 0:
        University += int(result[i][7])
    elif result[i][6] == 'Â∞àÁßëÁï¢Ê•≠' and int(result[i][7]) > 0:
>>>>>>> origin/lenny0805
        Acollege += int(result[i][7])
    elif result[i][6] == '∞™§§≤¶∑~' and int(result[i][7]) > 0:
        high += int(result[i][7])
<<<<<<< HEAD
    elif result[i][6] == '∞Í§§≤¶∑~' and int(result[i][7]) > 0:
        sec += int(result[i][7])
    elif result[i][6] == '∞Í§p≤¶∑~•H§U' and int(result[i][7]) > 0:
        ele += int(result[i][7])
=======
    elif result[i][6] == 'Âúã‰∏≠Áï¢Ê•≠' and int(result[i][7]) > 0:
        Juniorhigh += int(result[i][7])
    elif result[i][6] == 'ÂúãÂ∞èÁï¢Ê•≠‰ª•‰∏ã' and int(result[i][7]) > 0:
        Elementary += int(result[i][7])
>>>>>>> origin/Leo_0805

<<<<<<< HEAD
    if result[i][5] == '•º∫°15∑≥' and int(result[i][7]) > 0:
        age15 += int(result[i][7])
    elif result[i][5] == '15°„19∑≥' and int(result[i][7]) > 0:
=======
    if result[i][5] == 'Êú™Êªø15Ê≠≤' and int(result[i][7]) > 0:
        under_age15 += int(result[i][7])
    elif result[i][5] == '15ÔΩû19Ê≠≤' and int(result[i][7]) > 0:
>>>>>>> Chi_0805
        age19 += int(result[i][7])
<<<<<<< HEAD
    elif result[i][5] == '20°„24∑≥' and int(result[i][7]) > 0:
        age19to24 += int(result[i][7])
    elif result[i][5] == '25°„29∑≥' and int(result[i][7]) > 0:
        age29 += int(result[i][7])
    elif result[i][5] == '30°„34∑≥' and int(result[i][7]) > 0:
        age34 += int(result[i][7])
    elif result[i][5] == '35°„39∑≥' and int(result[i][7]) > 0:
=======
    elif result[i][5] == '20ÔΩû24Ê≠≤' and int(result[i][7]) > 0:
        age24 += int(result[i][7])
    elif result[i][5] == '25ÔΩû29Ê≠≤' and int(result[i][7]) > 0:
        age25to29 += int(result[i][7])
    elif result[i][5] == '30ÔΩû34Ê≠≤' and int(result[i][7]) > 0:
        age30to34 += int(result[i][7])
    elif result[i][5] == '35ÔΩû39Ê≠≤' and int(result[i][7]) > 0:
>>>>>>> origin/lenny0805
        age39 += int(result[i][7])
    elif result[i][5] == '40°„44∑≥' and int(result[i][7]) > 0:
        age44 += int(result[i][7])
<<<<<<< HEAD
    elif result[i][5] == '45°„49∑≥' and int(result[i][7]) > 0:
        age49 += int(result[i][7])
    elif result[i][5] == '50∑≥•H§W' and int(result[i][7]) > 0:
        age50 += int(result[i][7])
<<<<<<< HEAD
    if i!=len(result)-1:
        if result[i][2][0:2] != result[i+1][2][0:2]:
            k = k + 1
<<<<<<< HEAD
            printresult(k, Doc, master, college, Acollege, high, sec, ele)
            printage(age15, age19, age19to24, age29, age34, age39, age44, age49, age50)
=======
    elif result[i][5] == '45ÔΩû49Ê≠≤' and int(result[i][7]) > 0:
        age45to49 += int(result[i][7])
    elif result[i][5] == '50Ê≠≤‰ª•‰∏ä' and int(result[i][7]) > 0:
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
=======
    if i != len(result) - 1:
        if result[i][2][0:2] != result[i + 1][2][0:2]:
            City_order = City_order + 1
            Printeducation(City_order, Doc, master, college, Acollege, high, sec, ele)
            Printage(under_age15, age19, age24, age29, age34, age39, age44, age49, age50)
>>>>>>> Chi_0805
            print('\n')
            Doc = 0
            Master = 0
            University = 0
            Acollege = 0
            high = 0
<<<<<<< HEAD
            Juniorhigh = 0
            Elementary = 0
            age15 = 0
=======
            sec = 0
            ele = 0
            under_age15 = 0
>>>>>>> Chi_0805
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
<<<<<<< HEAD
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

#%% ¶~ƒ÷ºh™∫™¯±¯πœ
=======
        City_order = City_order + 1
        printresult(City_order, Doc, master, college, Acollege, high, sec, ele)
        printage(under_age15, age19, age24, age29, age34, age39, age44, age49, age50)
        print('\n\n')

# %% Âπ¥ÈΩ°Â±§ÁöÑÈï∑Ê¢ùÂúñ
>>>>>>> Chi_0805
myfont = FontProperties(fname='C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf')
X = [12, 17, 22, 27, 32, 37, 42, 47, 52]
Y = [sum(under_Age15), sum(Age19), sum(Age24), sum(Age29), sum(Age34), sum(Age39), sum(Age44), sum(Age49), sum(Age50)]
G = ["<15", "15~19", "20~24", "25~29", "30~34", "35~39", "40~44", "45~49", ">=50"]

<<<<<<< HEAD
plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="lightblue",tick_label=G)
plt.xlabel("¶~ƒ÷ºh",fontproperties = myfont,size=12)
plt.ylabel("§Hº∆",fontproperties = myfont,size=12)
plt.title("108¶~∑s•Õ®‡•¿øÀ¶~ƒ÷ºh§¿ßG",fontproperties = myfont,size=15)
plt.savefig('1.jpg', dpi=300)
#%% ¶~ƒ÷ºh™∫∂ÍªÊπœ
Y = [sum([sum(Age15),sum(Age19),sum(Age49),sum(Age50)]),sum(Age24),sum(Age29),sum(Age34),sum(Age39),sum(Age44)]
G = ["<20 and >=45","20~24","25~29","30~34","35~39","40~44"]
color=["#CCEEFF","#77DDFF","#33CCFF","#0088A8","#009FCC","#00BBFF"]

plt.pie(Y,labels=G,colors=color,explode=(0.1,0,0,0,0,0),autopct="%1.1f%%")
plt.title("108¶~∑s•Õ®‡•¿øÀ¶~ƒ÷ºh§¿ßG§Ò®“πœ",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('2.jpg', dpi=300)

#%% æ«æ˙™∫™¯±¯πœ
#plt.rcParams['font.sans-serif'] = 'C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf'
X = [10,20,30,40,50,60,70]
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's","Bachelor's","Associate","high","middle","elementary"]

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=5,color="pink",tick_label=G) #orientation = horizontal
plt.xlabel("æ«æ˙",fontproperties = myfont,size=12)
plt.ylabel("§Hº∆",fontproperties = myfont,size=12)
plt.title("108¶~∑s•Õ®‡•¿øÀæ«æ˙§¿ßG",fontproperties = myfont,size=15)
plt.savefig('3.jpg', dpi=300)

#%% æ«æ˙™∫∂ÍªÊπœ
Y = [sum(DOC),sum(MASTER),sum(COLLEGE),sum(ACOLLEGE),sum(HIGH),sum(SEC),sum(ELE)]
G = ["PhD","master's degree","Bachelor's degree","Associate degree","senior high school","middle school","elementary\nschool"]
color=["#C63300","#FFA488","#FF8888","#FF7744","#FF5511","#E63F00","#FFCCCC"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108¶~∑s•Õ®‡•¿øÀæ«æ˙§Ò®“πœ",fontproperties = myfont,size=13)
plt.axis("equal")
plt.savefig('4.jpg', dpi=300)

#%% •X•Õ´∞•´ Top 7™¯±¯πœ
Dict={}
Y=[]
G=[]
for i in range(len(j)):
    Dict["{0}".format(cityName[i])] = loc[i]
y = sorted(Dict.items(), key=lambda x:x[1],reverse=True)
for i in range(7):
    Y.append(y[i][1])
    G.append(y[i][0])
G = ['New Taipei','Taoyuan', 'Taichung', 'Taipei', 'Kaohsiung','Changhua', 'Tainan'] #≈„•‹§£§F§§§ÂQQ

plt.figure(figsize=(8,4))
plt.bar(X,height=Y,width=4,color="#CCBBFF",tick_label=G) #orientation = horizontal tick_label=j
plt.xlabel("´∞•´",fontproperties = myfont,size=13)
plt.ylabel("§Hº∆",fontproperties = myfont,size=13)
plt.title("108¶~∑s•Õ®‡•X•Õ´∞•´ Top 7",fontproperties = myfont,size=15)
plt.savefig('5.jpg', dpi=300)

#%% •_§§´n™F¬˜Æq ∂ÍªÊπœ
N = loc[0]+loc[1]+loc[2]+loc[6]+loc[7]+loc[17]+loc[18]
W = loc[3]+loc[8]+loc[9]+loc[10]
S = loc[4]+loc[5]+loc[11]+loc[12]+loc[13]+loc[19]
E = loc[14]+loc[15]
O = loc[16]+loc[20]+loc[21]
Y = [N,W,S,E,O]
G = ["North","West","South","East","offshore islands"]
color=["#FFEE99","#FFDD55","#FFCC22","#EEEE00","#DDAA00"]

plt.pie(Y,labels=G,colors = color,explode=(0,0,0,0,0.3),autopct="%1.1f%%")
plt.title("108¶~¶U¶a∞œ∑s•Õ®‡§Ò®“",fontproperties = myfont,size=13,loc="right")
plt.axis("equal")
plt.savefig('6.jpg', dpi=300)
#%% •x∆W¶Uø§•´¶aπœ
=======
plt.figure(figsize=(8, 4))
plt.bar(X, height=Y, width=4, color="lightblue", tick_label=G)
plt.xlabel("Âπ¥ÈΩ°Â±§", fontproperties=myfont, size=12)
plt.ylabel("‰∫∫Êï∏", fontproperties=myfont, size=12)
plt.title("108Âπ¥Êñ∞ÁîüÂÖíÊØçË¶™Âπ¥ÈΩ°Â±§ÂàÜ‰Ωà", fontproperties=myfont, size=15)
plt.savefig('1.jpg', dpi=300)
# %% Âπ¥ÈΩ°Â±§ÁöÑÂúìÈ§ÖÂúñ
Y = [sum([sum(under_Age15), sum(Age19), sum(Age49), sum(Age50)]), sum(Age24), sum(Age29), sum(Age34), sum(Age39), sum(Age44)]
G = ["<20 and >=45", "20~24", "25~29", "30~34", "35~39", "40~44"]
color = ["#CCEEFF", "#77DDFF", "#33CCFF", "#0088A8", "#009FCC", "#00BBFF"]

plt.pie(Y, labels=G, colors=color, explode=(0.1, 0, 0, 0, 0, 0), autopct="%1.1f%%")
plt.title("108Âπ¥Êñ∞ÁîüÂÖíÊØçË¶™Âπ¥ÈΩ°Â±§ÂàÜ‰ΩàÊØî‰æãÂúñ", fontproperties=myfont, size=13)
plt.axis("equal")
plt.savefig('2.jpg', dpi=300)

# %% Â≠∏Ê≠∑ÁöÑÈï∑Ê¢ùÂúñ
# plt.rcParams['font.sans-serif'] = 'C:\\Users\\Peixin\\Downloads\\csv_crawler\\NotoSerifCJKtc-Light.otf'
X = [10, 20, 30, 40, 50, 60, 70]
Y = [sum(DOC), sum(MASTER), sum(COLLEGE), sum(ACOLLEGE), sum(HIGH), sum(SEC), sum(ELE)]
G = ["PhD", "master's", "Bachelor's", "Associate", "high", "middle", "elementary"]

plt.figure(figsize=(8, 4))
plt.bar(X, height=Y, width=5, color="pink", tick_label=G)  # orientation = horizontal
plt.xlabel("Â≠∏Ê≠∑", fontproperties=myfont, size=12)
plt.ylabel("‰∫∫Êï∏", fontproperties=myfont, size=12)
plt.title("108Âπ¥Êñ∞ÁîüÂÖíÊØçË¶™Â≠∏Ê≠∑ÂàÜ‰Ωà", fontproperties=myfont, size=15)
plt.savefig('3.jpg', dpi=300)

# %% Â≠∏Ê≠∑ÁöÑÂúìÈ§ÖÂúñ
Y = [sum(DOC), sum(MASTER), sum(COLLEGE), sum(ACOLLEGE), sum(HIGH), sum(SEC), sum(ELE)]
G = ["PhD", "master's degree", "Bachelor's degree", "Associate degree", "senior high school", "middle school",
     "elementary\nschool"]
color = ["#C63300", "#FFA488", "#FF8888", "#FF7744", "#FF5511", "#E63F00", "#FFCCCC"]

plt.pie(Y, labels=G, colors=color, explode=(0, 0, 0, 0, 0, 0, 0.3), autopct="%1.1f%%")
plt.title("108Âπ¥Êñ∞ÁîüÂÖíÊØçË¶™Â≠∏Ê≠∑ÊØî‰æãÂúñ", fontproperties=myfont, size=13)
plt.axis("equal")
plt.savefig('4.jpg', dpi=300)

# %% Âá∫ÁîüÂüéÂ∏Ç Top 7Èï∑Ê¢ùÂúñ
Dict = {}
Y = []
G = []
for i in range(len(j)):
    Dict["{0}".format(j[i])] = loc[i]
y = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
for i in range(7):
    Y.append(y[i][1])
    G.append(y[i][0])
G = ['New Taipei', 'Taoyuan', 'Taichung', 'Taipei', 'Kaohsiung', 'Changhua', 'Tainan']  # È°ØÁ§∫‰∏ç‰∫Ü‰∏≠ÊñáQQ

plt.figure(figsize=(8, 4))
plt.bar(X, height=Y, width=4, color="#CCBBFF", tick_label=G)  # orientation = horizontal tick_label=j
plt.xlabel("ÂüéÂ∏Ç", fontproperties=myfont, size=13)
plt.ylabel("‰∫∫Êï∏", fontproperties=myfont, size=13)
plt.title("108Âπ¥Êñ∞ÁîüÂÖíÂá∫ÁîüÂüéÂ∏Ç Top 7", fontproperties=myfont, size=15)
plt.savefig('5.jpg', dpi=300)

# %% Âåó‰∏≠ÂçóÊù±Èõ¢Â≥∂ ÂúìÈ§ÖÂúñ
N = loc[0] + loc[1] + loc[2] + loc[6] + loc[7] + loc[17] + loc[18]
W = loc[3] + loc[8] + loc[9] + loc[10]
S = loc[4] + loc[5] + loc[11] + loc[12] + loc[13] + loc[19]
E = loc[14] + loc[15]
O = loc[16] + loc[20] + loc[21]
Y = [N, W, S, E, O]
G = ["North", "West", "South", "East", "offshore islands"]
color = ["#FFEE99", "#FFDD55", "#FFCC22", "#EEEE00", "#DDAA00"]

plt.pie(Y, labels=G, colors=color, explode=(0, 0, 0, 0, 0.3), autopct="%1.1f%%")
plt.title("108Âπ¥ÂêÑÂú∞ÂçÄÊñ∞ÁîüÂÖíÊØî‰æã", fontproperties=myfont, size=13, loc="right")
plt.axis("equal")
plt.savefig('6.jpg', dpi=300)
# %% Âè∞ÁÅ£ÂêÑÁ∏£Â∏ÇÂú∞Âúñ
>>>>>>> Chi_0805
county_shp = gpd.read_file(r'D:\NCKU\108-2\Coding-X_Python\map2\COUNTY_MOI_1081121.shp')
# county_shp.plot(cmap='RdBu')

num = [145, 3053, 12249, 3135, 4194, 4706, 2062, 3871, 20986, 27965, 21209, 11711, 22493, 3050, 4422, 1676, 2937, 1194,
       14317, 1467, 2411, 988]
county_shp['number'] = np.array(num)
<<<<<<< HEAD
county_shp = county_shp.drop([18],axis=0) #ß‚∞™∂ØßR±º
=======
county_shp = county_shp.drop([18], axis=0)  # ÊääÈ´òÈõÑÂà™Êéâ
>>>>>>> Chi_0805
county_shp["center"] = county_shp["geometry"].centroid
TW_points = county_shp.copy()
TW_points.set_geometry("center", inplace=True)
texts = []
ax = county_shp.plot(cmap="gray_r", column='number', legend=True, scheme='quantiles')
plt.legend(loc='best')
plt.axis("off")

for x, y, label in zip(TW_points.geometry.x, TW_points.geometry.y, TW_points.COUNTYENG):
    texts.append(plt.text(x, y, label, fontsize=5))

aT.adjust_text(texts, force_points=0.3, force_text=0.8, expand_points=(2, 2), expand_text=(1, 1),
               arrowprops=dict(arrowstyle="-", color='grey', lw=0.5))
plt.savefig('map.jpg', dpi=300)

