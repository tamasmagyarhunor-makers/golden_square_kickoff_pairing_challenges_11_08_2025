from lib.pokemon_store import PokemonStore
# DONE the PokemonStore should be able to store pokemons (strings: ["pikachu", "raichu"])
# DONE should be able to add pokemons
# DONE should be able to list pokemons

def test_pokemon_instantiates():
    # setup
    poke_store = PokemonStore()

    # assertion
    assert poke_store.room == []

def test_pokemon_adds_a_new_pokemons():
    # setup
    poke_store = PokemonStore()

    # action
    poke_store.add("pikachu")
    poke_store.add("charmander")

    # assertion
    assert poke_store.room == ["pikachu", "charmander"]

def test_show_list_of_pokemons():
    # setup
    poke_store = PokemonStore()

    # action
    poke_store.add("pikachu")
    poke_store.add("charmander")

    # assertion
    assert poke_store.show_pokemons() == ["pikachu", "charmander"]

