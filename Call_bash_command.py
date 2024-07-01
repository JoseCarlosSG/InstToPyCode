import subprocess

# Define el comando que quieres ejecutar
comando = "echo 'Hola, mundo!'"

# Ejecuta el comando
resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

# Imprime la salida
print("Salida:\n", resultado.stdout)
print("Errores:\n", resultado.stderr)
