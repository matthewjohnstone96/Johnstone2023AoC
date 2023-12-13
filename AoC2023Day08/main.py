import warnings
import math

def main(input_file: str, part_2: bool = False):
    path_dict = {}
    traverse_list = [] # 0 means left, 1 means right
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line != "" and "=" in line:
                path_key, paths = line.split("=")
                paths = [x.strip() for x in paths.strip().strip(")").strip("(").split(",")]
                path_dict[path_key.strip()] = paths
            elif line != "":
                for char in line:
                    if char == "L":
                        traverse_list.append(0)
                    elif char == "R":
                        traverse_list.append(1)
                    else:
                        warnings.warn(f"Invalid traverse char: {char}")

    print(path_dict)
    print(traverse_list)
    if not part_2:
        current_key = 'AAA'
        steps_taken = 0
        while current_key != 'ZZZ':
            current_key = path_dict[current_key][traverse_list[steps_taken % len(traverse_list)]]
            steps_taken += 1
            print(f"Current key: {current_key} | Steps taken: {steps_taken}")
    else:
        all_keys_tracked = []
        for key in path_dict.keys():
            if 'A' in key:
                all_keys_tracked.append(key) # append starting keys
        steps_taken = 0
        steps_taken_list = []
        print(f"All keys tracked: {all_keys_tracked}")
        for key_i, key in enumerate(all_keys_tracked):
            current_key = key
            while "Z" not in current_key:
                current_key = path_dict[current_key][traverse_list[steps_taken % len(traverse_list)]]
                steps_taken += 1
            print(f"Current key: {current_key} | Steps taken: {steps_taken}")
            steps_taken_list.append(steps_taken)
            steps_taken = 0
        print(f"Lowest Steps: {math.lcm(*steps_taken_list)}")


if __name__ == '__main__':
    # main('input.txt') # 11567
    # main('test.txt')
    main('input.txt', part_2=True)
    # main('test.txt', part_2=True)
