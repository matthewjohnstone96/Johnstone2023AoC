def main(input_file: str):
    sum = 0
    card_quantity_map = {}
    with (open(input_file, "r") as file):
        for line in file.readlines():
            card_str, all_numbers = line.strip().split(":")
            card_id = int(card_str.split()[1])
            winning_numbers_str, numbers_str = all_numbers.split("|")
            winning_numbers = [int(x.strip()) for x in winning_numbers_str.strip().split()]
            numbers = [int(x.strip()) for x in numbers_str.strip().split()]
            quantity_of_winning_numbers = 0
            for number in numbers:
                if number in winning_numbers:
                    quantity_of_winning_numbers += 1

            if quantity_of_winning_numbers > 0:
                sum += 2 ** (quantity_of_winning_numbers - 1)
            card_quantity_map[card_id] = quantity_of_winning_numbers
    print(f"Part 1 Sum: {sum}")
    # return sum
    part_2_sum = 0
    card_count_map = {}
    for card_id in card_quantity_map.keys():
        card_count_map[card_id] = 1
    for card, card_wins in card_quantity_map.items():
        for i in range(1, card_wins + 1):
            card_count_map[card+i] += 1*card_count_map[card]
    for card, count in card_count_map.items():
        part_2_sum += count
    print(card_quantity_map)
    print(card_count_map)
    print(f"Part 2 Sum: {part_2_sum}")





if __name__ == '__main__':
    main('input.txt')
    # main('test.txt')
