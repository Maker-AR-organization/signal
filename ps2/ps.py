from machine import Pin, ADC
import time


ps2_y = ADC(Pin(33))
ps2_y.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V
ps2_x = ADC(Pin(32))
ps2_x.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V


btn = Pin(23, Pin.IN,Pin.PULL_UP)

while True:
    val_y = ps2_y.read()  # 0-40+95
    val_x = ps2_x.read()  # 0-4095
    print("x:{} y:{} btn:{}".format(val_x, val_y, btn.value()))
    time.sleep(0.1)




