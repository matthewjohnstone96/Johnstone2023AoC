def main(input_file: str, part2=False):
    sum = 0
    with (open(input_file, "r") as file):
        parts_list = [] # list of tuples (part number, part index, part len, row number)
        symbols = [] # ditto but symbols (so no len) (symbol, symbol index, row number)
        for row_number, row in enumerate(file):
            row = row.strip()
            active_part = False
            part_number = 0
            part_index = 0
            for char_index, char in enumerate(row):
                if char == ".":
                    if active_part:
                        active_part = False
                        parts_list.append((part_number, part_index, char_index - part_index, row_number))
                    continue
                elif char.isdigit():
                    if not active_part:
                        active_part = True
                        part_number = int(char)
                        part_index = char_index
                    else:
                        part_number = part_number * 10 + int(char)
                else:
                    symbols.append((char, char_index, row_number))
                    if active_part:
                        active_part = False
                        parts_list.append((part_number, part_index, char_index - part_index, row_number))
            if active_part:
                parts_list.append((part_number, part_index, char_index - part_index, row_number))

        if not part2:
            for part in parts_list:
                for symbol in symbols:
                    if symbol[2] - 1 <= part[3] <= symbol[2] + 1 and part[1] - 1 <= symbol[1] <= part[1] + part[2]:
                        sum += part[0]
                        print(f"{part[0]}")
                        break
            print(sum)
            return sum

        for symbol in symbols:
            if symbol[0] != "*":
                continue
            gears = []
            for part in parts_list:
                if symbol[2] - 1 <= part[3] <= symbol[2] + 1 and part[1] - 1 <= symbol[1] <= part[1] + part[2]:
                    gears.append(part)
            if len(gears) == 2:
                sum += gears[0][0] * gears[1][0]
        print(sum)
        return sum


def alternative(input_file: str):
    def generate_adjacent_positions(digit_start_column: int, digit_row: int, digit_end_column: int,
                                    max_row: int, max_column: int):
        adjacent_positions = []
        for row in range(digit_row - 1, digit_row + 2):
            for column in range(digit_start_column - 1, digit_end_column + 2):
                if row < 0 or column < 0 or row > max_row or column > max_column:
                    continue
                adjacent_positions.append((row, column))
        return adjacent_positions

    sum = 0
    with (open(input_file, "r") as file):
        lines = file.readlines()
        line_num = 0
        lines_len = len(lines)
        row_len = len(lines[0].strip())
        for line in lines:
            line = line.strip()
            # print(f"Line #{line_num}: {len(line)}")
            active_part = False
            part_number = 0
            part_index = 0
            char_index = 0
            for char in line:
                if char.isdigit():
                    if not active_part:
                        active_part = True
                        part_number = int(char)
                        part_index = char_index
                    else:
                        part_number = part_number * 10 + int(char)
                else:
                    if active_part:
                        active_part = False
                        adjacent_positions = generate_adjacent_positions(digit_start_column=part_index, digit_row=line_num, digit_end_column=char_index-1,
                                                                         max_row=lines_len-1, max_column=row_len-1)
                        # print(f"=====================\nPart {part_number} at {line_num}, {part_index} to {char_index-1}")
                        # print(adjacent_positions)
                        # print(lines[adjacent_positions[0][0]][adjacent_positions[0][1]])
                        found = False
                        for adjacent_position in adjacent_positions:
                            row, column = adjacent_position
                            if lines[row][column] != "." and not lines[row][column].isdigit():
                                sum += part_number
                                found = True
                                break
                        # if not found:
                        #     print(f"Could not find adjacent symbol for part {part_number} at {line_num}, {part_index}")
                char_index += 1
            line_num += 1

        print(sum)


if __name__ == '__main__':
    # main('input.txt', part2=True)
    main('austin.txt', part2=False)
    # alternative('input.txt')
    # main('test.txt')
