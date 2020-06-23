# Import libraries
from adafruit_servokit import ServoKit
import board
import busio
import adafruit_pca9685

# Define the i2c bus on SDA and SCL
i2c = busio.I2C(board.SCL, board.SDA)

# PWM board 0 has address 64 (hex 40)
board0 = adafruit_pca9685.PCA9685(
    i2c, address=64, reference_clock_speed=25000000)

# PWM board 1 has address 65 (hex 41)
board1 = adafruit_pca9685.PCA9685(
    i2c, address=65, reference_clock_speed=25000000)

# Set PWM board frequency to 60
board0.frequency = 60
board1.frequency = 60

def setPWMBoard(board, id, pwm):
    if board == 0:
        # Board 0 PWM output control
        board0.channels[id].duty_cycle = pwm
    elif board == 1:
        # Board 1 PWM output control
        board1.channels[id].duty_cycle = pwm
    else:
        pass
