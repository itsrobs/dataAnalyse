import csv


# Lager lister av datafil MET:
def Datafil_MET_lister():
    Tid_norsknormaltid_MET = list()
    Lufttemperatur_MET = list()
    Lufttrykk_MET = list()
    with open("dataAnalyse/datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv"
            , "r", encoding="utf-8") as datafil1:
        leser_filen = csv.reader(datafil1, delimiter= ";")
        next(leser_filen)
        for hver_rekke in leser_filen:
            Tid_norsknormaltid_MET.append(hver_rekke[2])
            lufttemp_str = (hver_rekke[3].replace(",", "."))
            lufttrykk_str = (hver_rekke[4].replace(",", "."))
            
            Lufttemperatur_MET.append(float(lufttemp_str) if lufttemp_str else None)
            Lufttrykk_MET.append(float(lufttrykk_str) if lufttrykk_str else None)
    return Tid_norsknormaltid_MET, Lufttemperatur_MET, Lufttrykk_MET

# For å hente listene i en annen kode



# Lager lister av datafil lokaL:
def datafil_lokal_lister():
    Trykk_barometer_lokal = list()
    Trykk_absolutt_lokal = list()
    Datoer_lokal= list()
    Temperatur_lokal = list()
    with open("dataAnalyse/datafiler/trykk_og_temperaturlogg_rune_time.csv",
        "r", encoding="UTF8") as datafil2_MET:
        lesing_fil = csv.reader(datafil2_MET, delimiter = ";")
        next(lesing_fil)
        for rekker in lesing_fil:
            Datoer_lokal.append(rekker[0])
            trykk_barometer_str = (rekker[2].replace(",", "."))
            trykk_absolutt_str = (rekker[3].replace(",", "."))
            temperatur_str =(rekker[4].replace(",", "."))
            

            Trykk_barometer_lokal.append(float(trykk_barometer_str) if trykk_barometer_str else None)
            Trykk_absolutt_lokal.append(float(trykk_absolutt_str) if trykk_absolutt_str else None)
            Temperatur_lokal.append(float(temperatur_str) if temperatur_str else None)
    
    return Trykk_absolutt_lokal, Trykk_barometer_lokal, Datoer_lokal, Temperatur_lokal
# For å hente listene i en annen kode

Tid_norsknormaltid_MET, Lufttemperatur_MET, Lufttrykk_MET = Datafil_MET_lister()
Trykk_absolutt_lokal, Trykk_barometer_lokal, Datoer_lokal,Temperatur_lokal = datafil_lokal_lister()
