import requests
from arrivals import Arrivals

class BusStop:
    def __init__(self, id):
        self.id = id
        self.arrivals = []
        self.error = False

        url = f'https://api.tfl.gov.uk/StopPoint/{self.id}/Arrivals'

        response = requests.get(url)

        if response.status_code == 200:
            # Obtendo os dados da resposta
            data = response.json()
            if data:
                for bus in data:
                    mode = bus['modeName']
                    if mode == 'bus':
                        self.name = bus['stationName']
                        self.arrivals.append(Arrivals(bus['destinationName'], bus['expectedArrival'], bus['lineName']))
                    else:
                        self.error = True
            else:
                self.error = True