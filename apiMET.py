import requests
from datetime import datetime


#Henter data fra API-en til met.no, bruker koordinatene til Sola Værstasjon.
def hent_sol_tider(dato):
    url = f"https://api.met.no/weatherapi/sunrise/3.0/sun?lat=58.8766&lon=5.6370&date={dato}&offset=+02:00"
    headers = {
        'User-Agent': 'MinUnikeApp/1.0 (minemail@eksempel.com)'  # Bytt ut med din egen unike identifikator
    }
    response = requests.get(url, headers=headers)
    
    try:
        data = response.json()
        soloppgang = data['properties']['sunrise']['time']
        solnedgang = data['properties']['sunset']['time']
        return soloppgang, solnedgang
    except ValueError as e:
        print(f"Feil ved dekoding av JSON for dato {dato}: {e}")
        print(f"Innhold i responsen: {response.text}")
        return None, None
    except KeyError as e:
        print(f"KeyError for dato {dato}: {e}")
        print(f"Innhold i responsen: {data}")
        return None, None



def solData():
    solOpp = datetime.fromisoformat(hent_sol_tider("2021-06-12")[0])
    solNed = datetime.fromisoformat(hent_sol_tider("2021-06-11")[1])
    return solOpp, solNed

 