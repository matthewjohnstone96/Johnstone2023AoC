def main(input_file: str, part2=False):
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
    part2_seeds = []  # list of tuples (start, length)
    for i in range(0, len(seeds), 2):
        for j in range((seeds[i]), (seeds[i] + seeds[i + 1])):
            part2_seeds.append(j)

    print(f"Part 2 seeds ({len(part2_seeds)}): {part2_seeds}")
    min_loc_value_part_2 = 10000000000000
    for seed in part2_seeds:
        active_seed_traverse_value = seed
        for key in str_maps_traverse_order:
            for range_tuple in str_maps_to_range_lists[key]:
                if active_seed_traverse_value in range(range_tuple[1], range_tuple[1] + range_tuple[2]):
                    active_seed_traverse_value = range_tuple[0] + (active_seed_traverse_value - range_tuple[1])
                    break
        if active_seed_traverse_value < min_loc_value_part_2:
            min_loc_value_part_2 = active_seed_traverse_value

    print(f"Part 2: {min_loc_value_part_2}")


if __name__ == '__main__':
    main('input.txt')
    # main('test.txt')
