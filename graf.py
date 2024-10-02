import datetime
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from Datafiler_lister import Datafil_MET_lister, datafil_lokal_lister

# Last inn lister
Tid_norsknormaltid_MET, Lufttemperatur_MET, Lufttrykk_MET = Datafil_MET_lister()
Trykk_absolutt_lokal, Trykk_barometer_lokal, Datoer_lokal, Temperatur_lokal = datafil_lokal_lister()

from Trykk_barometer import konverter_dato_lokal, konverter_dato_MET
datetime_datoer_lokal = [konverter_dato_lokal(dato) for dato in Datoer_lokal]
datetime_normaltid_MET =[konverter_dato_MET(dato) for dato in Tid_norsknormaltid_MET]

plt.plot(datetime_datoer_lokal, Temperatur_lokal, color= "Blue", label= "Temperatur")
plt.plot(datetime_normaltid_MET, Lufttemperatur_MET, color= "green", label = "Temperatur MET")
plt.show()