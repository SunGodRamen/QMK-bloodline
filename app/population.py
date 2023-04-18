import random
import math
import string
import json

def min_layer_switches_required(layout):
    num_keys = len(layout)
    
    if num_keys < 3:
        raise ValueError("Layout must have at least 3 keys to cover the required character set.")
    
    num_keys -= 1  # Subtract 1 to account for the layer modifier key
    all_ascii_symbols = "".join(chr(i) for i in range(32, 128))
    num_ascii_characters = len(all_ascii_symbols)  # This includes both upper and lowercase characters

    min_layer_switches = math.ceil(num_ascii_characters / num_keys)

    if min_layer_switches > 15:
        raise ValueError("Layout requires too many layer switches (more than 15), which is invalid.")
    
    return min_layer_switches

def generate_random_keymap(layers, available_keys, finger_assignments):
    characters = list(string.printable[:-5])

    # Assign characters to keys while maintaining the finger assignments
    assigned_keys = {}
    for finger, keys in finger_assignments.items():
        num_keys = len(keys)
        for key in keys:
            if not characters:
                break
            char = random.choice(characters)
            characters.remove(char)
            assigned_keys[key] = {'char': char, 'layer': 0}

    # Assign the remaining characters to layers 1 and above
    for layer in range(1, layers):
        for key in assigned_keys:
            if not characters:
                break
            char = random.choice(characters)
            characters.remove(char)
            assigned_keys[key]['char'] += char

    # Generate the layers with assigned characters and layer-switching keys
    layers_list = []
    for layer in range(layers):
        layer_chars = [""] * available_keys
        for key in assigned_keys:
            index = int(key) - 1
            if layer < len(assigned_keys[key]['char']):
                layer_chars[index] = assigned_keys[key]['char'][layer]
            else:
                layer_chars[index] = ""
        layer_switch_keys = [f"TO{i}" if i != layer else f"FROM{i-1}" for i in range(layers)]
        layers_list.append(layer_chars + layer_switch_keys)

    return {"layers": layers_list}

def print_keymaps(keymaps):
    for i, keymap in enumerate(keymaps[:5]):
      print(f"Keymap {i+1}:\n{json.dumps(keymap, indent=2)}\n")

def generate_initial_keymaps(mu, layers, available_keys, finger_assignments):
    keymaps = []
    for _ in range(mu):
        keymap = generate_random_keymap(layers, available_keys, finger_assignments)
        keymaps.append(keymap)
    print_keymaps(keymaps)
    return keymaps