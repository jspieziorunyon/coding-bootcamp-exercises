"""
We need to display on our players' screens what the most common enemy in a given area of the game map is.

Complete the get_most_common_enemy function by iterating over all enemies in the dictionary and returning only the name of the enemy with the highest count.

If there are no enemies, return the Python None value (not a string). If there are multiple enemies with the same highest count, return the first one found.

enemies_dict is a dictionary of name -> count. Example:

{
    "jackal": 1,
    "kobold": 2,
    "soldier": 3,
    "gremlin": 5
}
"""

def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_name = None

    for enemy in enemies_dict:
        if max_so_far < enemies_dict[enemy] or max_name is None:
            max_name = enemy
            max_so_far = enemies_dict[enemy]
    return max_name
        
