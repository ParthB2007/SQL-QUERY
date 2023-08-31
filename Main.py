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
        return overwrite
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


def create_table_query(data, table_name):
    query = f"CREATE TABLE {table_name} ("
    column_template = "{} {}[{}]"
    for _, row in data.iterrows():
        query += column_template.format(row["Column"], row["DataType"], row["Size"]) + ", "
    query = query.rstrip(", ") + ");"
    print(query)
    return query


def add_data_query(data, table_name, columns):
    query = f"INSERT INTO {table_name}(" + ", ".join(columns) + ") VALUES"
    temp = query
    rows = []
    for _, row in data.iterrows():
        row_values = ", ".join(str(row[value]) for value in columns)
        rows.append("(" + row_values + ")")
    query += f";\n{temp}".join(rows) + ";"
    print(query)
    return query


def desc_table(table_name):
    query = f"DESC {table_name}"
    print(query)
    return query


def select_query1(table_name):
    query = f"SELECT * FROM {table_name};"
    print(query)
    return query


def select_query2(table_name, Condition):
    query = f"SELECT * FROM {table_name} where {Condition};"
    print(query)
    return query


def select_query3(table_name, find):
    query = f"SELECT {find} FROM {table_name};"
    print(query)
    return query


def main():
    table_name = input("Enter Table name: ")

    clear_console()

    print("Select an option:")
    print("1. Create Query")
    print("2. Insert Query")
    print("3. Describe Table Query")
    print("4. Select Data Query")

    choice = get_valid_input("Enter your choice (1/2/3/4): ", ['1', '2', '3', '4'])
    clear_console()

    final_query = ""

    if choice == '1' or choice == '2':
        input_file = input("Enter file name to read data: ")
        input_file += ".xlsx"

        input_data1 = read_excel_file(input_file, 0)
        input_data2 = read_excel_file(input_file, 1)
        title_columns = list(input_data1["Column"])

        clear_console()

        if choice == '1':
            create_query = create_table_query(input_data1, table_name)
            final_query = create_query
        elif choice == '2':
            insert_query = add_data_query(input_data2, table_name, title_columns)
            final_query = insert_query

    else:
        if choice == '3':
            desc_query = desc_table(table_name)
            final_query = desc_query
        elif choice == '4':
            print("Select an option:")
            print("1. Full table")
            print("2. Specific raw")
            print("3. Specific column")

            select_choice = get_valid_input("Enter your choice (1/2/3): ", ['1', '2', '3'])
            select_data_query = ""

            clear_console()

            if select_choice == '1':
                select_data_query = select_query1(table_name)
            elif select_choice == '2':
                Condition = input("What u wanna find? : ")
                select_data_query = select_query2(table_name, Condition)
            elif select_choice == '3':
                Find = input("Enter column name : ")
                select_data_query = select_query3(table_name, Find)

            final_query = select_data_query

    print("\n")

    condition = 'no'
    while condition == 'no':
        output_file = input("Enter file name to save your output data: ")
        output_file += ".txt"

        clear_console()
        condition = confirm_overwrite(output_file)
        if condition or condition == 'yes':
            save_to_txt(final_query, output_file)
        else:
            print(f"No changes made. Exiting '{output_file}'")


if __name__ == "__main__":
    clear_console()
    main()
