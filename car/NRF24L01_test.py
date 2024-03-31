import ustruct as struct
import utime, time
from machine import Pin, SPI
from NRF24L01 import NRF24L01
from micropython import const
import MyCar

_RX_POLL_DELAY = const(15)

# ----------- 这里的代码变化了------start------------
cfg = {"spi": -1, "miso": 35, "mosi": 32, "sck": 33, "csn": 25, "ce": 26}
# ----------- 这里的代码变化了------stop------------

# Addresses are in little-endian format. They correspond to big-endian
# 0xf0f0f0f0e1, 0xf0f0f0f0d2
pipes = (b"\xe1\xf0\xf0\xf0\xf0", b"\xd2\xf0\xf0\xf0\xf0")

nrf = None


def call_back(*argc):
    print("有数据...")
    if nrf.any():
        while nrf.any():
            buf = nrf.recv()
            # ----------- 这里的代码变化了------start------------
            (move_direction, flag,) = struct.unpack("ii", buf)
            print("received: move_direction =", move_direction, "flag =", flag)
            # ----------- 这里的代码变化了------stop------------
            # move_direction = move_direction*2
            if flag == 0:
                MyCar.move_up(move_direction)
            elif flag == 1:
                MyCar.move_down(1023 - move_direction)
            elif flag == 2:
                MyCar.move_left(1023 - move_direction)
            elif flag == 3:
                MyCar.move_right(move_direction)
            utime.sleep_ms(_RX_POLL_DELAY)
    MyCar.stop()


def slave():
    global nrf

    p5 = Pin(34, Pin.IN)
    p5.irq(trigger=Pin.IRQ_FALLING, handler=call_back)

    csn = Pin(cfg["csn"], mode=Pin.OUT, value=1)
    ce = Pin(cfg["ce"], mode=Pin.OUT, value=0)

    spi = SPI(-1, sck=Pin(cfg["sck"]), mosi=Pin(cfg["mosi"]), miso=Pin(cfg["miso"]))
    nrf = NRF24L01(spi, csn, ce, payload_size=8)  # 修改 payload_size 的大小为 8 bytes

    nrf.open_tx_pipe(pipes[1])
    nrf.open_rx_pipe(1, pipes[0])
    nrf.stop_listening()
    nrf.start_listening()

    print("NRF24L01 slave mode, waiting for packets... (ctrl-C to stop)")

    while True:
        print("waiting ....")
        time.sleep(1)


slave()

