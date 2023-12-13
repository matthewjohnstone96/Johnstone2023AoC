import sys

import numba as nb
import numpy as np


def main(input_file: str, part2=False):
    sum = 0
    str_maps_to_range_lists = {"seed": [], "soil": [], "fertilizer": [], "water": [],
                               "light": [], "temperature": [], "humidity": []}
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
                    for key in str_maps_to_range_lists.keys():
                        if key == line[0:len(key)] and "map" in line:
                            active_map = key
                            break
                else:
                    str_maps_to_range_lists[active_map].append(tuple(map(int, line.strip().split())))

    # print(soil_map)
    for seed in seeds:
        tracked_value = seed  # will ultimately be the location after all maps are traversed
        for key in str_maps_traverse_order:
            for range_tuple in str_maps_to_range_lists[key]:
                if tracked_value in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                    tracked_value = range_tuple[0] + (tracked_value - range_tuple[1])
                    break
        if tracked_value < location_number:
            location_number = tracked_value
    print(f"Part 1: {location_number}")

    # Part 2
    # seed restructure
    print("Starting part 2")
    # convert all data to numpy arrays
    traverse_list_list = np.empty(len(str_maps_traverse_order), dtype=np.ndarray)
    for key_i, key in enumerate(str_maps_traverse_order):
        key_array = np.empty(len(str_maps_to_range_lists[key]), dtype=np.ndarray)
        for range_tuple_i, range_tuple in enumerate(str_maps_to_range_lists[key]):
            range_tuple_array = np.array(range_tuple, dtype=np.int64)
            key_array[range_tuple_i] = range_tuple_array
        traverse_list_list[key_i] = key_array

    seeds_array = np.array(seeds, dtype=np.int64)
    # print(traverse_list_list)
    # print("===================")
    # print(str_maps_to_range_lists)

    # print(seeds_array)
    # sys.exit(0)
    # print(f"Part 2: {numba_method(seeds_array, traverse_list_list)}")
    print(f"Part 2: {reverse_method(seeds_array, traverse_list_list)}")


def numba_method(seeds: np.ndarray[np.int64], traverse_list_list: np.ndarray[np.ndarray[np.ndarray[np.int64]]]) -> np.int64:
    min_loc_value_part_2: np.int64 = np.int64(10000000000000)
    for i in range(0, len(seeds), 2):
        for j in range((seeds[i]), (seeds[i] + seeds[i + 1])):
            active_seed_traverse_value = j
            for traverse_set in traverse_list_list:
                for range_tuple in traverse_set:
                    if active_seed_traverse_value in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                        active_seed_traverse_value = range_tuple[0] + (active_seed_traverse_value - range_tuple[1])
                        break
            if active_seed_traverse_value < min_loc_value_part_2:
                min_loc_value_part_2 = active_seed_traverse_value
    return min_loc_value_part_2


def reverse_method(seeds: np.ndarray[np.int64], traverse_list_list: np.ndarray[np.ndarray[np.ndarray[np.int64]]]) -> np.int64:
    seed_tuple_list = []
    for i in range(0, len(seeds), 2):
        seed_tuple_list.append((seeds[i], seeds[i + 1]))
    print(f"seed_tuple_list: {seed_tuple_list}")
    min_loc_value_part_2: np.int64 = np.int64(0)
    min_not_found = True
    while min_not_found:
        min_loc_value_part_2 += 1
        print(f"Back tracking from {min_loc_value_part_2}\n====================")
        active_seed_traverse_value = min_loc_value_part_2
        for i in range(0, len(traverse_list_list)):
            for range_tuple in traverse_list_list[len(traverse_list_list) - i - 1]:
                if active_seed_traverse_value in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                    active_seed_traverse_value = range_tuple[1] + (active_seed_traverse_value - range_tuple[0])
                    break
                print(f"active_seed_traverse_value: {active_seed_traverse_value}")
        for seed_tuple in seed_tuple_list:
            if active_seed_traverse_value in range(seed_tuple[0], seed_tuple[0] + seed_tuple[1]):
                break
    return min_loc_value_part_2


if __name__ == '__main__':
    main('input.txt')
    # main('test.txt')
