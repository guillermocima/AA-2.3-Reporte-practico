jugadores = [
    {"nombre": "Brandon", "edad":22},
    {"nombre": "Alana", "edad":23},
    {"nombre": "Oso", "edad":24},
    {"nombre": "Kafai", "edad":25},
]

#Usar filter para obtener los jugadores mayores de 23 años
jugadores_mayores = list(filter(lambda jugador: jugador ["edad"] > 23, jugadores))

print(jugadores_mayores)