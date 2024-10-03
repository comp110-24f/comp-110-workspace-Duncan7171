# my_numbers: list[float] = []

# my_numbers.append(1.5)

# print(my_numbers)


game_points: list[int] = [102, 86, 94]

game_points[1] = 72

game_points.pop(1)

print(game_points)

print(len(game_points))


def display(Input: list[int]) -> None:
    index: int = 0
    while len(Input) > index:
        print(Input[index])
        index += 1


display(Input=game_points)
