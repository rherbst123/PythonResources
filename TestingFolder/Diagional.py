dimensions = [[8,6],[9,3]]

size = []

for dimension in dimensions:
    length, width = dimension
    diagonal = (length**2 + width**2)**0.5
    size.append(diagonal)

products = [dim[0] * dim[1] for dim in dimensions]
return max(products)

