import RPi.GPIO as GPIO

class App(object):
    # 初始化
    def init (self):
        GPIO.setmode(GPIO.BOARD)

    def start (self):
        # 启动各类服务

    def stop (self):
        # 关闭服务

    # 销毁
    def destory(self):
        GPIO.cleanup()
