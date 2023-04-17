import unittest
import sys
sys.path.append("..")
from app.population import min_layer_switches_required

class TestMinLayerSwitchesRequired(unittest.TestCase):
    def test_min_layer_switches_required(self):
        # Test case 1: a layout with 1 key
        layout1 = [{"label": "1", "x": 0, "y": 0}]
        with self.assertRaises(ValueError):
            min_layer_switches_required(layout1)

        # Test case 2: a layout with 30 keys (assuming a standard keyboard layout)
        layout2 = [{"label": f"{i}", "x": i % 10, "y": i // 10} for i in range(30)]
        result2 = min_layer_switches_required(layout2)
        expected2 = 2  # With 30 keys, we expect the function to return 3 layer switches
        self.assertEqual(result2, expected2)

        # Test case 3: a layout with 40 keys
        layout3 = [{"label": f"{i}", "x": i % 10, "y": i // 10} for i in range(40)]
        result3 = min_layer_switches_required(layout3)
        expected3 = 2  # With 40 keys, we expect the function to return 2 layer switches
        self.assertEqual(result3, expected3)

        # Test case 4: a layout with more than 15 layer switches
        layout4 = [{"label": f"{i}", "x": i % 10, "y": i // 10} for i in range(4)]
        with self.assertRaises(ValueError):
            min_layer_switches_required(layout4)

if __name__ == "__main__":
    unittest.main()
