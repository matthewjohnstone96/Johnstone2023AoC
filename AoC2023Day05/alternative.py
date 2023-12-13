import numpy as np
def main(input_file: str, part2=False):
    sum = 0
    str_maps_to_range_lists = {0: [], 1: [], 2: [], 3: [],
                               4: [], 5: [], 6: []}
    str_maps_traverse_order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"]
    seeds = []
    location_number = 10000000000000000000000000
    # Read input file and make maps
    with (open(input_file, "r") as file):
        active_map = None
        for line in file.readlines():
            if "seeds:" in line:
                seeds = [int(x) for x in line.strip().split(":")[1].split()]
            else:
                if line == "\n":
                    active_map = None
                    continue
                if active_map is None:
                    for key in str_maps_traverse_order:
                        if key == line[0:len(key)] and "map" in line:
                            active_map = str_maps_traverse_order.index(key)
                            break
                else:
                    str_maps_to_range_lists[active_map].append(tuple(map(int, line.strip().split())))

    for seed in seeds:
        tracked_value = seed  # will ultimately be the location after all maps are traversed
        for index, step in enumerate(str_maps_traverse_order):
            for range_tuple in str_maps_to_range_lists[index]:
                if tracked_value in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                    tracked_value = range_tuple[0] + (tracked_value - range_tuple[1])
                    break
        if tracked_value < location_number:
            location_number = tracked_value
    print(f"Part 1: {location_number}")

    # Part 2
    # seed restructure
    part2_seeds = []  # list of tuples (start, length)
    for i in range(0, len(seeds), 2):
        part2_seeds.append((seeds[i], seeds[i + 1]))

    print(f"Part 2 seeds: {part2_seeds}")
    print(f"Part 2: {find_min_part_2(part2_seeds, str_maps_to_range_lists)}")


def find_min_part_2(seed_tuple_list: list[tuple[int]], maps_to_range_lists: dict[int, list[tuple[int]]]):
    min_value: int = 10000000000
    for seed_range_tuple in seed_tuple_list:
        for i in range(0, seed_range_tuple[1]):
            active_seed_travers = seed_range_tuple[0] + i
            for j in range(0, len(maps_to_range_lists.keys())):
                for range_tuple in maps_to_range_lists[j]:
                    if active_seed_travers in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                        active_seed_travers = range_tuple[0] + (active_seed_travers - range_tuple[1])
                        break
            if active_seed_travers < min_value:
                min_value = active_seed_travers
    return min_value


if __name__ == '__main__':
    # main('input.txt')
    main('test.txt')
