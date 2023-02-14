import sqlite_functions

#info = sqlite_functions.get_table_info("my_database.db", "table1")
#print(info)

#columns = sqlite_functions.get_table_columns("my_database.db", "table1")
#print(columns)

#data=sqlite_functions.get_tables_and_views("my_database.db")
#print(data)
tb1_sise=sqlite_functions.get_fields("my_database.db", "table1")
print(tb1_sise)

#all_tbs=sqlite_functions.get_all_tables_info("my_database.db")
#print(all_tbs)