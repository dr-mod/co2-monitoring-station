import serial


class MHZ19b:

    CO2_CMD = bytearray(b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')

    def __init__(self):
        self.ser = serial.Serial('/dev/serial0', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

    def get_co2(self):
        self.ser.write(MHZ19b.CO2_CMD)
        response = bytearray(self.ser.read(9))
        if response[0] == 0xff and MHZ19b._calculate_crc(response) == response[8]:
            return MHZ19b._data_to_co2_level(response)
        else:
            return None

    @staticmethod
    def _calculate_crc(response):
        if len(response) != 9:
            return None
        crc = sum(response[1:8])
        return (~(crc & 0xff) & 0xff) + 1

    @staticmethod
    def _data_to_co2_level(data):
        return data[2] << 8 | data[3]

