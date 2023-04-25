def input_from_user(prompt: str):
    new_input = input(prompt)
    if new_input.isdigit():
        return int(new_input)
    return input_from_user(prompt)