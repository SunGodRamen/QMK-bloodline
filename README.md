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
 - Determine how many layers are necessary for the keymap to include all ascii characters from 32 (space) to 126 (~), considering the fact that a layer key uses one of the keys in the map and that a finger that is used to reach a layer cannot be used to produce a key on that layer
 - Generate μ random keymaps that contain all necessary character-producing keys, utilizing layers where required and appropriate.
 - Generate the weighted networks for the characters that each finger is assigned to using euclidean distance of the keys. Where a key is on a higher layer than base, the cost of the key is the travel distance of the layer key, plus the travel distance of the key.
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
```c
{
    "layers": [
        [
          "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "z", "x", "c", "v", "b", "n", "m", ",", "\\", "/", "TO3", " ", ".", "TO2"
        ],
        [
          "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "Z", "X", "C", "V", "B", "N", "M", ">", "|", "?", "TO3", " ", "<", "FROM2"
        ],
        [
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "\"", "'", "`", "~", "-", "_", "=", "+", "[", "]", "FROM3", "ENTER", " ", "TO2"
        ]
    ]
}
```

```c
{
  "left_pinky": {
    "1 - 1": 0.0,
    "1 - 11": 1.0,
    "1 - 21": 2.0,
    "11 - 1": 1.0,
    "11 - 11": 0.0,
    "11 - 21": 1.0,
    "21 - 1": 2.0,
    "21 - 11": 1.0,
    "21 - 21": 0.0
  },
  "left_ring": {
    "2 - 2": 0.0,
    "2 - 12": 1.0,
    "2 - 22": 2.0,
    "12 - 2": 1.0,
    "12 - 12": 0.0,
    "12 - 22": 1.0,
    "22 - 2": 2.0,
    "22 - 12": 1.0,
    "22 - 22": 0.0
  },
  "left_middle": {
    "3 - 3": 0.0,
    "3 - 13": 1.0,
    "3 - 23": 2.0,
    "13 - 3": 1.0,
    "13 - 13": 0.0,
    "13 - 23": 1.0,
    "23 - 3": 2.0,
    "23 - 13": 1.0,
    "23 - 23": 0.0
  },
  "left_index": {
    "4 - 4": 0.0,
    "4 - 14": 1.0,
    "4 - 24": 2.0,
    "4 - 6": 4.0,
    "4 - 16": 4.16,
    "4 - 26": 4.54,
    "14 - 4": 1.0,
    "14 - 14": 0.0,
    "14 - 24": 1.0,
    "14 - 6": 4.09,
    "14 - 16": 4.0,
    "14 - 26": 4.16,
    "24 - 4": 2.0,
    "24 - 14": 1.0,
    "24 - 24": 0.0,
    "24 - 6": 4.41,
    "24 - 16": 4.09,
    "24 - 26": 4.0,
    "6 - 4": 4.0,
    "6 - 14": 4.09,
    "6 - 24": 4.41,
    "6 - 6": 0.0,
    "6 - 16": 1.0,
    "6 - 26": 2.0,
    "16 - 4": 4.16,
    "16 - 14": 4.0,
    "16 - 24": 4.09,
    "16 - 6": 1.0,
    "16 - 16": 0.0,
    "16 - 26": 1.0,
    "26 - 4": 4.54,
    "26 - 14": 4.16,
    "26 - 24": 4.0,
    "26 - 6": 2.0,
    "26 - 16": 1.0,
    "26 - 26": 0.0
  },
  "left_thumb": {
    "31 - 31": 0.0,
    "31 - 32": 1.03,
    "32 - 31": 1.03,
    "32 - 32": 0.0
  },
  "right_thumb": {
    "33 - 33": 0.0,
    "33 - 34": 1.03,
    "34 - 33": 1.03,
    "34 - 34": 0.0
  },
  "right_index": {
    "5 - 5": 0.0,
    "5 - 15": 1.0,
    "5 - 25": 2.0,
    "5 - 7": 4.0,
    "5 - 17": 4.09,
    "5 - 27": 4.41,
    "15 - 5": 1.0,
    "15 - 15": 0.0,
    "15 - 25": 1.0,
    "15 - 7": 4.16,
    "15 - 17": 4.0,
    "15 - 27": 4.09,
    "25 - 5": 2.0,
    "25 - 15": 1.0,
    "25 - 25": 0.0,
    "25 - 7": 4.54,
    "25 - 17": 4.16,
    "25 - 27": 4.0,
    "7 - 5": 4.0,
    "7 - 15": 4.16,
    "7 - 25": 4.54,
    "7 - 7": 0.0,
    "7 - 17": 1.0,
    "7 - 27": 2.0,
    "17 - 5": 4.09,
    "17 - 15": 4.0,
    "17 - 25": 4.16,
    "17 - 7": 1.0,
    "17 - 17": 0.0,
    "17 - 27": 1.0,
    "27 - 5": 4.41,
    "27 - 15": 4.09,
    "27 - 25": 4.0,
    "27 - 7": 2.0,
    "27 - 17": 1.0,
    "27 - 27": 0.0
  },
  "right_middle": {
    "8 - 8": 0.0,
    "8 - 18": 1.0,
    "8 - 28": 2.0,
    "18 - 8": 1.0,
    "18 - 18": 0.0,
    "18 - 28": 1.0,
    "28 - 8": 2.0,
    "28 - 18": 1.0,
    "28 - 28": 0.0
  },
  "right_ring": {
    "9 - 9": 0.0,
    "9 - 19": 1.0,
    "9 - 29": 2.0,
    "19 - 9": 1.0,
    "19 - 19": 0.0,
    "19 - 29": 1.0,
    "29 - 9": 2.0,
    "29 - 19": 1.0,
    "29 - 29": 0.0
  },
  "right_pinky": {
    "10 - 10": 0.0,
    "10 - 20": 1.0,
    "10 - 30": 2.0,
    "20 - 10": 1.0,
    "20 - 20": 0.0,
    "20 - 30": 1.0,
    "30 - 10": 2.0,
    "30 - 20": 1.0,
    "30 - 30": 0.0
  }
}
```