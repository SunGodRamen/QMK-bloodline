import sys
sys.path.append("..")
import string
import unittest
from app.population import min_layer_switches_required, generate_random_keymap, generate_initial_keymaps

class TestPopulation(unittest.TestCase):
    
    @staticmethod
    def generate_test_finger_assignments():
        return {
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

    @staticmethod
    def generate_test_keymap(layers=4,available_keys=30):
        finger_assignments =  {
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
        return generate_random_keymap(layers, available_keys, finger_assignments)

    def test_min_layer_switches_required(self):
        self.assertEqual(min_layer_switches_required("123456789"), 12)
        with self.assertRaises(ValueError):
            min_layer_switches_required("A")
        with self.assertRaises(ValueError):
            min_layer_switches_required("ABC")
        with self.assertRaises(ValueError):
            min_layer_switches_required("")

    def test_generate_random_keymap(self):
        layers = 4
        available_keys = 30 
        keymap = self.generate_test_keymap(layers,available_keys);
        self.assertEqual(len(keymap["layers"]), layers)
        for layer in keymap["layers"]:
            self.assertEqual(len(layer), available_keys + layers)

    def test_generate_initial_keymaps(self):
        mu = 10
        layers=4
        available_keys=30
        finger_assignments = self.generate_test_finger_assignments()
        keymaps = generate_initial_keymaps(mu, layers, available_keys, finger_assignments)
        self.assertEqual(len(keymaps), mu)
        for keymap in keymaps:
            self.assertEqual(len(keymap["layers"]), layers)
            for layer in keymap["layers"]:
                self.assertEqual(len(layer), available_keys + layers)

    def test_full_character_set(self):
        keymap = self.generate_test_keymap();
        # Get unique characters from keymap, ignoring layer switch keys
        unique_characters = {char for layer in keymap["layers"] for char in layer if not char.startswith("TO") and not char.startswith("FROM")}
        # Get the set of expected characters
        expected_characters = set(string.printable[:-5])
        # Compare the sets
        self.assertEqual(unique_characters, expected_characters)

    def test_layer_switch_keys(self):
      layers = 3
      keymap = self.generate_test_keymap(3);

      for layer in keymap["layers"]:
          to_keys_count = {}
          from_keys_count = {}

          for key in layer:
              if key.startswith("TO"):
                  layer_num = int(key[2:])
                  to_keys_count[layer_num] = to_keys_count.get(layer_num, 0) + 1
              elif key.startswith("FROM"):
                  layer_num = int(key[4:])
                  from_keys_count[layer_num] = from_keys_count.get(layer_num, 0) + 1

          self.assertEqual(to_keys_count, from_keys_count)

          for layer_num in range(layers):
              if layer_num in to_keys_count:
                  self.assertEqual(to_keys_count[layer_num], 1)
                  self.assertEqual(from_keys_count[layer_num], 1)

    def get_shifted_character(self, char):
        if char.isdigit():
            return ")!@#$%^&*("[int(char)]
        elif char in string.ascii_lowercase:
            return char.upper()
        elif char in string.ascii_uppercase:
            return char.lower()
        else:
            # Add any other specific shifted character mappings here
            return None

    def test_shifted_characters(self):
        keymap = self.generate_test_keymap();

        first_layer = keymap["layers"][0]
        second_layer = keymap["layers"][1]

        for i, char in enumerate(first_layer):
            if char in string.ascii_lowercase:
                shifted_char = self.get_shifted_character(char)
                self.assertEqual(shifted_char, second_layer[i], f"Shifted character of {char} should be {shifted_char}, but got {second_layer[i]}")

if __name__ == '__main__':
    unittest.main()
