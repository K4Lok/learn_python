Python version: 3.6.x

Library required: mysql.connector, openpyxl

Library installation:
    pip install openpyxl|| pip3 install openpyxl    
    pip install mysql-connector-python || pip3 install mysql-connector-python

Check whether the library installed properly:
    pip list || pip3 list

What the script does:
    createTable.py:
	Connect to DB
	Send SQL to Create Table
	Commit
    insertDB.py:
	Connect to DB
	Get data from Excel
	Send SQL Insert Data
	Commit

More infos:
    SQL Create Table       : "https://www.w3schools.com/sql/sql_create_table.asp"
    Insert Multiple rows   : "https://stackoverflow.com/questions/452859/inserting-multiple-rows-in-a-single-sql-query"
    The benefits of cursor : "https://stackoverflow.com/questions/3861558/what-are-the-benefits-of-using-database-cursor"
    SQL Insert data        : "https://www.w3schools.com/python/python_mysql_insert.asp"
    Question on %s         : "https://stackoverflow.com/questions/20463333/mysqldb-python-insert-d-and-s"