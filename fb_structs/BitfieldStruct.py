from ctypes import Structure, c_uint32


class BitfieldStruct(Structure):
    _fields_ = [
        ('offset', c_uint32),
        ('length', c_uint32),
        ('msb_right', c_uint32)
    ]
