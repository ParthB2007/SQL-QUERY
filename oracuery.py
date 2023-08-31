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


def select_query(table_name):
    query = f"SELECT * FROM {table_name};"
    print(query)
    return query


def select_column_query(table_name, find):
    query = f"SELECT {find} FROM {table_name};"
    print(query)
    return query


def select_raw_query(table_name, Condition):
    query = f"SELECT * FROM {table_name} where {Condition};"
    print(query)
    return query
