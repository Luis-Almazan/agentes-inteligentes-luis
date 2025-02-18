import random

def recomendar_pelicula():
    peliculas = {
        "Acción": ["Mad Max: Fury Road", "John Wick", "Gladiador", "Die Hard"],
        "Comedia": ["Superbad", "The Hangover", "Dumb and Dumber", "Step Brothers"],
        "Drama": ["Forrest Gump", "The Shawshank Redemption", "The Green Mile", "Fight Club"],
        "Ciencia Ficción": ["Interstellar", "Blade Runner 2049", "The Matrix", "Inception"],
        "Terror": ["The Conjuring", "It", "A Nightmare on Elm Street", "Halloween"]
    }
    
    print("Seleccione su género favorito de la lista:")
    generos = list(peliculas.keys())
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero}")
    
    seleccion = input("Ingrese el número de su género favorito: ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(generos):
            genero_elegido = generos[seleccion - 1]
            pelicula_recomendada = random.choice(peliculas[genero_elegido])
            print(f"Recomendación: {pelicula_recomendada} ({genero_elegido})")
        else:
            print("Selección no válida. Intente de nuevo.")
    else:
        print("Entrada no válida. Intente de nuevo.")

if __name__ == "__main__":
    recomendar_pelicula()
