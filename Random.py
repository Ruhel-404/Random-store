import struct

def check_device_bit():
    if struct.calcsize("P") * 8 == 64:
        import R.so
#        print("You module imported.")
    elif struct.calcsize("P") * 8 == 32:
        print("Device not supported.")
    else:
        print("Unknown architecture.")

check_device_bit()
