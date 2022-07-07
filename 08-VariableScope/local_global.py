# Scope

enemies = 1  # different enemy - GLOBAL


def increase_enemies():
    enemies = 2 # different enemy - LOCAL
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Global Scope
player_health = 10


def game():
    def drink_potion():
        # Local Scope
        potion_strength = 2
        print(f"Potion Strength: {potion_strength}")
        print(f"Player Health: {player_health}")

    drink_potion()

game()

# NameError
# drink_potion()

# NameError
# print(potion_strength)


# There is no block scope (IF ELSE)
game_level = 3


def create_enemy():
    enemies = ["Loki", "Ultron", "Thanos"]

    if game_level < 5:
        new_enemy = enemies[0]

    # no block scope
    print(new_enemy)

create_enemy()