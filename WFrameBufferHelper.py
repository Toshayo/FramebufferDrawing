from fcntl import ioctl
from fb_structs.FbVarScreeninfoStruct import FbVarScreeninfoStruct


class WFrameBufferHelper:
    def __init__(self, fb):
        self.fb = fb

    def get_size(self):
        screen_info = FbVarScreeninfoStruct()
        ioctl(self.fb, FbVarScreeninfoStruct.FBIOGET_VSCREENINFO, screen_info)
        return screen_info.xres, screen_info.yres
