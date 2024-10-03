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

datoer = ["2021-06-11", "2021-06-12"]

for dato in datoer:
    soloppgang, solnedgang = hent_sol_tider(dato)
    if soloppgang and solnedgang:
        # Konverterer ISO 8601-strengen til et datetime-objekt
        dt_soloppgang = datetime.fromisoformat(soloppgang)
        dt_solnedgang = datetime.fromisoformat(solnedgang)
        
        # Formaterer datetime-objektene til et mer lesbart format
        lesbar_soloppgang = dt_soloppgang.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        lesbar_solnedgang = dt_solnedgang.strftime("%Y-%m-%d %H:%M:%S %Z%z")
        
        print(f"Dato: {dato} - Soloppgang: {lesbar_soloppgang}, Solnedgang: {lesbar_solnedgang}")
    else:
        print(f"Kunne ikke hente sol tider for dato {dato}")
