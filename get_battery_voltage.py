import smbus
import time

BQ25895_I2C_ADDRESS = 0x6A
BATTERY_VOLTAGE_REG = 0x0E

def read_register(bus, device_address, register):
    data = bus.read_word_data(device_address, register)
    return data

def hex_to_bin(hex_value, bits=8):
    return bin(hex_value)[2:].zfill(bits)

def get_battery_voltage(data):
    raw_vol = hex_to_bin(data)
    voltage = int(raw_vol[1]) * 1280  + int(raw_vol[2]) * 640 + int(raw_vol[3]) * 320 + int(raw_vol[4]) * 160 + int(raw_vol[5]) * 80 + int(raw_vol[6]) * 40 int(raw_vol[7]) * 20 + 2304
    return voltage

if __name__ == "__main__":
    bus = smbus.SMBus(1)

    try:
        value = bus.read_byte_data(BQ25895_I2C_ADDRESS, reg)
        print(get_battery_voltage(value))
    except Exception as e:
        print(f"Ошибка чтения регистра: {e}")

    finally:
        bus.close()
