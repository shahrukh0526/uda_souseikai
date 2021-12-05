import socket
import random

START = 0


def game():
    print("ゲームスタート!")
    port = 5001
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.bind(('10.201.5.59', 5001))
    socket1.listen(1)
    clientsocket, address = socket1.accept()
    print(f"connect from {address}")
    # clientsocket.send("ゲームスタート!\n数値を入力してください".encode("utf-8"))
    clientsocket.send(START.to_bytes(6, 'big'))
    selectnum_range_flag = 0
    score = 0
    end = b'\x80'
    for i in range(10):
        correct = [random.randint(0, 50) for i in range(20)]
        miss = [random.randint(51, 99) for i in range(20)]
        cor_flag = 0
        miss_flag = 0
        prtcol_miss = 0
        number = clientsocket.recv(4096)[5]
        print(number)
        judge = b'\x01'
        # for cor in correct:
        #     if cor == number:
        #         cor_flag = 1
        # for ms in miss:
        #     if ms == miss:
        #         miss_flag = 1
        # if i >= 1:
        #     if selectnum_range_flag == 0 and 0 <= number < 50:
        #         prtcol_miss = 1
        #     if selectnum_range_flag == 1 and 50 <= number < 99:
        #         prtcol_miss = 1
        # if 0 <= number < 50:
        #     selectnum_range_flag = 0
        # elif 50 <= number <= 99:
        #     selectnum_range_flag = 1

        # if prtcol_miss == 1:
        #     score -= 30
        # else:
        #     if cor_flag == 1:
        #         score += 10
        #     elif miss_flag == 1:
        #         score -= 10
        #     else:
        #         score -= 1
        # if score < 0:
        #     score = 0
        # if score > 255:
        #     score = 255
        score += 10
        judge += score.to_bytes(1, 'little')
        if len(judge) < 8:
            for i in range(8-len(judge)):
                judge += b'\x00'
        # print(judge)
        clientsocket.send(judge)
        # else:
        #     clientsocket.send(END.to_bytes(6, 'big'))
    # number = clientsocket.recv(4096)
    # print(number)
    print(score)
    end += score.to_bytes(1, 'little')
    if len(end) < 8:
        for i in range(8-len(end)):
            end += b'\x00'
    clientsocket.send(end)
    clientsocket.close()
    socket1.close()
    print("終了")


if __name__ == '__main__':
    game()

# すべてクライアントに贈るけど、表示はさせないで、最後だけ全部出力sル
# todo
# 文字コードを数字にする
# 複数のクライアントでもできるように
# サーバーを立てる
