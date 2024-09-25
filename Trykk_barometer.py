import csv
import datetime
import matplotlib.pyplot as plt

def datafil2_MET_lister():
    Trykk_barometer = list()
    Trykk_absolutt = list()
    with open("GitHub/dataAnalyse/datafiler/trykk_og_temperaturlogg_rune_time.csv",
        "r", encoding="UTF8") as datafil2_MET:
        lesing_fil = csv.reader(datafil2_MET, delimiter = ";")
        next(lesing_fil)
        for rekker in lesing_fil:
                Trykk_barometer.append(rekker[2])
                Trykk_absolutt.append(rekker[3])

        datafil2_MET.close()
    return Trykk_absolutt, Trykk_barometer
Trykk_absolutt, Trykk_barometer = datafil2_MET_lister()

Trykk_barometer_komma = [(point.replace(",",".")) for point in Trykk_barometer]
Trykk_absolutt_komma = [(point.replace(",",".")) for point in Trykk_absolutt]
cleaned_data = [float(item) for item in Trykk_barometer_komma if item]


    
    

lokalStasjon = "GitHub/dataAnalyse/datafiler/trykk_og_temperaturlogg_rune_time.csv"
dato = []

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
with open(lokalStasjon, "r") as localWeather:
        weather = csv.DictReader(localWeather, delimiter=";")
        for line in weather:
            date = dato.append(datetimeConverter(line["Dato og tid"]))
        

                 
plt.plot(dato, Trykk_absolutt_komma)
plt.title("Pressure vs. Time")
plt.xlabel("Date and Time")
plt.ylabel("Pressure (Absolutt)")
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()


print(date)

#print(Trykk_barometer_komma)