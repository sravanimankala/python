#nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])
print(matrix[2][0])
print(matrix[0][2])
print(matrix[2][0])

#list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)