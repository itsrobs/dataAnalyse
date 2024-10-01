import csv


# Lager lister av datafil 1:
def Datafil1_lister():
    Tid_norsknormaltid = list()
    Lufttemperatur = list()
    Lufttrykk = list()
    with open("dataAnalyse/datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv"
            , "r", encoding="utf-8") as datafil1:
        leser_filen = csv.reader(datafil1, delimiter= ";")
        next(leser_filen)
        for hver_rekke in leser_filen:
            Tid_norsknormaltid.append(hver_rekke[2])
            lufttemp_str = hver_rekke[3].replace(",", ".")
            lufttrykk_str = hver_rekke[4].replace(",", ".")
            
            Lufttemperatur.append(float(lufttemp_str) if lufttemp_str else None)
            Lufttrykk.append(float(lufttrykk_str) if lufttrykk_str else None)
    return Tid_norsknormaltid, Lufttemperatur, Lufttrykk

# For å hente listene i en annen kode



# Lager lister av datafil 1:
def datafil2_MET_lister():
    Trykk_barometer = list()
    Trykk_absolutt = list()
    Datoer_MET= list()
    with open("dataAnalyse/datafiler/trykk_og_temperaturlogg_rune_time.csv",
        "r", encoding="UTF8") as datafil2_MET:
        lesing_fil = csv.reader(datafil2_MET, delimiter = ";")
        next(lesing_fil)
        for rekker in lesing_fil:
            Datoer_MET.append(rekker[0])
            trykk_barometer_str = rekker[2].replace(",", ".")
            trykk_absolutt_str = rekker[3].replace(",", ".")
            

            Trykk_barometer.append(float(trykk_barometer_str) if trykk_barometer_str else None)
            Trykk_absolutt.append(float(trykk_absolutt_str) if trykk_absolutt_str else None)

    
    return Trykk_absolutt, Trykk_barometer, Datoer_MET
# For å hente listene i en annen kode


