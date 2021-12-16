#normal list
number_grid = [
    1,2,3
]

#nested... list in list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1]) #row and column

for row in number_grid:
    print(row) #prints the grid as it is

for row in number_grid:
    for col in row:
        print(col) #prints each value 1 by 1