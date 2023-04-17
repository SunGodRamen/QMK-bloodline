import random
import math
import string

def min_layer_switches_required(layout):
    num_keys = len(layout)
    
    if num_keys < 3:
        raise ValueError("Layout must have at least 3 keys to cover the required character set.")
    
    num_keys -= 1  # Subtract 1 to account for the layer modifier key
    all_ascii_symbols = "".join(chr(i) for i in range(32, 128))
    num_ascii_characters = len(all_ascii_symbols)  # This includes both upper and lowercase characters

    min_layer_switches = math.ceil((num_ascii_characters / 2) / num_keys)

    if min_layer_switches > 15:
        raise ValueError("Layout requires too many layer switches (more than 15), which is invalid.")
    
    return min_layer_switches



### WIP ---------

def assign_characters(layout, num_momentary_layers):
    all_ascii_symbols = "".join(chr(i) for i in range(32, 128))
    shift_label = "Shift"
    momentary_layer_labels = [f"ML{i}" for i in range(num_momentary_layers)]

    characters_and_actions = list(all_ascii_symbols) + [shift_label] + momentary_layer_labels

    assigned_keys = {}
    for key in layout:
        label = key["label"]
        assigned_key = random.choice(characters_and_actions)
        assigned_keys[label] = assigned_key

    return assigned_keys

def print_keymap(keymap):
    for key_label, assigned_key in keymap.items():
        print(f"{key_label}: {assigned_key}")

    layout = [...]  # Replace with your actual layout
    num_momentary_layers = 2  # Replace with the desired number of Momentary Layer switches
    keymap = assign_characters(layout, num_momentary_layers)
    print_keymap(keymap)