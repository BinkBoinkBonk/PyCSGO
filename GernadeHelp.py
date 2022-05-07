import pymem
from pymem import Pymem, process, exception
import pymem.process
import re

pm = Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)

class ConVar():
    def __init__(self, name):
        try:
            self.address = 0
            interface_engine_cvar = 0x3E9EC
            vstdlib = process.module_from_name(pm.process_handle, 'vstdlib.dll').lpBaseOfDll
            v1 = pm.read_uint(vstdlib + interface_engine_cvar)
            v2 = pm.read_uint(pm.read_uint(pm.read_uint(v1 + 0x34)) + 0x4)
            while v2 != 0:
                if name == pm.read_string(pm.read_uint(v2 + 0x0C)):
                    self.address = v2
                    return
                # print(pm.read_string(pm.read_uint(a0 + 0x0C)))
                v2 = pm.read_uint(v2 + 0x4)
        except Exception as err:
            pass

    def set_int(self, value: int):
         pm.write_int(self.address + 0x30, value ^ self.address)
 
grenadepreview = ConVar('cl_grenadepreview')

grenadepreview.set_int(1)
