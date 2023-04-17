### Problem Statement
  Develop an algorithm to optimize the key layout of any QMK keyboard with a given key coordinates definition and finger assignment. The algorithm should minimize the total travel distance for all ten fingers, including thumbs, while typing a set of English text documents. The optimized layout should also cluster similar characters in the same grouping. The algorithm must take into account the possibility of layers when the key matrix cannot accommodate all ASCII keys in the base layer and assign an equivalent cost to layer-switching keys as shifted keys.

# Input
 - QMK key coordinates definition (a list of lists representing the key coordinates for each row and column) and finger assignment (a list of tuples representing the row and column indices for each finger) for a keyboard.
 - A directory of English text files to be used for evaluating the fitness of the keymaps.
 - Key matrix size (number of keys available in a single layer).
 - Layer-switching cost (an equivalent cost to a shifted key).

# Output
Top 5 performing keymaps after a specified number of iterations.

## Constraints
 - The algorithm should be adaptable to any QMK keyboard with a given key coordinates definition and finger assignment.
 - The cost of moving between keys is defined as the Euclidean distance between them.
 - The finger assignments should be taken into account while evaluating the layout.
 - If a finger moves between two keys that it is responsible for, the cost is the weight of the edge between the two keys in the finger network.
 - If a finger moves to a new key managed by a different finger, the cost is the weight of the edge between the two keys in the new finger's network, and the old finger is assumed to return to its home row position.
 - If the key matrix cannot accommodate all ASCII keys in the base layer, a layer key should be used, and the rest of the keys should be placed on the next layer. The layer-switching cost is assigned to the layer key.
 - The algorithm should consider layers when generating keymaps and calculating fitness scores.

### Implementation
 - Read the QMK key coordinates definition and finger assignment from an external source (e.g., a file or user input).
 - Generate μ random keymaps that contain all necessary character-producing keys, utilizing layers where required.
 - Analyze the text files using the fitness function to consider the finger assignments, the total travel distance between keys while typing the translated documents, and shift, and layer-switching costs.
 - Implement a genetic algorithm to optimize the keymaps through a specified number of iterations (Γ), performing selection, crossover, and mutation to create new generations of keymaps, ensuring the full ASCII character set is accessible in child keymaps.
 - Across the iterations, store the top N performing keymaps based on their fitness scores and return them as output at the end.

## Technologies
Python; DEAP library, Docker

# Format
```c
{
  "layout": [
    {"label": "1", "x": 0, "y": 0.93},
    {"label": "2", "x": 1, "y": 0.31},
    {"label": "3", "x": 2, "y": 0},
    {"label": "4", "x": 3, "y": 0.28},
    {"label": "5", "x": 4, "y": 0.42},

    {"label": "6", "x": 7, "y": 0.42},
    {"label": "7", "x": 8, "y": 0.28},
    {"label": "8", "x": 9, "y": 0},
    {"label": "9", "x": 10, "y": 0.31},
    {"label": "10", "x": 11, "y": 0.93},

    {"label": "11", "x": 0, "y": 1.93},
    {"label": "12", "x": 1, "y": 1.31},
    {"label": "13", "x": 2, "y": 1},
    {"label": "14", "x": 3, "y": 1.28},
    {"label": "15", "x": 4, "y": 1.42},

    {"label": "16", "x": 7, "y": 1.42},
    {"label": "17", "x": 8, "y": 1.28},
    {"label": "18", "x": 9, "y": 1},
    {"label": "19", "x": 10, "y": 1.31},
    {"label": "20", "x": 11, "y": 1.93},

    {"label": "21", "x": 0, "y": 2.93},
    {"label": "22", "x": 1, "y": 2.31},
    {"label": "23", "x": 2, "y": 2},
    {"label": "24", "x": 3, "y": 2.28},
    {"label": "25", "x": 4, "y": 2.42},

    {"label": "26", "x": 7, "y": 2.42},
    {"label": "27", "x": 8, "y": 2.28},
    {"label": "28", "x": 9, "y": 2},
    {"label": "29", "x": 10, "y": 2.31},
    {"label": "30", "x": 11, "y": 2.93},

    {"label": "31", "x": 3.5, "y": 3.75},
    {"label": "32", "x": 4.5, "y": 4},

    {"label": "33", "x": 6.5, "y": 4},
    {"label": "34", "x": 7.5, "y": 3.75}
  ]
}
```

```c
finger_assignments = {
    "left_pinky": ["1", "11", "21"],
    "left_ring": ["2", "12", "22"],
    "left_middle": ["3", "13", "23"],
    "left_index": ["4", "14", "24", "6", "16", "26"],
    "left_thumb": ["31", "32"],
    "right_thumb": ["33", "34"],
    "right_index": ["5", "15", "25", "7", "17", "27"],
    "right_middle": ["8", "18", "28"],
    "right_ring": ["9", "19", "29"],
    "right_pinky": ["10", "20", "30"]
}
```
