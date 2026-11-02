import os

def main():
    nombre = os.getenv("USERNAME", "Desconocido")
    lenguaje = os.getenv("LANGUAGE", "Desconocido")
    
    print(f"¡Hola, {nombre}! Tu lenguaje favorito es {lenguaje}.")

if __name__ == "__main__":
    main()
