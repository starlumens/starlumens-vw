class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # (x, y) coordinates

    def update(self, world):
        pass  # Override in subclasses for custom behavior

class Player(Entity):
    def update(self, world):
        # Example: move randomly
        pass

class NPC(Entity):
    def update(self, world):
        # Example: NPC behavior
        pass

class GameWorld:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update(self)

    def render(self):
        # Placeholder: Print entities' positions
        for e in self.entities:
            print(f"{e.name} at {e.position}")

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
