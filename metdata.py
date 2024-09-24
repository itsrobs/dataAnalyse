import datetime, csv
import matplotlib.pyplot as plt

dato1 = "06.12.2021 23:37"
dato2 = "06/13/2021 01:04:58 am"



def datetimeConverter(date_time_string):
    try:
        format1 = "%m.%d.%Y %H:%M"
        date_time = datetime.datetime.strptime(date_time_string, format1)
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






lokalStasjon = "datafiler/trykk_og_temperaturlogg_rune_time.csv"

dato = list()
tidspunkt = list()
temperatur = list()


def opener():
    with open(lokalStasjon, "r") as localWeather:
        weather = csv.DictReader(localWeather, delimiter=";")
        for line in weather:
            dato.append(datetimeConverter(line["Dato og tid"]))
            temperatur.append(line["Temperatur (gr Celsius)"])


def plotter(x, y):
    plt.plot(x,y)
    plt.ylabel("temperatur")
    plt.xlabel("Dato/klokkeslett")
    plt.show()



def main():
    opener()
    plotter(dato, temperatur)
    print("DATO1: ", dato[0], " DATO2: ",  dato[-1],"\n", "TEMP1: ", temperatur[0], " TEMP2: ", temperatur[-1])


if __name__=="__main__":
    main()