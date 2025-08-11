class PokemonStore:
    def __init__(self):
        self.room = []
    
    def add(self, pokemon):
        self.room.append(pokemon)
    
    def show_pokemons(self):
        return self.room