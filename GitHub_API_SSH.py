"""
requests no puede directamente usar SSH para comunicarse con APIs web. 
La biblioteca requests se usa para realizar solicitudes HTTP, mientras 
que SSH es un protocolo de red para acceder y transferir archivos de 
manera segura entre computadoras en red.

Sin embargo, puedes configurar un túnel SSH para redirigir el tráfico 
HTTP a través de una conexión SSH. Esto es útil si necesitas acceder 
a una API que está detrás de un firewall o en una red privada.

Uso de Proxies con requests
Otra opción es utilizar proxies si estás trabajando con servicios que 
requieren pasar por proxies específicos

"""
import requests

proxies = {
    "http": "http://localhost:9000",
    "https": "http://localhost:9000",
}

url = "https://api.github.com/repos/tu_usuario/mi_api"
response = requests.get(url, proxies=proxies)

if response.status_code == 200:
    data = response.json()
    print(f"Nombre del repositorio: {data['name']}")
    print(f"Descripción: {data['description']}")
    print(f"URL: {data['html_url']}")
else:
    print(f"Error: {response.status_code}")

