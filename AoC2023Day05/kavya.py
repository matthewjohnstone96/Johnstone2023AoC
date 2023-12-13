import re

def main():
    # with open("sample.txt") as file:
    with open("input.txt") as file:
        input = [line.rstrip() for line in file]

    seeds = [int(s) for s in input[0].split(": ")[1].split(" ")]


    def parse_maps(header):
        index = input.index(header)
        map = []
        for i in range(index + 1, len(input)):
            if input[i] == '':
                break
            values = [int(x) for x in input[i].split(' ')]
            map.append((values[0], values[1], values[2]))
        return map


    seed_to_soil = parse_maps("seed-to-soil map:")
    seed_to_soil_cache = {}
    soil_to_fertilizer = parse_maps("soil-to-fertilizer map:")
    soil_to_fertilizer_cache = {}
    fertilizer_to_water = parse_maps("fertilizer-to-water map:")
    fertilizer_to_water_cache = {}
    water_to_light = parse_maps("water-to-light map:")
    water_to_light_cache = {}
    light_to_temp = parse_maps("light-to-temperature map:")
    light_to_temp_cache = {}
    temp_to_humidity = parse_maps("temperature-to-humidity map:")
    temp_to_humidity_cache = {}
    humidity_to_location = parse_maps("humidity-to-location map:")
    humidity_to_location_cache = {}


    def get_next_destination(curr, map, cache):
        if curr in cache:
            return cache[curr]

        for row in map:
            destination_start = row[0]
            source_start = row[1]
            map_range = row[2]

            if source_start <= curr < source_start + map_range:
                step = curr - source_start
                destination = destination_start + step
                cache[curr] = destination

                return destination

        return curr


    def get_previous_destination(curr, map, cache):
        if curr in cache:
            return cache[curr]

        for row in map:
            destination_start = row[0]
            source_start = row[1]
            map_range = row[2]

            if destination_start <= curr < destination_start + map_range:
                step = curr - destination_start
                source = source_start + step
                cache[curr] = source

                return source

        return curr


    def get_closest_location(seed):
        soil = get_next_destination(seed, seed_to_soil, seed_to_soil_cache)
        fertilizer = get_next_destination(soil, soil_to_fertilizer, soil_to_fertilizer_cache)
        water = get_next_destination(fertilizer, fertilizer_to_water, fertilizer_to_water_cache)
        light = get_next_destination(water, water_to_light, water_to_light_cache)
        temp = get_next_destination(light, light_to_temp, light_to_temp_cache)
        humidity = get_next_destination(temp,
                                        temp_to_humidity, temp_to_humidity_cache)
        location = get_next_destination(humidity, humidity_to_location, humidity_to_location_cache)

        return location


    closest_location = None
    smallest_index = None
    # for seed_index in range(0, len(seeds), 2):
    #     print(seed_index)
    #     range_count = seeds[seed_index + 1]
    #     initial_seed = seeds[seed_index]
    #
    #     for seed in range(initial_seed, initial_seed + range_count):
    #         location = get_closest_location(seed)
    #
    #         if closest_location is None or closest_location > location:
    #             closest_location = location

    ranges = []
    for seed_index in range(0, len(seeds), 2):
        print(seed_index)
        range_count = seeds[seed_index + 1]
        initial_seed = seeds[seed_index]
        ranges.append((initial_seed, initial_seed + range_count))
    print(ranges)


    def is_in_range(curr):
        for range in ranges:
            if range[0] <= curr < range[1]:
                return True
        return False


    location = 0
    while True:
        print(location)
        humidity = get_previous_destination(location, humidity_to_location, humidity_to_location_cache)
        temp = get_previous_destination(humidity, temp_to_humidity, temp_to_humidity_cache)
        light = get_previous_destination(temp, light_to_temp, light_to_temp_cache)
        water = get_previous_destination(light, water_to_light, water_to_light_cache)
        fertilizer = get_previous_destination(water, fertilizer_to_water, fertilizer_to_water_cache)
        soil = get_previous_destination(fertilizer, soil_to_fertilizer, soil_to_fertilizer_cache)
        seed = get_previous_destination(soil, seed_to_soil, seed_to_soil_cache)

        if is_in_range(seed):
            break

        location += 1
    print("location: ", location)


if __name__ == '__main__':
    main()