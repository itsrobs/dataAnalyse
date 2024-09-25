import csv

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
Trykk_absloutt, Trykk_barometer = datafil2_MET_lister()

Trykk_barometer_komma = [(point.replace(",",".")) for point in Trykk_barometer]
cleaned_data = [float(item) for item in Trykk_barometer_komma if item]
print(cleaned_data)
    
    

#print(Trykk_barometer_komma)