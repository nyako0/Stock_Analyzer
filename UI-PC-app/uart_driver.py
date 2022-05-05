import serial

class UARTDriver:
    def __init__(self, com, frequency):
        self.ser = serial.Serial(com, frequency)

    def com_send(self, raw_data: list):
        ser = self.ser
        data = bytes(raw_data)
        ser.write(data)
        return data

    def com_read(self, n_bytes: int):
        ser = self.ser
        data_received = ser.read(n_bytes)
        return data_received


