import ctypes       # permiten interactuar con la API de Windows y acceder a información del sistema
import sys          # permiten interactuar con la API de Windows y acceder a información del sistema
import subprocess

from write_CIS_Benchmarks import Hardening


def is_admin():
    """
    funcion para ejecutar python como administrador
    si en caso no es admin, no se realiza la ejecución
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def installed_program(program):
    """
    verifica si un programa dado está instalado
    en el SO windows
    """
    try:
        subprocess.check_output(["where", program], stderr=subprocess.STDOUT, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    if is_admin():
        opcion = 0
        while opcion != 7:
            print("    ")
            print("Ingrese la aplicacion o SO a hardenizar:")
            print("1. Adobe")
            print("2. Chrome")
            print("3. Edge")
            print("4. Office 365")
            print("5. SO Windows 10")
            print("6. SO Windows 11")
            print("7. Salir")
            opcion = int(input("Ingrese una opción :"))

            match opcion:
                case 1:
                    Hardening.hardening_adobe()
                    print("    ")
                    print("la optimizacion de Adobe fue exitosa")
                case 2:
                    Hardening.hardening_chrome()
                    print("    ")
                    print("la optimizacion de Crome fue exitosa")
                case 3:
                    Hardening.hardening_edge()
                    print("    ")
                    print("la optimizacion de Edge fue exitosa")
                case 4:
                    Hardening.hardening_office365()
                    print("    ")
                    print("la optimizacion de Edge fue exitosa")
                case 5:
                    Hardening.hardening_windows_10()
                    print("    ")
                    print("la optimizacion de Edge fue exitosa")
                case 6:
                    Hardening.hardening_windows_11()
                    print("    ")
                    print("la optimizacion de Edge fue exitosa")
                case 7:
                    print("    ")
                    print("Gracias ...")
                case _:
                    print("Opcio inválida, vuelve a ingresar")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)