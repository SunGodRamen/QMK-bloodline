import json
from finger_networks import (
    euclidean_distance,
    create_key_coordinates,
    create_key_distances,
    create_finger_networks,
    print_finger_networks,
)

# Load sample layout
with open("data/sample-layout.json", "r") as layout_file:
    layout_data = json.load(layout_file)

# Load sample finger assignments
with open("data/sample-finger-assignments.json", "r") as finger_assignments_file:
    finger_assignments_data = json.load(finger_assignments_file)

# Create key coordinates
key_coordinates = create_key_coordinates(layout_data["layout"])

# Create key distances
key_distances = create_key_distances(key_coordinates)

# Create finger networks
finger_networks = create_finger_networks(finger_assignments_data, key_distances)

# Print finger networks
print_finger_networks(finger_networks)
