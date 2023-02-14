import sqlite3
from collections import OrderedDict  
#function to get table size for a table in a database  not working
def calculate_table_size(db_file_path, table_name):
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Get the size of the data in the table in bytes
    cursor.execute(f"SELECT sum(length(*)), count(*) FROM {table_name}")
    result = cursor.fetchone()
    if result is not None:
        data_size_bytes, row_count = result
        data_size_bytes += row_count * 100  # Estimated overhead per row
    else:
        data_size_bytes = 0
    print("Data size in bytes:", data_size_bytes)

    # Get the size of the indices in the table in bytes
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_names = [row[1] for row in cursor.fetchall()]
    index_size_bytes = 0
    for column_name in column_names:
        cursor.execute(f"PRAGMA index_list({table_name})")
        indices = cursor.fetchall()
        for index_name, *_ in indices:
            if index_name.startswith(f"sqlite_autoindex_{table_name}_"):
                continue
            cursor.execute(f"SELECT sum(length(quote({column_name}))) FROM {index_name}")
            index_size_result = cursor.fetchone()
            index_size_bytes += index_size_result[0] if index_size_result is not None else 0
    print("Index size in bytes:", index_size_bytes)

    # Total size in bytes
    table_size_bytes = data_size_bytes + index_size_bytes
    print("Table size in bytes:", table_size_bytes)

    # Convert to megabytes
    table_size_mb = table_size_bytes / 1024 / 1024
    return table_size_mb


#function to get table names for a database
def get_tables_and_views(db_name):
    print('from get_tables_and_views:',db_name)
    path=db_name
    print(path)
    conn = sqlite3.connect(path)
    
    cursor = conn.cursor()
    
    query = "SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view');"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit
    
    tables_and_views = {}
    for name, tp in result:
        tables_and_views[name] = tp
    
    tables_and_views_ordered = OrderedDict(sorted(tables_and_views.items()))
    cursor.close()
    conn.close()
    
    return tables_and_views_ordered
#function to get table names for a database
def get_fields(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    query = f"PRAGMA table_info({table_name});"
    cursor.execute(query)
    result = cursor.fetchall()

    
    fields = {}
    for field_info in result:
        fields[field_info[1]] = {"cid": field_info[0], "type": field_info[2]}       
    
    cursor.close()
    conn.close()
    
    return fields
#function to get table size for a single table in a database
def get_table_size(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA page_size")
    page_size = cursor.fetchone()[0]
    
    cursor.execute(f"PRAGMA table_info({table_name})")
    num_pages = cursor.fetchone()[0]
    
    total_size = page_size * num_pages
    
    cursor.close()
    conn.close()
    
    return total_size
#function to get table info for a single table in a database
def get_table_info(db_file, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get the size of the table in bytes
    cursor.execute(f"PRAGMA page_count;")
    pages = cursor.fetchone()[0]
    cursor.execute(f"PRAGMA page_size;")
    page_size = cursor.fetchone()[0]
    table_size_bytes = pages * page_size

    # Get the number of columns in the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_info = cursor.fetchall()
    num_columns = len(column_info)

    # Get the number of rows in the table
    cursor.execute(f"SELECT count(*) FROM {table_name}")
    num_rows = cursor.fetchone()[0]

    # Get the names and columns of the indices associated with the table
    #cursor.execute(f"PRAGMA index_list({table_name})")
    #index_info = cursor.fetchall()
    #indices = []
    #for idx in index_info:
    #    index_name = idx[1]
    #    index_columns = idx[2]
    #    indices.append((index_name, index_columns))

    # Close the connection
    conn.close()

    # Convert the size of the table from bytes to MB
    table_size_mb = table_size_bytes / 1024 / 1024

    tables_and_views={
        "table_name": table_name,
        "table_size_mb": table_size_mb,
        "num_columns": num_columns,        
        "num_rows": num_rows,
        #"indices": indices
    }

    tables_and_views_ordered = OrderedDict(tables_and_views.items())
    print(tables_and_views_ordered)
    # Return the information about the table in a dictionary
    return tables_and_views_ordered
#function to get columns info for a table in a database
def get_table_columns(db_file, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get the names and data types of the columns in the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_info = cursor.fetchall()
    columns = {}
    for col in column_info:
        column_name = col[1]
        column_type = col[2]
        columns[column_name] = column_type

    # Close the connection
    conn.close()

    # Return the names and data types of the columns as a dictionary
    return columns
#function to get tables info for all tables in a database
def get_all_tables_info(db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get the names of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Get the information about each table in the database
    tables_info = []
    for table in tables:
        table_name = table[0]
        table_info = get_table_info(db_file, table_name)
        tables_info.append(table_info)

    # Close the connection
    conn.close()

    # Return the information about each table in the database
    return tables_info


