def pyramid(rows):
    rows = int(rows)
    if rows <= 0:
        return 0
    return rows + pyramid(rows - 1)


print(pyramid(20))
