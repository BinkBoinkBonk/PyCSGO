import pymem
import pymem.process
import requests


offsets = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get( offsets ).json()
m_fFlags = int( response["netvars"]["m_fFlags"] )
dwEntityList = int( response["signatures"]["dwEntityList"] )
dwGlowObjectManager = int( response["signatures"]["dwGlowObjectManager"] )
m_iGlowIndex = int( response["netvars"]["m_iGlowIndex"] )
m_iTeamNum = int( response["netvars"]["m_iTeamNum"] )
dwLocalPlayer = int( response["signatures"]["dwLocalPlayer"] )
def main():
    print('''                                                                                                                            
    __________               __      __      __        .__  .__          
    \______   \ ____   ____ |  | __ /  \    /  \_____  |  | |  |   ______
     |    |  _//  _ \ /    \|  |/ / \   \/\/   /\__  \ |  | |  |  /  ___/
     |    |   (  <_> )   |  \    <   \        /  / __ \|  |_|  |__\___ \ 
     |______  /\____/|___|  /__|_ \   \__/\  /  (____  /____/____/____  >
            \/            \/     \/        \/        \/               \/                                            
    ''')
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
##    class ConVar():
##        def __init__(self, name):
##            try:
##                self.address = 0
##                interface_engine_cvar = 0x3E9EC
##                vstdlib = process.module_from_name(pm.process_handle, 'vstdlib.dll').lpBaseOfDll
##                v1 = pm.read_uint(vstdlib + interface_engine_cvar)
##                v2 = pm.read_uint(pm.read_uint(pm.read_uint(v1 + 0x34)) + 0x4)
##                while v2 != 0:
##                    if name == pm.read_string(pm.read_uint(v2 + 0x0C)):
##                        self.address = v2
##                        return
##                    # print(pm.read_string(pm.read_uint(a0 + 0x0C)))
##                    v2 = pm.read_uint(v2 + 0x4)
##            except Exception as err:
##                pass
##
##        def set_int(self, value: int):
##             pm.write_int(self.address + 0x30, value ^ self.address)
##     
##    grenadepreview = ConVar('cl_grenadepreview')
##
##    grenadepreview.set_int(1)
    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))  # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow


if __name__ == '__main__':
    main()
