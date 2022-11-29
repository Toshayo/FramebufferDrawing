from ctypes import Structure, c_char, c_ulong, c_uint32, c_uint16


class FbFixScreeninfoStruct(Structure):
    FBIOGET_FSCREENINFO = 0x4602

    _fields_ = [
        ('id', c_char * 16),  # identification string eg "TT Builtin"
        ('smem_start', c_ulong),  # Start of frame buffer mem (physical address)
        ('smem_len', c_uint32),  # Length of frame buffer mem
        ('type', c_uint32),  # see FB_TYPE_*
        ('type_aux', c_uint32),  # Interleave for interleaved Planes
        ('visual', c_uint32),  # see FB_VISUAL_*
        ('xpanstep', c_uint16),  # zero if no hardware panning
        ('ypanstep', c_uint16),  # zero if no hardware panning
        ('ywrapstep', c_uint16),  # zero if no hardware ywrap
        ('line_length', c_uint32),  # length of a line in bytes
        ('mmio_start', c_ulong),  # Start of Memory Mapped I/O (physical address)
        ('mmio_len', c_uint32),  # Length of Memory Mapped I/O
        ('accel', c_uint32),  # Indicate to driver which specific chip/card we have
        ('capabilities', c_uint16),  # see FB_CAP_*
        ('reserved', c_uint16 * 2),  # Reserved for future compatibility
    ]
