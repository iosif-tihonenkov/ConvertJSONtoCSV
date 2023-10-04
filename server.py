
import socket
#обозначили сокет, который потенциально может быть и клиентским и серверным
some_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Обозначаем сокет серверным. назначаем на него адреы