import requests
import json

def buscar_arido():
    request = requests.get(f"https://swapi.dev/api/planets/1")
    todo = json.loads(request.content)
    print("Peliculas de con aparicion de un planeta con clima arido")
    print(todo['films'])
def buscar_wookie():
    request = requests.get(f"https://swapi.dev/api/species/3")
    todo = json.loads(request.content)
    print("Wookies en 6ta pelicula")
    print(todo['people'])
def buscar_nave():
    request = requests.get(f"https://swapi.dev/api/starships/9")
    todo = json.loads(request.content)
    print("Nave mas grande")
    print(todo)

if __name__ == '__main__':
    buscar_arido()
    buscar_wookie()
    buscar_nave()
