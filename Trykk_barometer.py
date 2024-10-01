import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator

from Datafiler_lister import Datafil1_lister, datafil2_MET_lister

# Load data
Tid_norsknormaltid, Lufttemperatur, Lufttrykk = Datafil1_lister()
Trykk_absolutt, Trykk_barometer, Datoer_MET = datafil2_MET_lister()


# Function to convert date strings to datetime objects
def konverter_dato(dato_tid):
    formater = ["%m.%d.%Y %H:%M", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S %p", "%d.%m.%Y %H:%M"]
    for formateringsformat in formater:
        try:
            return datetime.datetime.strptime(dato_tid, formateringsformat)
        except ValueError:
            continue
    return None


konverterte_datoer = [konverter_dato(dato) for dato in Datoer_MET]
konvertert_normaltid =[konverter_dato(dato) for dato in Tid_norsknormaltid]
Trykk_absolutt = [float(x) * 10 for x in Trykk_absolutt]


aligned_dates = []
aligned_barometer = []
for date, barometer in zip(konverterte_datoer, Trykk_barometer):
    if barometer is not None:  # Check if barometer is not None
        try:
            # Convert the barometer value to a float
            aligned_barometer.append(float(barometer))  # Ensure conversion to float
            aligned_dates.append(date)  # Append the corresponding date
        except ValueError:
            continue 
aligned_barometer = [float(x) * 10 for x in aligned_barometer]

aligned_normaltid = []
aligned_lufttrykk = []

for date, lufttrykk in zip(konvertert_normaltid, Lufttrykk):
    if date is not None and lufttrykk is not None:
        aligned_normaltid.append(date)
        aligned_lufttrykk.append(float(lufttrykk))



# Function to convert a list of datetime objects to a uniform string format
def format_datetimes(datetimes):
    # Desired output format
    desired_format = "%Y-%m-%d %H:%M"
    
    # Convert each datetime object to the desired format
    formatted_dates = [dt.strftime(desired_format) for dt in datetimes]
    
    return formatted_dates

formatted_list1 = format_datetimes(konverterte_datoer)
formatted_list2 = format_datetimes(aligned_dates)
formatted_list3 = format_datetimes(aligned_normaltid)








plt.figure(figsize=(12, 6))

plt.plot(formatted_list1, Trykk_absolutt, color='blue', label='Absolutt Trykk')
plt.plot(formatted_list2,aligned_barometer, color='orange', label='Barometer Trykk')
plt.plot(formatted_list3,aligned_lufttrykk)



plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=7))
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=7))
plt.xticks(rotation=45)


# Display the plot
plt.show()