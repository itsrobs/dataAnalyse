# -*- coding: utf-8 -*-
from apiMET import hent_sol_tider, solData
import datetime, csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.dates import DateFormatter
from Sinnes_Sauda import Sinnes_sauda_lister, plotter_Sinnes_sauda

# Filplassering for data som skal brukes i programmet
lokal_stasjon = "datafiler/trykk_og_temperaturlogg_rune_time.csv"
met_stasjon = "datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv"

# Setter opp tomme lister for bruk
lokal_dato = []
lokal_temperatur = []
lokal_trykk = []
lokal_abs_trykk = []

met_dato = []
met_temperatur = []
met_trykk = []

# Spesifiserer indekser med onsket tidspunkt for solnedgang mellom
# 11. juni 2021 klokka 17:31 til 12. juni 2021 klokka 03:05


def datetimeConverter(date_time_string):
    # Konverterer datoformatet som blir brukt i den lokale fila og gjør om til datetime
    formater = ["%m.%d.%Y %H:%M", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S %p"]
    for formatet in formater:
        try:
            return datetime.datetime.strptime(date_time_string, formatet)
        except:
            pass


def datetimeConverterMET(date_time_string):
    # Konverterer datoformatet som blir brukt i MET fila og gjør om til datetime
    formater = ["%d.%m.%Y %H:%M"]
    for formatet in formater:
        try:
            return datetime.datetime.strptime(date_time_string, formatet)
        except:
            pass


def gjennomsnitt(tid, temperaturer, antall):
    # Finner gjennomsnitt temperatur og datoer, returnerer en liste med en liste av datoer[0] og temperaturer[1], 
    # antall er hvor mange temperaturverdier du vil regne gjennomsnitt fra
    gjennomsnittTempListe = []
    gjennomsnittDatoListe = []
    totalGjennomsnitt = []
    calculator = 0
    count = 0
    for temp in temperaturer:
        if count < antall:
            calculator += temp
            count += 1
        else:
            gjennomsnittTempListe.append(calculator/count)
            calculator = 0
            count = 0
    count = 0
    for d in tid:
        if count < antall:
            count += 1
        else:
            gjennomsnittDatoListe.append(d)
            count = 0
    totalGjennomsnitt.append(gjennomsnittDatoListe)
    totalGjennomsnitt.append(gjennomsnittTempListe)
    return totalGjennomsnitt


def opener():
    # Åpner og leser inn temperatur og dato fra den lokale fila og setter dataen inn i en liste
    with open(lokal_stasjon, "r") as localWeather:
        weather = csv.DictReader(localWeather, delimiter=";")
        exceptTrykk = 0
        exceptAbsTrykk = 0
        for line in weather:
            lokal_dato.append(datetimeConverter(line["Dato og tid"]))
            tempFloat = line["Temperatur (gr Celsius)"].replace(",",".")
            lokal_temperatur.append(float(tempFloat))
            
            tempTrykk = line["Trykk - barometer (bar)"].replace(",",".")
            try:
                tempTrykk = float(tempTrykk)*10
                lokal_trykk.append(tempTrykk)
                exceptTrykk = tempTrykk
            except:
                lokal_trykk.append(float(exceptTrykk))
                
            tempAbsTrykk = line["Trykk - absolutt trykk maaler (bar)"].replace(",",".")
            try:
                tempAbsTrykk = float(tempAbsTrykk)*10
                lokal_abs_trykk.append(tempAbsTrykk)
                exceptAbsTrykk = tempAbsTrykk
            except:
                print(tempAbsTrykk)
                lokal_abs_trykk.append(exceptAbsTrykk)
            
                
def metOpener():
    # Åpner og leser inn temperatur og dato fra MET fila og setter dataen inn i en liste
    with open(met_stasjon, "r") as metWeather:
        weather = csv.DictReader(metWeather, delimiter=";")
        for line in weather:
            if "Sola" in str(line):
                met_dato.append(datetimeConverterMET(line["Tid(norsk normaltid)"]))
                tempFloat = line["Lufttemperatur"].replace(",",".")
                met_temperatur.append(float(tempFloat))
                tempTrykk = line["Lufttrykk i havnivaa"].replace(",",".")
                met_trykk.append(float(tempTrykk))

def punktSolned(variabel):
    # Henter inn punkt manuel fra solned_indekser
    p1 = [lokal_dato[variabel[0]], lokal_temperatur[variabel[0]]]
    p2 = [lokal_dato[variabel[1]], lokal_temperatur[variabel[1]]]
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    return x, y

def punktSolnedMet(variabel):
    # Henter inn punkt manuel fra solned_indekser
    p1 = [lokal_dato[variabel[0]], met_temperatur[variabel[0]]]
    p2 = [lokal_dato[variabel[1]], met_temperatur[variabel[1]]]
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    return x, y


def plotter(x1, y1, label, ylab, sub):
    # Tar inn liste med x og y-verdier, og plotter dem.
    plt.gca().xaxis.set_major_formatter(DateFormatter("%m-%d %H"))
    plt.subplot(2, 1, sub)
    plt.plot(x1,y1, label=label)
    #plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=15, integer=True))
    #plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))
    plt.legend()
    plt.xlabel("Tid")
    plt.ylabel(ylab)
    
    
def solOppOgNed():
    solopp, solned = solData()
    opp = 2
    ned = 2
    for i in lokal_dato:
        
        if str(i.strftime('%H:%M')) == solopp.strftime('%H:%M'):
            break
        else:
            opp += 1
        
    for i in lokal_dato:
        
        if str(i.strftime('%H:%M')) == solned.strftime('%H:%M'):
            break
        else:
            ned += 1
    return opp, ned


def temperaturFall():
    opp, ned =  "03:05", "17:31"
    oppCount = 2
    nedCount = 2
    for i in lokal_dato:
        
        if str(i.strftime('%H:%M')) == opp:
            break
        else:
            oppCount += 1
        
    for i in lokal_dato:
        
        if str(i.strftime('%H:%M')) == ned:
            break
        else:
            nedCount += 1
    return oppCount, nedCount


def temperaturFallMet():
    opp, ned =  "03:00", "18:00"
    oppCount = 2
    nedCount = 2
    oppEkstraCount = 1
    for i in met_dato:
        
        if str(i.strftime('%H:00')) == opp:
            if oppEkstraCount == 0:
                break
            else:
                oppEkstraCount = 0
        else:
            oppCount += 1
        
    for i in met_dato:
        
        if str(i.strftime('%H:%M')) == ned:
                break
        else:
            nedCount += 1
    return oppCount, nedCount

# Plot for histogram
def plot_histogram(data1, data2):
    figure, (ax1, ax2) = plt.subplots(2, 1)

    # histogram data: bins lager en serie intervaller med grader fra min til max, teller hver data som er i hver "bin"
    ax1.hist(data1, bins=range(int(min(data1)), int(max(data1)) + 2))
    ax1.set_xlabel('Temperatur (°C)')
    ax1.set_ylabel('Antall')
    ax1.set_title('Histogram over Lokal Temperatur')

    # Plot andre histogram
    ax2.hist(data2, bins=range(int(min(data2)), int(max(data2)) + 2))
    ax2.set_xlabel('Temperatur (°C)')
    ax2.set_ylabel('Antall')
    ax2.set_title('Histogram over MET Temperatur')

    plt.tight_layout()
    plt.show()

# Sinnes og sauda plot i eget vindu
def plotter_Sinnes_sauda(Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk,
    met_dato, met_temperatur, met_trykk):
    plt.subplot(2,1,1)
    plt.plot(Sinnes_tid, Sinnes_lufttemperatur, label = "Sinnes lufttemperatur")
    plt.plot(Sauda_tid, Sauda_lufttemperatur, label = "Sauda lufttemperatur")
    plt.plot(met_dato, met_trykk, label = "Sola Lufttemperatur")
    plt.legend()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(Sinnes_tid, Sinnes_lufttrykk, label = "Sinnes lufttrykk")
    plt.plot(Sauda_tid, Sauda_lufttrykk, label = "Sauda lufttrykk")
    plt.plot(met_dato, met_temperatur, label = "Sola lufttrykk")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
    
    # Apner filer og laster dem inn i lister
    opener()
    metOpener()
    
    # Regner ut gjennomsnitt
    averageDateTime = gjennomsnitt(lokal_dato, lokal_temperatur, 30)
    
    solOppOgNed()
    temperaturFall()


    # Setter opp Subplots
    plt.subplots(2, 1)
    
    # Øvre Subplot
    plotter(lokal_dato, lokal_temperatur, "Lokal Temperatur", "Temp", 1)
    plotter(averageDateTime[0], averageDateTime[1], "Gjennomsnittstemperatur", "Temp", 1)
    plotter(met_dato, met_temperatur, "MET Temperatur", "Temp", 1)
    plotter(*punktSolned(solOppOgNed()), "Temperaturfall soloppgang til solnedgang", "Temp", 1)
    plotter(*punktSolned(temperaturFall()), "Temperaturfall maksimal til minimal Lokal", "Temp", 1)
    plotter(*punktSolnedMet(temperaturFallMet()), "Temperaturfall maksimal til minimal MET", "Temp", 1)
    
    
    # Nedre Subplot
    plotter(lokal_dato, lokal_abs_trykk, "Absolutt trykk", "Trykk", 2)
    plotter(lokal_dato, lokal_trykk, "Barometrisk trykk", "Trykk", 2)
    plotter(met_dato, met_trykk, "Absolutt trykk MET", "Trykk", 2)
    '''
    # Nytt vindu
    plt.figure(figsize=(8, 6))
    Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk = Sinnes_sauda_lister()
    
    # Plot Sinnes-Sauda data
    plotter_Sinnes_sauda(Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk, met_dato, met_trykk, met_temperatur)
    
    # Plotter histogram
    plot_histogram(lokal_temperatur, met_temperatur)
   '''  
    # Viser fullført plot
    plt.show()


if __name__=="__main__":
    main()