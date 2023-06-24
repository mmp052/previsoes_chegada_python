import requests
from arrivals import Arrivals

class TubeStop:
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
                for tube in data:
                    mode = tube['modeName']
                    if mode == 'tube':
                        self.name = tube['stationName']
                        self.arrivals.append(Arrivals(tube['destinationName'], tube['expectedArrival'], tube['lineName']))
                    else:
                        self.error = True
            else:
                self.error = True