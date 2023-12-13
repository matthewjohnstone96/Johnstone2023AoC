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
        return sum

if __name__ == '__main__':
    main('austin.txt', part2=True)
    # main('test.txt')
