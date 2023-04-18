import sys
sys.path.append("..")
import string
import unittest
from app.population import min_layer_switches_required, generate_random_keymap, generate_initial_keymaps

class TestPopulation(unittest.TestCase):
    def test_min_layer_switches_required(self):
        self.assertEqual(min_layer_switches_required("123456789"), 12)
        with self.assertRaises(ValueError):
            min_layer_switches_required("A")
        with self.assertRaises(ValueError):
            min_layer_switches_required("ABC")
        with self.assertRaises(ValueError):
            min_layer_switches_required("")

    def test_generate_random_keymap(self):
        layers = 3
        available_keys = 30
        finger_assignments = {
            "0": ["1", "2", "3"],
            "1": ["4", "5", "6"],
            "2": ["7", "8", "9"],
            "3": ["10", "11", "12"],
            "4": ["13", "14", "15"],
            "5": ["16", "17", "18"],
            "6": ["19", "20", "21"],
            "7": ["22", "23", "24"],
            "8": ["25", "26", "27"],
            "9": ["28", "29", "30"]
        }
        keymap = generate_random_keymap(layers, available_keys, finger_assignments)
        self.assertEqual(len(keymap["layers"]), layers)
        for layer in keymap["layers"]:
            self.assertEqual(len(layer), available_keys + layers)

    def test_generate_initial_keymaps(self):
        mu = 10
        layers = 3
        available_keys = 30
        finger_assignments = {
            "0": ["1", "2", "3"],
            "1": ["4", "5", "6"],
            "2": ["7", "8", "9"],
            "3": ["10", "11", "12"],
            "4": ["13", "14", "15"],
            "5": ["16", "17", "18"],
            "6": ["19", "20", "21"],
            "7": ["22", "23", "24"],
            "8": ["25", "26", "27"],
            "9": ["28", "29", "30"]
        }
        keymaps = generate_initial_keymaps(mu, layers, available_keys, finger_assignments)
        self.assertEqual(len(keymaps), mu)
        for keymap in keymaps:
            self.assertEqual(len(keymap["layers"]), layers)
            for layer in keymap["layers"]:
                self.assertEqual(len(layer), available_keys + layers)

    def test_full_character_set(self):
        layers = 3
        available_keys = 30
        finger_assignments = {
            "0": ["1", "2", "3"],
            "1": ["4", "5", "6"],
            "2": ["7", "8", "9"],
            "3": ["10", "11", "12"],
            "4": ["13", "14", "15"],
            "5": ["16", "17", "18"],
            "6": ["19", "20", "21"],
            "7": ["22", "23", "24"],
            "8": ["25", "26", "27"],
            "9": ["28", "29", "30"]
        }
        keymap = generate_random_keymap(layers, available_keys, finger_assignments)

        unique_characters = set()
        for layer in keymap["layers"]:
            for char in layer:
                if char and char not in unique_characters:
                    unique_characters.add(char)

        expected_characters = set(string.printable[:-5])
        self.assertEqual(unique_characters, expected_characters)

if __name__ == '__main__':
    unittest.main()
