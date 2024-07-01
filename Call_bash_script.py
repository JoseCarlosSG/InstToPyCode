"""import subprocess

# Ruta al script Bash
ruta_script_bash = './Git_branch_creation.sh'

# Argumentos para pasar al script Bash
argumentos = ['arg1', 'arg2']

# Ejecutar el script Bash desde Python
resultado = subprocess.run([ruta_script_bash] + argumentos, capture_output=True, text=True)

# Imprimir la salida del script Bash
print("Salida del script Bash:")
print(resultado.stdout)

# Imprimir el código de salida del script Bash
print("Código de salida:", resultado.returncode)"""

import subprocess

# Ruta al script de Bash
script_path = "C:/Users/jcsan/Documents/Repositories/APIs_project/Bash_script.sh"  # Reemplaza con la ruta correcta a tu script
param1 = "5"
param2 = "10"

# Usa Git Bash para ejecutar el script
try:
    result = subprocess.run(
        ["C:/Program Files/Git/bin/bash.exe", script_path, param1, param2],
        capture_output=True, text=True, check=True
    )
    # Imprime la salida del script Bash
    print("Resultado del script Bash:", result.stdout.strip())
except subprocess.CalledProcessError as e:
    print(f"El script Bash falló con el código de salida {e.returncode}")
    print(f"Errores:\n{e.stderr}")

# NOTE: Allow to execute script from python by chmod command:
# chmod +x Bash_script.sh


