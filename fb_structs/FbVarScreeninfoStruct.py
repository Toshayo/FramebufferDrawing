from ctypes import Structure, c_uint32

from fb_structs.BitfieldStruct import BitfieldStruct


class FbVarScreeninfoStruct(Structure):
    FBIOGET_VSCREENINFO = 0x4600
    FBIOPUT_VSCREENINFO = 0x4601

    _fields_ = [
        ('xres', c_uint32),  # visible resolution
        ('yres', c_uint32),
        ('xres_virtual', c_uint32),  # virtual resolution
        ('yres_virtual', c_uint32),
        ('xoffset', c_uint32),  # offset from virtual to visible
        ('yoffset', c_uint32),  # resolution

        ('bits_per_pixel', c_uint32),  # guess what
        ('grayscale', c_uint32),  # 0 = color, 1 = grayscale, >1 = FOURCC

        ('red', BitfieldStruct),  # bitfield in fb mem if true color,
        ('green', BitfieldStruct),  # else only length is significant
        ('blue', BitfieldStruct),
        ('transp', BitfieldStruct),  # transparency

        ('nonstd', c_uint32),  # != 0 Non standard pixel format

        ('activate', c_uint32),  # see FB_ACTIVATE_*

        ('height', c_uint32),  # height of picture in mm
        ('width', c_uint32),  # width of picture in mm

        ('accel_flags', c_uint32),  # (OBSOLETE) see fb_info.flags

        # Timing: All values, in pixclocks, except pixclock (of course)
        ('pixclock', c_uint32),  # pixel clock in ps (pico seconds)
        ('left_margin', c_uint32),  # time from sync to picture
        ('right_margin', c_uint32),  # time from picture to sync
        ('upper_margin', c_uint32),  # time from sync to picture
        ('lower_margin', c_uint32),
        ('hsync_len', c_uint32),  # length of horizontal sync
        ('vsync_len', c_uint32),  # length of vertical sync
        ('sync', c_uint32),  # see FB_SYNC_*
        ('vmode', c_uint32),  # see FB_VMODE_*
        ('rotate', c_uint32),  # angle we rotate counter clockwise
        ('colorspace', c_uint32),  # colorspace for FOURCC-based modes
        ('reserved', c_uint32 * 4),  # Reserved for future compatibility
    ]
