import os 
from colorama import init, Fore, Style

# iniciamos colorama 
init (autoreset=True) 

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def imprimir_titulo(texto):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== {texto.upper()} === {Style.RESET_ALL}")
    
def imprimir_error(texto):
        print(f"{Fore.RED} ERROR: {texto}{Style.RESET_ALL}")
        
def imprimir_exito(texto):
    print(f"{Fore.GREEN} ÉXITO: {texto}{Style.RESET_ALL}")
    
def validar_input_string(prompt):
    while True:
        dato = input(f"{Fore.YELLOW}{prompt}: {Style.RESET_ALL}").strip() #ingresa el nombre del producto
        if dato:
            return dato
        imprimir_error("El campo no puede estar vacío. Inténtalo de nuevo.")
        
def validar_input_float(prompt):
    while True:
        try:
            dato = float(input(f"{Fore.YELLOW}{prompt}: {Style.RESET_ALL}"))
            if dato >= 0:
                return dato
            imprimir_error("El numero debe ser positivo")
        except ValueError:
            imprimir_error("El campo no tiene que ser un numero valido. Inténtalo de nuevo.")
           
def validar_input_int(prompt):
    while True:
        try:
            dato = int(input(f"{Fore.YELLOW}{prompt}: {Style.RESET_ALL}"))
            if dato >= 0:
                return dato
            imprimir_error("El numero debe ser positivo")
        except ValueError:
            imprimir_error("El campo no tiene que ser un numero entero valido. Inténtalo de nuevo.")