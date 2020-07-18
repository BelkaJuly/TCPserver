import socket
import re


def check_date(HH, MM, SS):
    """

    Функция определяет, нужно ли прибавить минуты и часы после округления
    """
    if round(float(SS), 1) >= 0:
        SS = '00.0'
        MM = str(int(MM) + 1)
        if len(MM) < 2:
            MM = '0' + MM
        if MM == '60':
            MM = '00'
            HH = str(int(HH) + 1)
            if len(HH) < 2:
                HH = '0' + HH
    return HH, MM, SS


# Задаем адрес сервера
SERVER_ADDRESS = ('localhost', 8686)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('server is running, please, press ctrl+c to stop')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("new connection from {address}".format(address=address))

    data = connection.recv(1024)

    match = re.search(r'\d{4}\s\w{2}\s\d{2}:[0-5][0-9]:[0-5][0-9][.]\d{3}\s\d{2}', str(data))
    if match:
        sport_number, id, time, group_number = map(str, match[0].split())
        hours, minutes, seconds = map(str, time.split(':'))
        if group_number == '00':
            HH, MM, SS = check_date(hours, minutes, seconds)
            print(f'спортсмен, нагрудный номер {sport_number} прошёл отсечку {id} в '
                  f'{HH}:{MM}:{SS}')
            connection.send(bytes('Your data was printed on a screen!', encoding='UTF-8'))
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(f'\nНомер участника - {sport_number}, id канала - {id}, часы - {hours}, '
                    f'минуты - {minutes}, секунды - {seconds}, номер группы - {group_number}')
        connection.send(bytes('Your data was written in logs.txt!', encoding='UTF-8'))
    else:
        connection.send(bytes('The input data is inappropriate!', encoding='UTF-8'))

    connection.close()
