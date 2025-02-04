# SBUS_Generator 

pythonを使って、シリアル通信でSBUSを送るコードです

受信機が必要なデバックを簡易的に実行することができます

## 実行環境

・python 3.12.4

・pyserial 3.5

> [!NOTE]
> 少し古い環境で実行していますが、pyserialが対応していればどのバージョンでも動かせます

## 使い方

・使用するポートを選択する

```py
# "com5"の部分を変更してください
ser = serial.Serial('com5', baudrate=100000, parity=serial.PARITY_EVEN, stopbits=2, timeout=1)
```
・USB等を接続し、プログラムを実行する`

・ WASDなどのキーボード操作を行い、値を調整しつつ送信する

> [!WARNING]
> #### 実際の受信機との違い
> 
> 信号の反転を行っていません
> (Not回路などの信号の反転を外して使ってください）

## 操作方法

・W/S channel 2

・A/D channel 1

・Q/E channel 6

・J/L channel 0

・R   reset

値は 0 <= value <= 2000 の範囲になります

> [!WARNING]
> #### 勢いよく値が変わるので、モータテストの際には値の増える速度を調整してください
> 
