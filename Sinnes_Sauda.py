import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def Sinnes_sauda_lister():
    Sinnes_tid = list()
    Sinnes_lufttemperatur = list()
    Sinnes_lufttrykk = list()

    Sauda_tid = list()
    Sauda_lufttemperatur = list()
    Sauda_lufttrykk = list()

    with open("dataAnalyse/datafiler/temperatur_trykk_sauda_sinnes_samme_tidsperiode.csv", "r",
        encoding= "UTF-8") as Sinnes_Sauda_fil:
        leser_sinnes_sauda = csv.reader(Sinnes_Sauda_fil, delimiter= ";")
        next(leser_sinnes_sauda)
        rekke = 0
        for hver_rekke in leser_sinnes_sauda:
            if rekke < 96:

                Sinnes_tid.append(hver_rekke[2])
                Sinnes_lufttemperatur.append(float(hver_rekke[3].replace(",", ".")))
                Sinnes_lufttrykk.append(float(hver_rekke[4].replace(",", ".")))
                rekke += 1

            elif rekke >= 96 and rekke < 192:
                Sauda_tid.append(hver_rekke[2])
                Sauda_lufttemperatur.append(float(hver_rekke[3].replace(",", ".")))
                Sauda_lufttrykk.append(float(hver_rekke[4].replace(",", ".")))
                rekke += 1
                 
    time_format = "%d.%m.%Y %H:%M"
    Sinnes_tid = [datetime.datetime.strptime(tid, time_format) for tid in Sinnes_tid]
    Sauda_tid = [datetime.datetime.strptime(tid, time_format) for tid in Sauda_tid]

    # Return all the data
    return Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk

Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk= Sinnes_sauda_lister()
def plotter_Sinnes_sauda(Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk):
    plt.subplot(2,1,1)
    plt.plot(Sinnes_tid, Sinnes_lufttemperatur, label = "Sinnes lufttemperatur")
    plt.plot(Sauda_tid, Sauda_lufttemperatur, label = "Sauda lufttemperatur")
    plt.legend()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(Sinnes_tid, Sinnes_lufttrykk, label = "Sinnes lufttrykk")
    plt.plot(Sauda_tid, Sauda_lufttrykk, label = "Sauda lufttrykk")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

