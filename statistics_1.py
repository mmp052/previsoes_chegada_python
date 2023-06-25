import csv
import datetime
import pytz

def average_waiting_time(lines, average_time, name):
    # Exportar dados para um arquivo CSV
    dados = zip(lines, average_time)
    nome_arquivo = f'{name}.csv'

    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Line', 'Average Waiting Time (minutes)'])  # Escrever o cabeçalho
        writer.writerows(dados)  # Escrever os dados

def calc_average(all_avererage_time):
    lines = []
    average_time = []

    for line in all_avererage_time:
        qnt = len(all_avererage_time[line])
        total = sum(all_avererage_time[line])
        lines.append(line)
        average_time.append(total//qnt)

    return lines, average_time

def make_csv(stops, type):
    all_average_time = {}

    time_zone = pytz.timezone('Europe/London')
    time_now = datetime.datetime.now(time_zone).strftime("%H:%M")

    # 1 == bus
    if type == 1:
        for stop in stops:
            if stop.arrivals:
                name = stop.name
                for arrival in stop.arrivals:
                    expectedArrival = arrival.expectedArrival[11:16]
                    if time_now[0:2] != expectedArrival[0:2]:
                        diff_H = abs(int(expectedArrival[0:2]) - int(time_now[0:2])) * 60
                        diff_M = abs(int(expectedArrival[3:]) - int(time_now[3:])) + diff_H
                    else:
                        diff_M = abs(int(expectedArrival[3:]) - int(time_now[3:]))

                    if arrival.lineName not in all_average_time:
                        all_average_time[arrival.lineName] = []

                    all_average_time[arrival.lineName].append(diff_M)

        lines, average_time = calc_average(all_average_time)

        average_waiting_time(lines, average_time, f'average_waiting_time_bus_{name}')
    
    # 2 == tube
    if type == 2:
        for stop in stops:
            if stop.arrivals:
                name = stop.name
                for arrival in stop.arrivals:
                    expectedArrival = arrival.expectedArrival[11:16]
                    if time_now[0:2] != expectedArrival[0:2]:
                        diff_H = abs(int(expectedArrival[0:2]) - int(time_now[0:2])) * 60
                        diff_M = abs(int(expectedArrival[3:]) - int(time_now[3:])) + diff_H
                    else:
                        diff_M = abs(int(expectedArrival[3:]) - int(time_now[3:]))

                    if arrival.lineName not in all_average_time:
                        all_average_time[arrival.lineName] = []

                    all_average_time[arrival.lineName].append(diff_M)

        lines, average_time = calc_average(all_average_time)

        average_waiting_time(lines, average_time, f'average_waiting_time_tube_{name}')
                    