# -*- coding: utf-8 -*-
from apiMET import solData
import datetime, csv
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from Sinnes_Sauda import Sinnes_sauda_lister
import math

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

def trykkDifferanse(lst1, lst2):
    differanseListe = []
    for i in range(len(lst1)):
        differanseListe.append(abs(lst1[i]-lst2[i]))
    return differanseListe


def finnLinje(variabel, kilde):
    # finner og returnerer to lister, x[p1, p2] og y[p1, p2]
    p1 = [eval(kilde+"_dato")[variabel[0]], eval(kilde+"_temperatur")[variabel[0]]]
    p2 = [eval(kilde+"_dato")[variabel[1]], eval(kilde+"_temperatur")[variabel[1]]]
    x = [p1[0], p2[0]]
    y = [p1[1], p2[1]]
    return x, y

def plotter(x1, y1, label, ylab, sub, antall = 2):
    # Tar inn liste med x og y-verdier, og plotter dem.
    plt.gca().xaxis.set_major_formatter(DateFormatter("%m-%d %H"))
    plt.subplot(antall, 1, sub)
    plt.plot(x1,y1, label=label)
    #plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=15, integer=True))
    #plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=12))
    plt.legend()
    plt.xlabel("Tid")
    plt.ylabel(ylab)
    
    
def solOppOgNed(kilde):
    solopp, solned = solData()
    if kilde == "lokal":
        opp = 2
        ned = 2
        for i in eval(kilde+"_dato"):
            
            if str(i.strftime('%H:%M')) == solopp.strftime('%H:%M'):
                break
            else:
                opp += 1
            
        for i in eval(kilde+"_dato"):
            
            if str(i.strftime('%H:%M')) == solned.strftime('%H:%M'):
                break
            else:
                ned += 1
    else:
        opp = 1
        ned = 1
        for i in eval(kilde+"_dato"):
            
            if str(i.strftime('%d %H')) == solopp.strftime('12 %H'):
                break
            else:
                opp += 1
            
        for i in eval(kilde+"_dato"):
            
            if str(i.strftime('%d %H')) == solned.strftime('11 %H'):
                break
            else:
                ned += 1
    return opp, ned


def temperaturFall(kilde):
    if kilde == "lokal":
        opp, ned =  "11 17:31", '12 03:05'
    else:
        opp, ned = "11 18:00", "12 03:00"
    oppCount = 2
    nedCount = 2
    for i in eval(kilde+"_dato"):
        if str(i.strftime('%d %H:%M')) == opp:
            break
        else:
            oppCount += 1
        
    for i in eval(kilde+"_dato"):
        
        if str(i.strftime('%d %H:%M')) == ned:
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
    # plt.show()

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
    # plt.show()


def standardAvvik(maalinger):
    summgjennomsnitt = 0.0
    summstandardavvik = 0.0
    for n in range(len(maalinger)):
        summgjennomsnitt += maalinger[n]
    gjennomsnittet = (1/len(maalinger)*summgjennomsnitt)  
    for n in range(len(maalinger)):
       summstandardavvik += (maalinger[n]-gjennomsnittet)**2
    standardavvik = math.sqrt((1/(len(maalinger)-1)) * summstandardavvik)
    return standardavvik


def main():
    # Apner filer og laster dem inn i lister
    opener()
    metOpener()
    # print(lokal_dato)

    datoliste = []

    lokal_trykk2 = []
    lokal_temp2 = []

    met_temp2 = []
    met_trykk2 = []

    ftemp = []
    ftrykk = []

    for index, temp in enumerate(lokal_temperatur):
        nosec = lokal_dato[index].replace(second=00)
        if nosec in met_dato and nosec not in datoliste:
            lokal_temp2.append(temp)
            datoliste.append(nosec)
            lokal_trykk2.append(lokal_trykk[index])

    for index, temp in enumerate(met_temperatur):
        if met_dato[index] in datoliste:
            met_temp2.append(temp)
            met_trykk2.append(met_trykk[index])
        
    for i, d in enumerate(datoliste):
        ftemp.append(abs(met_temp2[i]-lokal_temp2[i]))
        ftrykk.append(abs(met_trykk2[i]-lokal_trykk2[i]))



    gjennomsnittForskjellTemp = sum(ftemp)/len(ftemp)
    gjennomsnittForskjellTrykk = sum(ftrykk)/len(ftrykk)
    print(f"Gjennomsnittlig temperaturforskjell: {gjennomsnittForskjellTemp},\nGjennomsnitt trykkforskjell: {gjennomsnittForskjellTrykk}")
    print(f"Maks temp forskjell: {max(ftemp)} dato: {datoliste[ftemp.index(max(ftemp))]} \nMin temp forskjell: {min(ftemp)} dato: {datoliste[ftemp.index(min(ftemp))]}")
    print(f"Maks trykk forskjell: {max(ftrykk)} dato: {datoliste[ftrykk.index(max(ftrykk))]}\nMin trykk forskjell: {min(ftrykk)} dato: {datoliste[ftrykk.index(min(ftrykk))]}")


    # Regner ut gjennomsnitt
    averageDateTime = gjennomsnitt(lokal_dato, lokal_temperatur, 30)
    
    """
    averageStandardAvvik = []
    for n in range(len(averageDateTime[1])):
        averageStandardAvvik.append(((lokal_temperatur[n]-averageDateTime[1][n])**2)/(len(averageDateTime)))
    """
    

    # Setter opp Subplots
    plt.subplots(2, 1)
    
    # Øvre Subplot
    plotter(lokal_dato, lokal_temperatur, "Lokal Temperatur", "Temp", 1)

    plt.plot(datoliste, ftemp, label="Forskjell på temp")
    plt.plot(datoliste, ftrykk, label="Forskjell på trykk")


    plt.errorbar(averageDateTime[0], averageDateTime[1], yerr=standardAvvik(lokal_temperatur), errorevery=30, capsize=4, label = "Gjennomsnittlig Temperatur med Standardavvik")
    plotter(met_dato, met_temperatur, "MET Temperatur", "Temp", 1)
    plotter(*finnLinje(solOppOgNed("lokal"), "lokal"), "Temperaturfall soloppgang til solnedgang Lokal", "Temp", 1)
    plotter(*finnLinje(temperaturFall("lokal"), "lokal"), "Temperaturfall maksimal til minimal Lokal", "Temp", 1)
    #plotter(*finnLinje(temperaturFall("met"), "met"), "Temperaturfall maksimal til minimal MET", "Temp", 1)
    plotter(*finnLinje(solOppOgNed("met"), "met"), "Temperaturfall soloppgang til solnedgang MET", "Temp", 1)
    
    # Nedre Subplot
    plotter(lokal_dato, lokal_abs_trykk, "Absolutt trykk", "Trykk", 2)
    plotter(lokal_dato, lokal_trykk, "Barometrisk trykk", "Trykk", 2)
    plotter(met_dato, met_trykk, "Absolutt trykk MET", "Trykk", 2) 
    plt.figure(figsize=(8, 6))

    trykk_average = gjennomsnitt(lokal_dato, trykkDifferanse(lokal_trykk, lokal_abs_trykk), 10)  
    plotter(trykk_average[0], trykk_average[1], "Trykk Differanse", "Trykk Differanse", 1, 1)
    
    # Nytt vindu
    plt.figure(figsize=(8, 6))
    Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk = Sinnes_sauda_lister()
    
    # Plot Sinnes-Sauda data
    plotter_Sinnes_sauda(Sinnes_tid, Sinnes_lufttemperatur, Sinnes_lufttrykk, Sauda_tid, Sauda_lufttemperatur, Sauda_lufttrykk, met_dato, met_trykk, met_temperatur)
    
    # Plotter histogram
    plot_histogram(lokal_temperatur, met_temperatur)
   
    # Viser fullført plot
    plt.show()


if __name__=="__main__":
    main()