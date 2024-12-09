

def import_data(file_path):
    column1 = []
    column2 = []
    with open(file_path, 'r') as file:
        for line in file:
            col1, col2 = line.split()
            column1.append(int(col1))
            column2.append(int(col2))
    return column1, column2

# Example usage
file_path = '2024/day-01/data.txt'
column1, column2 = import_data(file_path)

column1.sort()
column2.sort()

distance = []
for i in range(len(column1)):
    distance.append(abs(column1[i] - column2[i]))

print(sum(distance))

# Count occurrences of each element from column1 in column2
occurrences = {element: column2.count(element) for element in column1}
similarity = [key * value for key, value in occurrences.items() if value > 0]

print(sum(similarity))
