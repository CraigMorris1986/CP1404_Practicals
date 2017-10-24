def pyramid(rows):
    try:
        rows = int(rows)
    except ValueError:
        print("rows must be a number (height of the pyramid)")
    if rows > 0:
        for row in range(rows):
            blocks = rows + pyramid(rows-1)
    else:
        blocks = 0
    return blocks

print(pyramid(5))
