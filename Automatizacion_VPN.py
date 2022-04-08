# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 08:41:49 2022

@author: gregorio.diaz
"""



from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import time
Forti="C:\Program Files\Fortinet\FortiClient\FortiClient.exe"
Escritorio='C:/WINDOWS/system32/mstsc.exe'


def Conexion_app(ruta,identificador):
    
    app = Application(backend="uia").start(ruta,timeout=10)
    time.sleep(5)
    app.windows()
#    print('exito en conexion')
    dlg = app[identificador]
#    dlg.print_control_identifiers()
    return (app,dlg)
def Ingresar_contra(ventana):
    ventana.type_keys('{TAB}{TAB}{TAB}')
    time.sleep(2)
    ventana.type_keys("Proyectos2021*{+}")
    time.sleep(2)
    ventana.type_keys('{ENTER}')
    time.sleep(15)
    return('conraseña puesta')

win,app_forti=Conexion_app(Forti,'FortiClient')
app_forti.type_keys('{TAB}{ENTER}')
time.sleep(10)
win.kill(soft=False)

win,app_forti=Conexion_app(Forti,'FortiClient')
#Envio contraseña  y enter
Ingresar_contra(app_forti)
print("Conexion VPN Exitosa")
win.kill(soft=False)


win,app_escritorio=Conexion_app(Escritorio,'Conexión a Escritorio remoto')
time.sleep(2)
app_escritorio.type_keys("10.10.100.22")
app_escritorio.type_keys('{ENTER}')
print("Se conecta a escritorio remoto." )



