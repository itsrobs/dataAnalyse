import datetime
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from Datafiler_lister import Datafil_MET_lister, datafil_lokal_lister

# Last inn lister
Tid_norsknormaltid_MET, Lufttemperatur_MET, Lufttrykk_MET = Datafil_MET_lister()
Trykk_absolutt_lokal, Trykk_barometer_lokal, Datoer_lokal = datafil_lokal_lister()


# Funksjon som konverterer datoene i lokal datafil til datetime objekter
def konverter_dato_lokal(dato_tid):
    formater = ["%m.%d.%Y %H:%M", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S %p"]
    for formateringsformat in formater:
        try:
            return datetime.strptime(dato_tid, formateringsformat)
        except ValueError:
            continue
    return None
datetime_datoer_lokal = [konverter_dato_lokal(dato) for dato in Datoer_lokal]


# Funksjon som konverterer datoene i MET datafil til datetime objekter
def konverter_dato_MET(dato_tid):
    formater = ["%d.%m.%Y %H:%M"]
    for formateringsformat in formater:
        try:
            return datetime.strptime(dato_tid, formateringsformat)
        except ValueError:
            continue
    return None
datetime_normaltid_MET =[konverter_dato_MET(dato) for dato in Tid_norsknormaltid_MET]


# Funksjon som fikser korresponderende tall til datoer til Barometer trykk lokal liste
def justere_lister_barometer(datetime_list, value_list):
    justerte_datoer_lokal = []
    justerte_barometer_lokal = []
    for date, value in zip(datetime_list, value_list):
        if date is not None and value is not None:
            justerte_datoer_lokal.append(date)
            justerte_barometer_lokal.append(value)

    return justerte_datoer_lokal, justerte_barometer_lokal
justert_datoer_lokal, justert_barometer_lokal = justere_lister_barometer(datetime_datoer_lokal, Trykk_barometer_lokal)


# Justerer y verdier
justert_barometer_lokal = [float(x) * 10 for x in justert_barometer_lokal]
Trykk_absolutt_lokal = [float(x) * 10 for x in Trykk_absolutt_lokal]


""" Starter plotting av grafene her """
# Størrelse plot
plt.figure(figsize=(12, 6))

# Plotter grafene
plt.plot(datetime_datoer_lokal, Trykk_absolutt_lokal, color='blue', label="Absolutt Trykk")
plt.plot(justert_datoer_lokal, justert_barometer_lokal, color='orange', label="Barometisk Trykk")
plt.plot(datetime_normaltid_MET, Lufttrykk_MET, color="green", label= "Absolutt trykk MET")

# Finjusterer x og y aksene
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=8))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=7))
plt.xticks(rotation=45)
plt.legend()

# Display the plot
plt.show()