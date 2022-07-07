# Modifying Global Scope

enemies = 1

def increase_enemies_v1():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")

def increase_enemies_v2():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1

increase_enemies_v1()
enemies = increase_enemies_v2()
print(f"Enemies outside function: {enemies}")