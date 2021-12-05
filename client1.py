import socket

port = 5000
server = ('10.201.6.58', 8000)
# server = (socket.gethostname(), port)

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(server)
msg = socket1.recv(4096)
print(msg)
print("数値を入力してください")
for i in range(10):
    number = int(input()).to_bytes(1, 'little')
    # print(number)
    number1 = b'\x00\x00\x00\x00\x00'+number
    print(number1)
    socket1.send(number1)
    judge = socket1.recv(4096)
    print(judge)
result = socket1.recv(4096)
print(result)
# msg = socket1.recv(4096).decode()
# print(msg)
# while True:
#     number = int(input())
#     socket1.send(number.to_bytes(6, 'big'))
#     break
socket1.close()
