import csv


Navn = list()
Stasjon = list()
Tid_norsknormaltid = list()
Lufttemperatur = list()
Lufttrykk = list()

with open("Øvinger/Øving6_gruppeprosjekt/datafiler/temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
          , "r", encoding="utf-8") as datafil1:
    leser_filen = csv.reader(datafil1, delimiter= ";")
    next(leser_filen)
    for hver_rekke in leser_filen:
        Navn.append(hver_rekke[0])
        Stasjon.append(hver_rekke[1])
        Tid_norsknormaltid.append(hver_rekke[2])
        Lufttemperatur.append(hver_rekke[3])
        Lufttemperatur.append(hver_rekke[4])

datafil1.close()

