# StarLumens Game World Basic Framework

A simple, extensible Python framework for building a virtual game world.  
Includes basic architecture for a game world, entities (players, NPCs), and a minimal game loop.

## Features

- Modular structure for easy extension
- Core classes: `GameWorld`, `Entity`, `Player`, `NPC`
- Example main loop
- Ready for unit testing

## Getting Started

1. **Install requirements (if any):**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game loop:**
   ```bash
   python main.py
   ```

3. **Run tests:**
   ```bash
   python -m unittest discover tests
   ```

## Folder Structure

```
game-world-framework/
├── main.py
├── game/
│   ├── world.py
│   ├── entity.py
│   ├── player.py
│   └── npc.py
└── tests/
    └── test_game.py
```

## Extending

- Add new entity types by subclassing `Entity`
- Expand world logic in `world.py`
- Add new features in the `game/` directory

---

© 2025 Your Name
