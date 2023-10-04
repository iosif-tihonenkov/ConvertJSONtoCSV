
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
data = client_socket.recv(1024).decode('utf-8')
#Вывод полученных данных в терминал
print(data)
#Отправляем данные клиенту
#Заголовок для браузера
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
#То что хотим отправить
content = 'Ответочка от сервера'.encode('utf-8')
#посылаем клиенту
client_socket.send(HDRS.encode('utf-8') + content)
#Сообщение об окончании работы сервера
print("Сервер закончил работу")