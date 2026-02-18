# basic math using variables
player_health = 1000

# reduce by 100 here
player_health -= 100

print(player_health)

# and here
player_health -= 100
print(player_health)

# and here
player_health -= 100

print(player_health)

# and here
player_health -= 100

print(player_health)

# Create a new variable called armored_health on line 3 
# and set it equal to player_health multiplied by armor_multiplier.

player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier

print(armored_health)

# Fix the bugs to get the character report working!

"""
Run the code to see it fail.
Fix the syntax so that each variable is the data type you'd expect:
name: String
level: Integer
character_class: String
magic_resistance: Float (keep it equal to 15 but change it to a float)
account_active: Boolean
"""
name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")

