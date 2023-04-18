import sys
sys.path.append("..")
import unittest
from app.finger_networks import euclidean_distance, create_key_coordinates, create_key_distances, create_finger_networks

class TestEuclideanDistance(unittest.TestCase):
    def test_euclidean_distance(self):
        coord1 = (0, 0)
        coord2 = (3, 4)
        expected_distance = 5.0
        actual_distance = euclidean_distance(coord1, coord2)
        self.assertEqual(expected_distance, actual_distance)

class TestCreateKeyCoordinates(unittest.TestCase):
    def test_create_key_coordinates(self):
        layout = [
            {"label": "1", "x": 0, "y": 0},
            {"label": "2", "x": 3, "y": 4},
            {"label": "3", "x": 1, "y": 1},
        ]
        expected_coordinates = {
            "1": (0, 0),
            "2": (3, 4),
            "3": (1, 1),
        }
        actual_coordinates = create_key_coordinates(layout)
        self.assertEqual(expected_coordinates, actual_coordinates)

class TestCreateKeyDistances(unittest.TestCase):
    def test_create_key_distances(self):
        key_coordinates = {
            "1": (0, 0),
            "2": (3, 4),
            "3": (1, 1),
        }
        expected_distances = {
            ("1", "1"): 0.0,
            ("1", "2"): 5.0,
            ("1", "3"): 1.4142135623730951,
            ("2", "1"): 5.0,
            ("2", "2"): 0.0,
            ("2", "3"): 3.605551275463989,
            ("3", "1"): 1.4142135623730951,
            ("3", "2"): 3.605551275463989,
            ("3", "3"): 0.0,
        }
        actual_distances = create_key_distances(key_coordinates)
        self.assertEqual(expected_distances, actual_distances)

class TestCreateFingerNetworks(unittest.TestCase):
    def test_create_finger_networks(self):
        finger_assignments = {
            "left": ["1", "3"],
            "right": ["2"],
        }
        key_distances = {
            ("1", "1"): 0.0,
            ("1", "2"): 5.0,
            ("1", "3"): 1.4142135623730951,
            ("2", "1"): 5.0,
            ("2", "2"): 0.0,
            ("2", "3"): 3.605551275463989,
            ("3", "1"): 1.4142135623730951,
            ("3", "2"): 3.605551275463989,
            ("3", "3"): 0.0,
        }
        expected_networks = {
            "left": {
                ("1", "1"): 0.0,
                ("1", "3"): 1.4142135623730951,
                ("3", "1"): 1.4142135623730951,
                ("3", "3"): 0.0,
            },
            "right": {
                ("2", "2"): 0.0,
            },
        }
        actual_networks = create_finger_networks(finger_assignments, key_distances)
        self.assertEqual(expected_networks, actual_networks)

if __name__ == '__main__':
    unittest.main()