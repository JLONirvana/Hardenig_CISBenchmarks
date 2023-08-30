import shutil
import subprocess
import sys
import time


class PolicyCopier:
    def __init__(self, ruta_origen, ruta_destino):
        # Atributos de la clase, se inicializan los parámetros
        self.ruta_origen = ruta_origen
        self.ruta_destino = ruta_destino

    def copy_policies_adm(self):
        """
        copia la platilla de las políticas en fomato .admx o .adml
        (la cual contiene la configuracion de las directivas)
        a la ruta del disco local C
        """

        try:
            shutil.copy2(self.ruta_origen, self.ruta_destino)
            print("el archivo se ha copiado de manera exitosa")
        except IOError as e:
            print("ocurrió un error al copiar el archivo :", e)

    @staticmethod
    def write_policies(ruta_lgpo, ruta_escritura):
        """
        funcion que realiza la escritura de las políticas
        mediante el cmd de windows
        """
        # Se usa un bloque try-except para capturar posibles excepciones
        try:
            subprocess.run(["cmd", "/c", ruta_lgpo, "/g", ruta_escritura])
            time.sleep(1)
        except FileNotFoundError as e:
            print("error al ejecutar el programa LGPO.exe o al encontrar la política " + ruta_escritura + ":", e)
            sys.exit()
