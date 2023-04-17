def euclidean_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def create_key_coordinates(layout):
    key_coordinates = {}
    for key in layout:
        label = key["label"]
        x = key["x"]
        y = key["y"]
        key_coordinates[label] = (x, y)
    return key_coordinates

def create_key_distances(key_coordinates):
    key_distances = {}
    for key1, coord1 in key_coordinates.items():
        for key2, coord2 in key_coordinates.items():
            key_distances[(key1, key2)] = euclidean_distance(coord1, coord2)
    return key_distances

def create_finger_networks(finger_assignments, key_distances):
    finger_networks = {}
    for finger, assigned_keys in finger_assignments.items():
        network = {}
        for key1 in assigned_keys:
            for key2 in assigned_keys:
                network[(key1, key2)] = key_distances[(key1, key2)]
        finger_networks[finger] = network
    return finger_networks

def print_finger_networks(finger_networks):
    for finger, network in finger_networks.items():
        print(f"{finger}:")
        for (key1, key2), distance in network.items():
            print(f"  {key1} - {key2}: {distance:.2f}")
        print()
