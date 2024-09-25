import datetime, csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


lokalStasjon = "datafiler/trykk_og_temperaturlogg_rune_time.csv"


dato = []
temperatur = []


def datetimeConverter(date_time_string):
    try:
        format1 = "%m.%d.%Y %H:%M"
        date_time = datetime.datetime.strptime(date_time_string, format1)
        return date_time
    except:
        pass
    try:
        format2 = "%m/%d/%Y %I:%M:%S %p"
        date_time = datetime.datetime.strptime(date_time_string, format2)
    except:
        try:
            format3 = "%m/%d/%Y %H:%M:%S %p"
            date_time = datetime.datetime.strptime(date_time_string, format3)
        except:
            pass
    return date_time


#Finner gjennomsnitt temperatur og datoer, returnerer en liste med en liste av datoer[0] og temperaturer[1], 
#antall er hvor mange temperaturverdier du vil regne gjennomsnitt fra
def gjennomsnitt(tid, temperaturer, antall):
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


#Åpner og leser inn temperatur og dato i en liste
def opener():
    with open(lokalStasjon, "r") as localWeather:
        weather = csv.DictReader(localWeather, delimiter=";")
        for line in weather:
            dato.append(datetimeConverter(line["Dato og tid"]))
            temperatur.append(line["Temperatur (gr Celsius)"])


def plotter(x1, y1, label):
    plt.plot(x1,y1, label=label)
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=15, integer=True))
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=6))
    plt.legend()
    plt.xlabel("Dato")
    plt.ylabel("Temp")
    

def main():
    opener()
    temperaturFloat = [float(point.replace(",",".")) for point in temperatur]
    averageDateTime = gjennomsnitt(dato, temperaturFloat, 30)
    plotter(dato, temperaturFloat, "Temperatur")
    plotter(averageDateTime[0], averageDateTime[1], "Gjennomsnittstemperatur")

    plt.show()


if __name__=="__main__":
    main()