def hi_pokemons(pokemons):
    capitalized_pokemons = []
    for pokemon in pokemons:
        capitalized_pokemons.append(pokemon.capitalize())
    
    answer = f"Hi {', '.join(capitalized_pokemons)}!"
    return answer