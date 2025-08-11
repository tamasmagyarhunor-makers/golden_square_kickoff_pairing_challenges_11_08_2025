from lib.hi_pokemons import hi_pokemons

def test_pokemon_takes_list_of_pokemons_and_returns_them_saying_hi():
    pokemons = ['pikachu', 'mewtwo', 'bulbasaur']
    assert hi_pokemons(pokemons) == "Hi Pikachu, Mewtwo, Bulbasaur!"
    # INPUT: hi_pokemons(['pikachu', 'mewtwo', 'bulbasaur'])
    # OUTPUT: "Hi Pikachu, Mewtwo, Bulbasaur!"