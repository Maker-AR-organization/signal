import ustruct as struct
import utime
from machine import Pin, SPI, ADC
from NRF24L01 import NRF24L01
import time

cfg = {"spi": -1, "miso": 17, "mosi": 16, "sck": 4, "csn": 2, "ce": 15}

# Addresses are in little-endian format. They correspond to big-endian
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")


def main():
    # PS2遥感配置相关
    ps2_y = ADC(Pin(33))
    ps2_y.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V
    ps2_x = ADC(Pin(32))
    ps2_x.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V
    btn = Pin(23, Pin.IN, Pin.PULL_UP)

    # NRF24L01发送相关
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)
    spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
    nrf = NRF24L01(spi, csn, ce, payload_size=8)
    nrf.open_tx_pipe(pipes[0])
    nrf.open_rx_pipe(1, pipes[1])
    nrf.stop_listening()

    while True:
        val_y = ps2_y.read()  # 0-4095
        val_x = ps2_x.read()  # 0-4095
        # print("x:{} y:{} btn:{} ".format(int(val_x/4), int(val_y/4), btn.value()))
        # time.sleep(0.1)
        val_y = int(val_y / 4)
        val_x = int(val_x / 4)
        move_num = -1

        if val_y > 500:
            move_num = val_y  # 0 前进
            flag = 0
            print("x:{} y:{} btn:{} flag:{}".format(val_x, val_y, btn.value(), flag))
        elif val_y < 480:
            move_num = val_y  # 1 后退
            flag = 1
            print("x:{} y:{} btn:{} flag:{}".format(val_x, val_y, btn.value(), flag))
        if val_x > 500:
            move_num = val_x  # 3
            flag = 3
            print("x:{} y:{} btn:{} flag:{}".format(val_x, val_y, btn.value(), flag))
        elif val_x < 480:
            move_num = val_x  # 2
            flag = 2
            print("x:{} y:{} btn:{} flag:{}".format(val_x, val_y, btn.value(), flag))
        if move_num != -1:
            try:
                nrf.send(struct.pack("ii", move_num, flag))  # 用0/1/2/3分表表示上下左右命令
            except OSError:
                pass


main()

