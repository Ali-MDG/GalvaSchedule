from random import random, shuffle
import traceback
import Sequence_Cost
import copy
import math
import CostParameters
import Algoritma2
import openpyxl
import pandas as pd
from ProductionSequence import ProductionSequence


Xcampain = []
Xcampain_rev = []
galva_sorted = []
GIsub = []
Galvaneal = []
ZPAR = []
GalvanealGroup = []
BobinListe_P99 = []
BobinListe_rest = []
BobinListeGroupList = []
BobinListeGroup = []
select1 = 0
select2 = 0
mincost = 0
Totalcost = math.inf

Costs = []
campain_rolls = []
df = pd.read_excel("Kampanya1_Short.xlsx")

MySequenceList = []
for index, row in df.iterrows():
    bobinno = str(row["Bobin No"])
    starttime = str(row["Başlama Zamanı"])
    endtime = str(row["Bitiş Zamanı"])
    uzunluk = float(row["Uzunluk"])
    kalınlık = float(row["Kalınlık[B] (MM)"])
    genislik = float(row["Genişlik[B] (MM)"])
    HRC_kalite = str(row["HRC Kalite[B]"])
    kalite = str(row["Kalite[B]"])
    passivizasyon = str(row["Pas. Tipi[B]"])
    RTF_Ort = float(row["RTF Ort. Sıc.[B] (GC)"])
    RTF_Min = float(row["RTF min[H] (gr/m2)"])
    RTF_Max = float(row["RTF max[H] (C°)"])
    Kaplama_Tipi = str(row["Kaplama Tipi[H]"])
    YuzeyGrup = float(row["yüzey gr.[H]"])
    Oncelik = float(row["Öncelik[H]"])
    CGL_hız = float(row["CGL Maks. Hız[H] (m/dk)"])
    new_line = ProductionSequence(bobinno, starttime,  endtime, uzunluk, kalınlık, genislik, HRC_kalite,kalite,
                                  passivizasyon, RTF_Ort, RTF_Max, RTF_Min, Kaplama_Tipi, YuzeyGrup, Oncelik, CGL_hız)
    MySequenceList.append(new_line)

for i in range(len(MySequenceList)):
    print(MySequenceList[i].BobinNo, "---", MySequenceList[i].Kalınlık, "---", MySequenceList[i].Genislik, "---",
          MySequenceList[i].Passivizasyon, "---",MySequenceList[i].Oncelik,  "---",MySequenceList[i].RTF_Min, "---",
          MySequenceList[i].RTF_Max, "---", MySequenceList[i].RTF_Ort, "---", MySequenceList[i].CGL_hız)


campain_rolls = copy.copy(MySequenceList)

groupgecisinitialPP = []
for i in range(1, len(campain_rolls)):
    perthick = 0
    widechange = 0
    perthick = abs(((campain_rolls[i].Kalınlık - campain_rolls[i - 1].Kalınlık) /
                    max(campain_rolls[i - 1].Kalınlık, campain_rolls[i].Kalınlık)) * 100)
    widechange = abs(campain_rolls[i].Genislik - campain_rolls[i - 1].Genislik)
    if (perthick > CostParameters.CostParametersGA.kalinlikgecis) or (
            widechange > CostParameters.CostParametersGA.genislikgecis):
        print("thick change:", perthick, campain_rolls[i - 1].Kalınlık, campain_rolls[i].Kalınlık,
              "widechange:", widechange, campain_rolls[i - 1].Genislik, campain_rolls[i].Genislik)
        print(campain_rolls[i - 1].BobinNo, "--arası--", campain_rolls[i].BobinNo)
        groupgecisinitialPP.append(campain_rolls[i - 1])




#campain_rolls = shuffle(MySequenceList)

BegCost = Sequence_Cost.Process_Cost_2(campain_rolls)
#BegCost = Sequence_Cost.Process_Cost(campain_rolls)
print(BegCost[0]+BegCost[1]+BegCost[2]+BegCost[3])
print("Başlama", BegCost)
# for roll in Galvaneal:
#     roll.bobin_category = "Galvaneal"
#
# for roll in Zcampain:
#     roll.bobin_category = "Zcampain"
#
# for roll in Xcampain:
#     roll.bobin_category = "Xcampain"
#
# for roll in DPcampain:
#     roll.bobin_category = "DPcampain"
#
# for roll in ZPAR:
#     roll.bobin_category = "ZPAR"
#
# for roll in YediYuzeycampain:
#     roll.bobin_category = "YediYuzeycampain"
#
#
#
# print("GA bobin sayısı:", len(Galvaneal))
# print("Z bobin sayısı:", len(Zcampain))
# print("X bobin sayısı:",len(Xcampain))
# print("DP bobin sayısı:", len(DPcampain))
# print("ZPAR bobin sayısı:", len(ZPAR))
# print("Yediyüzey bobin sayısı:", len(YediYuzeycampain))
# if CostParameters.campain_tobe_scheduled == "Galvaneal":
#     campain_rolls = Galvaneal
# elif CostParameters.campain_tobe_scheduled == "Zcampain":
#     campain_rolls = Zcampain
# elif CostParameters.campain_tobe_scheduled == "Xcampain":
#     campain_rolls = Xcampain
# elif CostParameters.campain_tobe_scheduled == "DPcampain":
#     campain_rolls = DPcampain
# elif CostParameters.campain_tobe_scheduled == "ZPAR":
#     campain_rolls = ZPAR
# elif CostParameters.campain_tobe_scheduled == "YediYuzeycampain":
#     campain_rolls = YediYuzeycampain
# else:
#     print("Hatalı kampanya ismi")
#     raise SystemExit

try:
    if len(campain_rolls) > 0:
        algo2 = Algoritma2.Algorithm(campain_rolls)
        algo2.algorithm2()
except Exception as e:
    print(traceback.format_exc())
# algo = Algorithm.Algorithm(Galvaneal)
# algo = Algorithm.Algorithm(Zcampain)

# algo = Algorithm.Algorithm(DPcampain)
# algo = Algorithm.Algorithm(ZPAR)
# algo = Algorithm.Algorithm(YediYuzeycampain)
