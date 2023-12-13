import warnings


def main(input_file: str, part_2: bool = False):
    times_list = []
    distances_list = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            if "time:" in line.lower():
                times_list = [int(x.strip()) for x in line.split(":")[1].split() if x.isdigit()]
            elif "distance:" in line.lower():
                distances_list = [int(x.strip()) for x in line.split(":")[1].split() if x.isdigit()]

    if part_2:
        time_total = 0
        distance_total = 0
        for i, time in enumerate(times_list):
            time_total = int(f"{time_total}{time}")
        times_list = [time_total]
        for i, distance in enumerate(distances_list):
            distance_total = int(f"{distance_total}{distance}")
        distances_list = [distance_total]

    print(f"Times list: {times_list}")
    print(f"Distances list: {distances_list}")

    win_possibilities_sum = 1
    for i, time in enumerate(times_list):
        is_odd = time % 2 != 0
        half_time_floor = int((time - (1 * is_odd))/2)
        half_time_ceil = int((time + (1 * is_odd))/2)
        winning_index = None
        for j in range(0, half_time_floor, 1):
            distance_traveled = (time - j)*j
            if distance_traveled > distances_list[i]:
                winning_index = j
                break
        if winning_index is None:
            warnings.warn("No winning index found")
        else:
            win_multiplier = (half_time_ceil - winning_index)*2 + (1 * (not is_odd))
            win_possibilities_sum *= win_multiplier
            print(f"Winning multiplier: {win_multiplier}")

    print(f"Winning possibilities sum: {win_possibilities_sum}")


if __name__ == '__main__':
    # main('input.txt')
    main('test.txt')
    main('input.txt', part_2=True)
    main('test.txt', part_2=True)
