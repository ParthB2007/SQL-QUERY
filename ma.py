import oracuery as ou
import UniK as uk


def main():
    table_name = input("Enter Table name: ")

    uk.clear_console()

    print("Select an option:")
    print("1. Create Query")
    print("2. Insert Query")
    print("3. Describe Table Query")
    print("4. Select Data Query")

    choice = uk.get_valid_input("Enter your choice (1/2/3/4): ", ['1', '2', '3', '4'])
    uk.clear_console()

    final_query = ""

    if choice == '1' or choice == '2':
        input_file = input("Enter file name to read data: ")
        input_file += ".xlsx"

        input_data1 = uk.read_excel_file(input_file, 0)
        input_data2 = uk.read_excel_file(input_file, 1)
        title_columns = list(input_data1["Column"])

        uk.clear_console()

        if choice == '1':
            create_query = ou.create_table_query(input_data1, table_name)
            final_query = create_query
        elif choice == '2':
            insert_query = ou.add_data_query(input_data2, table_name, title_columns)
            final_query = insert_query

    else:
        if choice == '3':
            desc_query = ou.desc_table(table_name)
            final_query = desc_query
        elif choice == '4':
            print("Select an option:")
            print("1. Full table")
            print("2. Specific raw")
            print("3. Specific column")

            select_choice = uk.get_valid_input("Enter your choice (1/2/3): ", ['1', '2', '3'])
            select_data_query = ""

            uk.clear_console()

            if select_choice == '1':
                select_data_query = ou.select_query(table_name)
            elif select_choice == '2':
                Condition = input("What u wanna find? : ")
                select_data_query = ou.select_raw_query(table_name, Condition)
            elif select_choice == '3':
                Find = input("Enter column name : ")
                select_data_query = ou.select_column_query(table_name, Find)

            final_query = select_data_query

    print("\n")

    condition = 'no'
    while condition == 'no':
        output_file = input("Enter file name to save your output data: ")
        output_file += ".txt"

        uk.clear_console()
        condition = uk.confirm_overwrite(output_file)
        if condition or condition == 'yes':
            uk.save_to_txt(final_query, output_file)
        else:
            print(f"No changes made. Exiting '{output_file}'")


if __name__ == "__main__":
    uk.clear_console()
    main()
