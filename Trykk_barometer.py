import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from Datafiler_lister import Datafil1_lister, datafil2_MET_lister

# Load data
Tid_norsknormaltid, Lufttemperatur, Lufttrykk = Datafil1_lister()
Trykk_absolutt, Trykk_barometer, Datoer_MET = datafil2_MET_lister()

# Function to convert date strings to datetime objects
def konverter_dato(dato_tid):
    formater = ["%m.%d.%Y %H:%M", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S %p"]
    for formateringsformat in formater:
        try:
            return datetime.datetime.strptime(dato_tid, formateringsformat)
        except ValueError:
            continue
    return None

# Convert dates
konverterte_datoer = [konverter_dato(dato) for dato in Datoer_MET]



Trykk_barometer_sample = Trykk_barometer[::6]
konverterte_datoer_barometer = konverterte_datoer[::6]



# Plotting the dat


plt.plot(konverterte_datoer, Trykk_absolutt, color='blue', label='Absolutt Trykk')
plt.plot(konverterte_datoer_barometer, Trykk_barometer_sample, color='orange', label='Barometer Trykk')



plt.xticks(rotation=45)


# Display the plot
plt.show()