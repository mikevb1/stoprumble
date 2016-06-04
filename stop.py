import ctypes


class XinputVibration(ctypes.Structure):
    _fields_ = [('wLeftMotorSpeed', ctypes.c_ushort),
                ('wRightMotorSpeed', ctypes.c_ushort)]

xinput = ctypes.windll.xinput1_1
xinput.XInputSetState(0, ctypes.byref(XinputVibration(0, 0)))
