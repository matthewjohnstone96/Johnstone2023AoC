
def main(input_file: str):

    limits = {"red": 12, "green": 13, "blue": 14}
    with open(input_file, "r") as file:
        sum = 0
        minimums_sum = 0
        for line in file.readlines():
            game_string, game_rounds = line.split(":")
            game_int = int(game_string.split(" ")[1])
            game_rounds = game_rounds.split(";")
            game_rounds = [round.strip() for round in game_rounds]
            # fail_test = False
            minimums = {"red": 0, "green": 0, "blue": 0}
            for round in game_rounds:
                color_number_combos = round.split(",")
                for color_number_combo in color_number_combos:
                    number, color = color_number_combo.strip().split(" ")
                    number = int(number)
                    if number > minimums[color]:
                        minimums[color] = number
                    # if number > limits[color]:
                    #     fail_test = True
                    #     break
            minimums_sum += minimums["red"] * minimums["green"] * minimums["blue"]



            # if not fail_test:
            #     sum += game_int
    # print(sum)
    print(minimums_sum)

if __name__ == '__main__':
    main('input.txt')
