from machine import Pin
import time
import machine

# 定义GPIO引脚
# 控制1个电机
"""
p13 = Pin(13, Pin.OUT)
p12 = Pin(12, Pin.OUT)
# 控制1个电机
p14 = Pin(14, Pin.OUT)
p27 = Pin(27, Pin.OUT)
# 控制1个电机
p15 = Pin(15, Pin.OUT)
p2 = Pin(2, Pin.OUT)
# 控制1个电机
p4 = Pin(4, Pin.OUT)
p16 = Pin(16, Pin.OUT)
"""
p13_pwm = machine.PWM(machine.Pin(13))  # 设置13号引脚为PWM输出
p12_pwm = machine.PWM(machine.Pin(12))  # 设置12号引脚为PWM输出
p14_pwm = machine.PWM(machine.Pin(14))  # 设置14号引脚为PWM输出
p27_pwm = machine.PWM(machine.Pin(27))  # 设置27号引脚为PWM输出
p15_pwm = machine.PWM(machine.Pin(15))  # 设置15号引脚为PWM输出
p2_pwm = machine.PWM(machine.Pin(2))  # 设置2号引脚为PWM输出
p4_pwm = machine.PWM(machine.Pin(4))  # 设置4号引脚为PWM输出
p16_pwm = machine.PWM(machine.Pin(16))  # 设置16号引脚为PWM输出

"""
def move_left():
    p13.value(1)
    p12.value(0)
    p14.value(0)
    p27.value(1)
    p15.value(0)
    p2.value(1)
    p4.value(1)
    p16.value(0)
"""


def move_left(data):
    p13_pwm.duty(data)  # 设置13号引脚的占空比为50%（实际数值需要根据具体情况调整）
    p12_pwm.duty(0)  # 设置12号引脚的占空比为0%
    p14_pwm.duty(0)  # 设置14号引脚的占空比为0%
    p27_pwm.duty(data)  # 设置27号引脚的占空比为50%
    p15_pwm.duty(0)  # 设置15号引脚的占空比为0%
    p2_pwm.duty(data)  # 设置2号引脚的占空比为100%
    p4_pwm.duty(data)  # 设置4号引脚的占空比为100%
    p16_pwm.duty(0)  # 设置16号


"""
def move_right():
    p13.value(0)
    p12.value(1)
    p14.value(1)
    p27.value(0)
    p15.value(1)
    p2.value(0)
    p4.value(0)
    p16.value(1)
"""


def move_right(data):
    p13_pwm.duty(0)  # 设置13号引脚的占空比为50%（实际数值需要根据具体情况调整）
    p12_pwm.duty(data)  # 设置12号引脚的占空比为0%
    p14_pwm.duty(data)  # 设置14号引脚的占空比为0%
    p27_pwm.duty(0)  # 设置27号引脚的占空比为50%
    p15_pwm.duty(data)  # 设置15号引脚的占空比为0%
    p2_pwm.duty(0)  # 设置2号引脚的占空比为100%
    p4_pwm.duty(0)  # 设置4号引脚的占空比为100%
    p16_pwm.duty(data)  # 设置16号


"""
def move_up():
    p13.value(1)
    p12.value(0)
    p14.value(1)
    p27.value(0)
    p15.value(1)
    p2.value(0)
    p4.value(1)
    p16.value(0)
"""


def move_up(data):
    p13_pwm.duty(data)  # 设置13号引脚的占空比为50%（实际数值需要根据具体情况调整）
    p12_pwm.duty(0)  # 设置12号引脚的占空比为0%
    p14_pwm.duty(data)  # 设置14号引脚的占空比为0%
    p27_pwm.duty(0)  # 设置27号引脚的占空比为50%
    p15_pwm.duty(data)  # 设置15号引脚的占空比为0%
    p2_pwm.duty(0)  # 设置2号引脚的占空比为100%
    p4_pwm.duty(data)  # 设置4号引脚的占空比为100%
    p16_pwm.duty(0)


"""
def move_down():
    p13.value(0)
    p12.value(1)
    p14.value(0)
    p27.value(1)
    p15.value(0)
    p2.value(1)
    p4.value(0)
    p16.value(1)
"""


def move_down(data):
    p13_pwm.duty(0)  # 设置13号引脚的占空比为50%（实际数值需要根据具体情况调整）
    p12_pwm.duty(data)  # 设置12号引脚的占空比为0%
    p14_pwm.duty(0)  # 设置14号引脚的占空比为0%
    p27_pwm.duty(data)  # 设置27号引脚的占空比为50%
    p15_pwm.duty(0)  # 设置15号引脚的占空比为0%
    p2_pwm.duty(data)  # 设置2号引脚的占空比为100%
    p4_pwm.duty(0)  # 设置4号引脚的占空比为100%
    p16_pwm.duty(data)


"""
def stop():
    p13.value(0)
    p12.value(0)
    p14.value(0)
    p27.value(0)
    p15.value(0)
    p2.value(0)
    p4.value(0)
    p16.value(0)

"""


def stop():
    p13_pwm.duty(0)  # 设置13号引脚的占空比为50%（实际数值需要根据具体情况调整）
    p12_pwm.duty(0)  # 设置12号引脚的占空比为0%
    p14_pwm.duty(0)  # 设置14号引脚的占空比为0%
    p27_pwm.duty(0)  # 设置27号引脚的占空比为50%
    p15_pwm.duty(0)  # 设置15号引脚的占空比为0%
    p2_pwm.duty(0)  # 设置2号引脚的占空比为100%
    p4_pwm.duty(0)  # 设置4号引脚的占空比为100%
    p16_pwm.duty(0)


"""
while True:
    a = int(input())
    move_left(a)
'''
# move_up()
# stop()

"""

