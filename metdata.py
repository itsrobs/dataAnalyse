import datetime, csv


lokalStasjon = "datafiler/trykk_og_temperaturlogg_rune_time.csv"

dato = list()
tidspunkt = list()
temperatur = list()



with open(lokalStasjon, "r") as localWeather:
    weather = csv.DictReader(localWeather, delimiter=";")
    for line in weather:
        dato.append(line["Dato og tid"])
        temperatur.append(line["Temperatur (gr Celsius)"])
