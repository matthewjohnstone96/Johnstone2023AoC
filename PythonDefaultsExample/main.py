def main():
    alternative_str = "second string"
    for i in range(10):
        if i == 5:
            print(function_with_default_input_string(alternative_str))
        else:
            print(function_with_default_input_string())


def function_with_default_input_string(input_string: str = "Initial default string"):
    return input_string


if __name__ == '__main__':
    main()