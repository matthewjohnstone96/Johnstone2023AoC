# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def main(input_file: str):
    with open(input_file, "r") as file:
        sum = 0
        for line in file.readlines():
            numbers = []
            index = 0
            for char in line.lower():
                if char.isdigit():
                    numbers.append((int(char), index))
                index += 1

            for str_digit in DIGITS:
                index = 0
                for index in range(len(line)):
                    if line.lower()[index:].startswith(str_digit):
                        numbers.append((DIGITS.index(str_digit) + 1, index))
                        index += len(str_digit)
                    else:
                        index += 1
                # if str_digit.lower() in line.lower():
                #     number_index = line.lower().find(str_digit.lower())
                #     numbers.append((DIGITS.index(str_digit) + 1, number_index))
            numbers.sort(key=lambda x: x[1])
            if len(numbers) == 1:
                number = numbers[0][0] * 10 + numbers[0][0]
                # print(number)
                sum += number
            if len(numbers) >= 2:
                number = numbers[0][0] * 10 + numbers[-1][0]
                # print(number)
                sum += number
        print(sum)


def test():
    # test_str = "onetwothreeone2"
    # for digit in DIGITS:
    #     if digit in test_str:

    # print(test_str.find("one"))

    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('input.txt')
    # main('input_2.txt')
    # test()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
