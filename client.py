import socket
import struct
import os

def send_file(sck: socket.socket, filename):
    #Получение размера файла
    filesize = os.path.getsize(filename)
    #Сообщаем серверу, сколько байт будет отправлено
    sck.sendall(struct.pack("<Q", filesize))
    #Отправка файла блоками по 1024 байта
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sck.sendall(read_bytes)
with socket.create_connection(('127.0.0.1', 3000)) as conn:
    print("Подключение к серверу")
    print("Передача файла...")
    send_file(conn, "example.json")
    print("Отправлено.")
print("Соединение закрыто.")