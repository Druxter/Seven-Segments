# 0  = A, B, C, D, E, F     // G
# 1  = B, C                 // A D E F G
# 2  = A, B, D, E ,G        // C F
# 3  = A, B, C, D, G        // E F
# 4  = B, C, F, G           // A D E
# 5  = A, C, D, F, G        // B E
# 6  = A, C, D, E, F, G     // B
# 7  = A, B, C              // D E F G
# 8  = A, B, C, D, E, F, G  // 
# 9  = A, B, C, D, F, G     // E

segments = {
   #z: [A, B, C, D, E, F, G]
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}

patterns = [
            [
                ['#','#','#'],
                ['#',' ','#'],
                ['#',' ','#'],
                ['#',' ','#'],
                ['#','#','#'],
            ],
            [
                [' ','#',' '],
                [' ','#',' '],
                [' ','#',' '],
                [' ','#',' '],
                [' ','#',' '],
            ], 
            [
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
                ['#',' ',' '],
                ['#','#','#'],
            ],
            [
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
            ],
            [
                ['#',' ','#'],
                ['#',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                [' ',' ','#'],
            ],
            [
                ['#','#','#'],
                ['#',' ',' '],
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
            ],
            [
                ['#','#','#'],
                ['#',' ',' '],
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
            ],
            [
                ['#','#','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#'],
                [' ',' ','#'],
            ],
            [
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
            ],
            [
                ['#','#','#'],
                ['#',' ','#'],
                ['#','#','#'],
                [' ',' ','#'],
                ['#','#','#'],
            ]
        ]

def displaySevenSegments(inputNumber):
    if inputNumber in segments:
        for y in range(5):
            for x in range(3):
                print(patterns[inputNumber][y][x], end=" ")
            print()

        binary = format(inputNumber, '04b')
        print(f"\nBentuk Biner dari {inputNumber}: {binary}")

        segmentValue = segments[inputNumber]
        segemntLabels = ['A','B','C','D','E','F','G']
        print("\nSegment Values:")
        for label, value in zip(segemntLabels, segmentValue):
            print(f"{label}: {value}")

    else:
        print("Input tidak valid. Masukkan angka 0-9.")


inputNumber = int(input("Masukkan angka (0-9): "))

displaySevenSegments(inputNumber)