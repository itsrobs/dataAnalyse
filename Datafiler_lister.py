import csv


# Lager lister av datafil 1:
def Datafil1_lister():
    Tid_norsknormaltid = list()
    Lufttemperatur = list()
    Lufttrykk = list()
    with open("GitHub/dataAnalyse/datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv"
            , "r", encoding="utf-8") as datafil1:
        leser_filen = csv.reader(datafil1, delimiter= ";")
        next(leser_filen)
        for hver_rekke in leser_filen:
            Tid_norsknormaltid.append(hver_rekke[2])
            Lufttemperatur.append(hver_rekke[3])
            Lufttrykk.append(hver_rekke[4])
        datafil1.close()
    return Tid_norsknormaltid, Lufttemperatur, Lufttrykk

# For å hente listene i en annen kode
Tid_norsknormaltid, Lufttemperatur, Lufttrykk = Datafil1_lister()



# Lager lister av datafil 1:
def datafil2_MET_lister():
    Trykk_barometer = list()
    Trykk_absolutt = list()
    Datoer_Met= list()
    with open("GitHub/dataAnalyse/datafiler/trykk_og_temperaturlogg_rune_time.csv",
        "r", encoding="UTF8") as datafil2_MET:
        lesing_fil = csv.reader(datafil2_MET, delimiter = ";")
        next(lesing_fil)
        for rekker in lesing_fil:
                Datoer_MET.append(rekker[0])
                Trykk_barometer.append(rekker[2])
                Trykk_absolutt.append(rekker[3])

        datafil2_MET.close()
    return Trykk_absolutt, Trykk_barometer
# For å hente listene i en annen kode
Trykk_absolutt, Trykk_barometer, Datoer_MET = datafil2_MET_lister()
