import warnings


def main(input_file: str, part_2: bool = False):
    sum_of_history = 0
    list_list_of_rows = [] # 0 means left, 1 means right
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            list_of_rows = line.split()
            list_of_rows = [int(x) for x in list_of_rows]
            list_list_of_rows.append(list_of_rows)
    print(list_list_of_rows)

    for history_list in list_list_of_rows:
        deltas_list_list = [history_list]
        end_of_list = False
        while not end_of_list:
            deltas = []
            for i in range(len(deltas_list_list[-1])-1):
               deltas.append(deltas_list_list[-1][i+1] - deltas_list_list[-1][i])
            if (sum(deltas) == 0 and deltas[0] == 0) or len(deltas) <= 1:
                end_of_list = True
            else:
                deltas_list_list.append(deltas)
        print(f"Delta list list: {deltas_list_list}")
        new_value = 0

        if part_2:
            for deltas_list_i in range(len(deltas_list_list)-1, -1, -1):
                new_value = deltas_list_list[deltas_list_i][0] - new_value
        else:
            for deltas_list in deltas_list_list:
                new_value += deltas_list[-1]
        print(new_value)
        sum_of_history += new_value

    print(f"Sum of history: {sum_of_history}")


if __name__ == '__main__':
    # main('input.txt')
    # main('test.txt')
    main('input.txt', part_2=True)
    # main('test.txt', part_2=True)
