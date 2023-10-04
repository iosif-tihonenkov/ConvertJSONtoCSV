
import socket

#Создали серверный сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 3000))
#Заставляем сервер слушать входящие
server.listen(4)
print('Сервер запущен')
#Учим сервер принмать отправленные ему запросы и разделять его на клиента и адрес, с которого прилетел запрос
client_socket, address = server.accept()
#Получаем содержимое запроса с клиента
data = int(client_socket.recv(1024).decode('utf-8'))

#Возведение числа в квадрат
result = str(data**2)

#Отправляем данные клиенту
#То что хотим отправить
content = result.encode('utf-8')
#посылаем клиенту
client_socket.send(content)
#Сообщение об окончании работы сервера
print("Сервер закончил работу")