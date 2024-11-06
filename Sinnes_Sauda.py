import csv
import datetime
import matplotlib.pyplot as plt

def Sinnes_sauda_lister():
    Sinna_tid = list()
    Sinna_lufttemperatur = list()
    Sinna_lufttrykk = list()

    Sauda_tid = list()
    Sauda_lufttemperatur = list()
    Sauda_lufttrykk = list()

    with open("dataAnalyse/datafiler/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv", "r",
        encoding= "UTF-8") as Sinnes_Sauda_fil:
        leser_sinna_sauda = csv.reader(Sinnes_Sauda_fil, delimiter= ";")
        next(leser_sinna_sauda)
        for i, hver_rekke in enumerate(leser_sinna_sauda):
            if i < 97:
                Sinna_tid.append(hver_rekke[2])
                Sinna_lufttemperatur.append(hver_rekke[3])
                Sinna_lufttrykk.append(hver_rekke[4])

            elif i >= 96 and i < 192:
                Sauda_tid.append(hver_rekke[2].replace(",","."))
                Sauda_lufttemperatur.append(hver_rekke[3].replace(",","."))
                Sauda_lufttrykk.append(hver_rekke[4].replace(",","."))

    return Sinna_tid, Sauda_tid, Sinna_lufttemperatur, Sauda_lufttemperatur, Sinna_lufttrykk, Sauda_lufttrykk

Sinna_tid, Sinna_lufttemperatur, Sinna_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk = Sinnes_sauda_lister()
print(enumerate(Sinna_lufttemperatur))
#print((Sauda_lufttrykk))

