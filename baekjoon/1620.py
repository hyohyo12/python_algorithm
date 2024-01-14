import sys
input = sys.stdin.readline

if __name__ == "__main__":
    pokemon = []
    pokemondict = {}
    n,m = map(int,input().split())
    for i in range(n):
        name = input().strip()
        pokemon.append(name)
        pokemondict[name] = i+1
    for i in range(m):
        quest = input().strip()
        if quest.isdigit():
            print(pokemon[int(quest)-1])
        else:
            print(pokemondict[quest])
    