from game.world import GameWorld
from game.player import Player
from game.npc import NPC

def main():
    world = GameWorld(width=10, height=10)
    player = Player("Hero", (5, 5))
    npc = NPC("Villager", (2, 3))
    world.add_entity(player)
    world.add_entity(npc)

    # Main game loop (simplified)
    for tick in range(5):
        print(f"--- Tick {tick} ---")
        world.update()
        world.render()

if __name__ == "__main__":
    main()
