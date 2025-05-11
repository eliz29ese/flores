import sys
import time
import os

def print_ascii_animation(file_path, delay=0.0000000000000000001):
    """
    Imprime un archivo ASCII carácter por carácter con una animación rápida
    
    Args:
        file_path (str): Ruta al archivo ASCII
        delay (float): Tiempo de espera entre caracteres (segundos)
    """
    try:
        # Limpiar la pantalla antes de comenzar
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Abrir y leer el archivo ASCII
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Imprimir carácter por carácter con una pequeña pausa
        for char in content:
            sys.stdout.write(char)
            sys.stdout.flush()  # Forzar la salida inmediata
            time.sleep(delay)
        
        print()
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{file_path}'")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    # Ruta al archivo ASCII
    ascii_file = "hbd.txt"
    
    # Verificar si el archivo existe
    if not os.path.exists(ascii_file):
        print(f"El archivo '{ascii_file}' no existe en la ubicación actual.")
        print(f"Ubicación actual: {os.getcwd()}")
        print("Por favor, verifica que el archivo esté en la misma carpeta que este script.")
    else:
        # Ejecutar la animación
        print_ascii_animation(ascii_file)




