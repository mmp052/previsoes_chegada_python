import requests
from tube import TubeStop
from bus import BusStop
from statistics_1 import make_csv

tube_stops = []
bus_stops = []

while True:
    print('''1 para consultar uma estação de onibus
2 para consultar uma estação de metro
3 para sair''')

    opcao = int(input('Selecione uma opção: '))
    while not (opcao == 1 or opcao == 2 or opcao == 3):
        opcao = int(input('Selecione uma opção válida: '))

    tube_stops.clear()
    bus_stops.clear()

    if opcao == 1:
        station = input('Digite o nome da estação: ')
        url = f'https://api.tfl.gov.uk/StopPoint/Search?query={station}&modes=bus'
        response = requests.get(url)

        if response.status_code == 200:
            # Obtendo os dados da resposta
            data = response.json()
            
            # Iterando sobre as paradas de ônibus e exibindo os IDs
            if data['matches']:
                for stop in data['matches']:
                    stop_id = stop['id']
                    bus_stops.append(BusStop(stop_id))

                make_csv(bus_stops, 1)
                
                for bus_stop in bus_stops:
                    if not bus_stop.error:  
                        print(f'Estação {bus_stop.name}:')

                        if bus_stop.arrivals:
                            for arrival in bus_stop.arrivals:
                                print(f'\tÔnibus {arrival.lineName} para {arrival.destinationName}: Chegada esperada às {arrival.expectedArrival[11:16]}')
                        else:
                            print('Não foi possivel pegar as previsoes dessa estação')      
                    else:
                        print('Não foi possivel pegar as previsoes dessa estação')
                    
            else:
                print('Nenhuma parada encontrada na base de dados')

    if opcao == 2:
        station = input('Digite o nome da estação: ')
        url = f'https://api.tfl.gov.uk/StopPoint/Search?query={station}&modes=tube'
        response = requests.get(url)

        if response.status_code == 200:
            # Obtendo os dados da resposta
            data = response.json()
            
            # Iterando sobre as paradas de ônibus e exibindo os IDs
            if data['matches']:
                for stop in data['matches']:
                    stop_id = stop['id']
                    tube_stops.append(TubeStop(stop_id))
                
                make_csv(tube_stops, 2)

                for tube_stop in tube_stops:
                    if not tube_stop.error:
                        print(f'Estação {tube_stop.name}:')

                        if tube_stop.arrivals:
                            for arrival in tube_stop.arrivals:
                                print(f'\tTrem {arrival.lineName} para {arrival.destinationName}: Chegada esperada às {arrival.expectedArrival[11:16]}')
                        else:
                            print('Não foi possivel pegar as previsoes dessa estação')      
                    else:
                        print('Não foi possivel pegar as previsoes dessa estação')
                    
            else:
                print('Nenhuma parada encontrada na base de dados')
        
    if opcao == 3:
            break
        





# id_holborn_station = '940GZZLUHBN'

# Termo de pesquisa (pode ser o nome do ponto de ônibus, localização ou código de parada)
# search_term = 'holborn'

# bus_stop_ids = []

# URL da API para pesquisar paradas de ônibus
# url = f'https://api.tfl.gov.uk/StopPoint/Search?query={search_term}&modes=tube&app_id=&app_key={api_key}'

# Fazendo a solicitação à API
# response = requests.get(url)

# if response.status_code == 200:
#     # Obtendo os dados da resposta
#     data = response.json()
    
#     # Iterando sobre as paradas de ônibus e exibindo os IDs
#     for stop in data['matches']:
#         stop_id = stop['id']
#         stop_name = stop['name']
        
#         bus_stop_ids.append((stop_id, stop_name))
# else:
#     print('Não foi possível obter os pontos de ônibus.')

# for bus_stop_id in bus_stop_ids:

    # URL da API para obter os horários de chegada de ônibus
    # url = f'https://api.tfl.gov.uk/StopPoint/{bus_stop_id[0]}/Arrivals?app_id=&app_key={api_key}'

    # Fazendo a solicitação à API
    # response = requests.get(url)

    # if response.status_code == 200:
        # Obtendo os dados da resposta
        # data = response.json()

        
        # Iterando sobre os ônibus e exibindo os horários de chegada
    #     print(f'Estação {bus_stop_id[1]}:')
    #     for bus in data:
    #         mode = bus['modeName']
    #         line_name = bus['lineName']
    #         destination_name = bus['destinationName']
    #         expected_arrival = bus['expectedArrival']
            
    #         if mode == 'tube':
    #             print(f'\tÔnibus {line_name} para {destination_name}: Chegada esperada às {expected_arrival[11:16]}')
    # else:
    #     print('Não foi possível obter os horários de chegada dos ônibus.')


# from tfl.api_token import ApiToken
# from tfl.client import Client

# app_id = 'b74ffd5a96ec460d9dbfc4842427d01d'
# app_key = '865fab2ef35943fb91bfc7eeedcfcef1'

# token = ApiToken(app_id, app_key)
# client = Client(token)

# print(client.get_lines(mode='bus')[0])
# print(client.get_stop_points_by_line_id(line_id=1)[0])
# Itere sobre os pontos de ônibus e exiba as informações desejadas
# for bus in client.get_stop_points_by_mode(mode="bus"):
#     print(bus)
    # if rotas:
    #     id = bus.id
    #     print(f"ID: {id} | Rotas: {rotas}")