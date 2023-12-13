import copy


def main(input_file: str, part_2: bool = False):
    cards_dict = {
        "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }
    if part_2:
        cards_dict["J"] = 1
    bid_sum = 0
    hands_tuples = [] # list of tuples (hand, bid, hand_type, secondary_card_score) where hand type follows the ranks below
    type_ranks = {"five_of_a_kind": 6, "four_of_a_kind": 5, "full_house": 4, "three_of_a_kind": 3, "two_pair": 2,
                  "one_pair": 1, "high_card": 0}

    with open(input_file) as f:
        for line in f.readlines():
            hand, bid = line.split()
            bid = int(bid)
            unique_chars = {}
            hand_rank = 0
            secondary_hand_rank = 0
            for char in hand:
                if char not in unique_chars:
                    unique_chars[char] = 1
                else:
                    unique_chars[char] += 1

            if part_2:
                if "J" in unique_chars.keys() and len(unique_chars) != 1:
                    j_count = unique_chars["J"]
                    unique_chars.pop("J")
                    max_char = max(unique_chars, key=unique_chars.get)
                    unique_chars[max_char] += j_count

            # find starting hand rank base on hand types
            if len(unique_chars) == 2:
                max_count = unique_chars[max(unique_chars, key=unique_chars.get)]
                if max_count == 4:
                    hand_rank = type_ranks["four_of_a_kind"]
                elif max_count == 3:
                    hand_rank = type_ranks["full_house"]
            elif len(unique_chars) == 1:
                hand_rank = type_ranks["five_of_a_kind"]
            elif len(unique_chars) == 4:
                hand_rank = type_ranks["one_pair"]
            elif len(unique_chars) == 3:
                pairs = 0
                for char in unique_chars:
                    if unique_chars[char] == 2:
                        pairs += 1
                if pairs == 2:
                    hand_rank = type_ranks["two_pair"]
                else:
                    hand_rank = type_ranks["three_of_a_kind"]

            # find secondary hand rank based on card values
            for char in hand:
                secondary_hand_rank += secondary_hand_rank * 100 + cards_dict[char]

            if len(hands_tuples) == 0:
                hands_tuples.append((hand, bid, hand_rank, secondary_hand_rank))
                continue

            # find where to place hand in hands_tuples based ONLY on hand_rank
            current_hand_tuples = copy.deepcopy(hands_tuples)
            card_placed = False
            for compare_hand_index, compare_hand in enumerate(current_hand_tuples):
                if hand_rank < compare_hand[2]:
                    continue
                elif hand_rank == compare_hand[2]:
                    if secondary_hand_rank < compare_hand[3]:
                        continue
                    elif secondary_hand_rank == compare_hand[3]: # this case should not happen
                        print("ERROR: secondary_hand_rank == compare_hand[3]")
                        hands_tuples.insert(compare_hand_index, (hand, bid, hand_rank, secondary_hand_rank))
                        card_placed = True
                        break
                    else:
                        hands_tuples.insert(compare_hand_index, (hand, bid, hand_rank, secondary_hand_rank))
                        card_placed = True
                        break
                else:
                    hands_tuples.insert(compare_hand_index, (hand, bid, hand_rank, secondary_hand_rank))
                    card_placed = True
                    break

            if not card_placed:
                hands_tuples.append((hand, bid, hand_rank, secondary_hand_rank))
        for hand_i, hand in enumerate(hands_tuples):
            bid_sum += (len(hands_tuples)-hand_i) * hand[1]
            print(f"Adding {hand[1]} to bid sum for hand {hand[0]} at hand rank {hand_i} (aka: {(len(hands_tuples)-hand_i)} * {hand[1]}).")
    print(bid_sum)




if __name__ == '__main__':
    # main('input.txt')  # Part 1: too low 95025682 -- too high 256150920 -- too high 253607781 -- not correct 251881308
    # main('test.txt')
    main('input.txt', part_2=True)
    # main('test.txt', part_2=True)

