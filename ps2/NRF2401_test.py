import ustruct as struct
import utime
from machine import Pin, SoftSPI
from NRF24L01 import NRF24L01


cfg = {"spi": -1, "miso": 17, "mosi": 16, "sck": 4, "csn": 2, "ce": 15}

# Addresses are in little-endian format. They correspond to big-endian
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")


def master():
    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)

    spi = SoftSPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
    nrf = NRF24L01(spi, csn, ce, payload_size=4)

    nrf.open_tx_pipe(pipes[0])
    nrf.open_rx_pipe(1, pipes[1])
    nrf.stop_listening()
    for i in range(100000):
        try:
            nrf.send(struct.pack("i", 3))  # 用0/1/2/3分表表示上下左右命令
        except OSError:
            pass


master()

