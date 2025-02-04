import serial
import time
import keyboard

# COM5の部分を使用するポートに合わせて変更
ser = serial.Serial('com5', baudrate=100000, parity=serial.PARITY_EVEN, stopbits=2, timeout=1)

# 送信データの初期化
data = [0] * 25 
control = [0] * 10

# 送信データの入力
control[0] = 1000
control[1] = 1000
control[2] = 1000
control[3] = 1000
control[4] = 1000
control[5] = 1000
control[6] = 500 #armのチャンネル
control[7] = 1000


# SBUSのデータe
# 11bitの符号なし整数をdataに格納

def convert_data():

    data[0] = 0x0F # ヘッダー
    data[1] = control[0] & 0xFF
    data[2] = ((control[0] >> 8) & 0x07) | ((control[1] & 0x1F) << 3)
    data[3] = ((control[1] >> 5) & 0x3F) | ((control[2] & 0x03) << 6)
    data[4] = (control[2] >> 2) & 0xFF
    data[5] = ((control[2] >> 10) & 0x01) | ((control[3] & 0x7F) << 1)
    data[6] = (control[3] >> 7) & 0x0F | ((control[4] & 0x0F) << 4)
    data[7] = ((control[4] >> 4) & 0x7F) | ((control[5] & 0x01) << 7)
    data[8] = (control[5] >> 1) & 0xFF
    data[9] = ((control[5] >> 9) & 0x03) | ((control[6] & 0x3F) << 2)
    data[10] = ((control[6] >> 6) & 0x1F) | ((control[7] & 0x07) << 5)
    data[11] = (control[7] >> 3) & 0xFF

    data[23] = 0x00 
    data[24] = 0x00 # フッター

def CheckKeybord():

    # armのチャンネル
    if keyboard.is_pressed('q'):

        control[6] = 500
        print("channel 6: 500")

    elif keyboard.is_pressed('e'):
        
        control[6] = 1500
        print("channel 6: 1500")

    # スロットルのチャンネル
    if keyboard.is_pressed('w'):

        if(control[2] < 2000):

            control[2] += 10
            print("channel 2:" + str(control[2]))

    elif keyboard.is_pressed('s'):
        
        if(control[2] > 0):

            control[2] -= 10
            print("channel 2:" + str(control[2]))

    # ロールのチャンネル
    if keyboard.is_pressed('a'):

        if(control[1] < 2000):

            control[1] += 10
            print("channel 1:" + str(control[1]))

    elif keyboard.is_pressed('d'):
        
        if(control[1] > 0):

            control[1] -= 10
            print("channel 1:" + str(control[1]))

    # ヨーのチャンネル
    if keyboard.is_pressed('j'):

        if(control[0] < 2000):

            control[0] += 10
            print("channel 0:" + str(control[0]))

    elif keyboard.is_pressed('l'):
        
        if(control[0] > 0):

            control[0] -= 10
            print("channel 0:" + str(control[0]))

    if keyboard.is_pressed('R'):

        control[0] = 1000
        control[1] = 1000
        control[2] = 1000
        control[3] = 1000
        control[4] = 1000
        control[5] = 1000
        control[6] = 500 #armのチャンネル
        control[7] = 1000

        print("Reset")

while(1):

    CheckKeybord() # キーボードの入力を確認

    convert_data() # データの変換

    ser.write(data) # 送信
    time.sleep(0.003)
