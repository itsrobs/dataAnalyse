import csv



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

Tid_norsknormaltid, Lufttemperatur, Lufttrykk = Datafil1_lister()
print(Lufttrykk)


