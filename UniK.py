import pandas as pd
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Please enter one of: {', '.join(valid_options)}")


def confirm_overwrite(file_name):
    if os.path.exists(file_name):
        overwrite = get_valid_input(f"'{file_name}' already exists. Do you want to overwrite it? (yes/no): ",
                                    ['yes', 'no'])
        return overwrite == 'yes'
    return True


def read_excel_file(file_name, sheet_number):
    try:
        return pd.read_excel(file_name, sheet_name=sheet_number)
    except Exception as e:
        print(f"Error reading input data from '{file_name}': {e}")
        return


def save_to_txt(data, output_file):
    temp = open(output_file, "w")
    try:
        temp.write(data)
        print(f"Data has been successfully saved to '{output_file}'")
    except Exception as e:
        print(f"Error writing data to '{output_file}': {e}")
    temp.close()
