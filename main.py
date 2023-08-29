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
            input("\nPress Enter to continue...")
            clear_console()
            return


def readfile(ip_file):
    try:
        return pd.read_excel(ip_file)
    except Exception as e:
        print(f"Error reading input data from '{ip_file}': {e}")
        return


def Create_Table(ip_file):
    data = readfile(ip_file)
    data_set = list(data)
    req_set = ['Column', 'DataType', 'Size']

    n = len(data)
    i = 0
    a = "create table table_name ("
    b = "{0} {1}[{2}]"
    while i < n and data_set == req_set:
        temp = data.iloc[i]
        column = data["Column"].iloc[i]
        datatype = data["DataType"].iloc[i]
        size = data["Size"].iloc[i]

        a += b.format(column, datatype, size)
        i += 1
        if i < n:
            a += ", "
    else:
        a += ");"
        print(a)


def main():
    input_file = "Data.xlsx"
    # output_file = "Query.txt"

    Create_Table(input_file)


if __name__ == "__main__":
    main()
