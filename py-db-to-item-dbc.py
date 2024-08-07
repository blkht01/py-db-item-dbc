# Copyright (c) 2024, blkht01@github
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

import pymysql

# Database connection parameters
db_config = {
    'host': 'localhost',            # IP of your database server
    'user': 'acore',                # Database user
    'password': 'acore',            # Database password
    'database': 'acore_world',   # Database name
    'charset': 'utf8mb4',           # Database charset (probably leave this as is)
    'cursorclass': pymysql.cursors.DictCursor
}

# Define the range for the entries you want to extract
entry_start = 73840
entry_end = 999999

# SQL query to fetch data from item_template with a range filter
select_query = f"""
SELECT 
    entry as ID, 
    class as ClassID,
    subclass as SubclassID, 
    SoundOverrideSubclass as Sound_Override_subclassid, 
    Material, 
    displayid as DisplayInfoID, 
    InventoryType, 
    sheath as SheatheType 
FROM 
    item_template
WHERE 
    entry BETWEEN {entry_start} AND {entry_end}
"""

# Connect to the database
connection = pymysql.connect(**db_config)

try:
    with connection.cursor() as cursor:
        # Execute the select query
        cursor.execute(select_query)
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Prepare the SQL file content
        sql_commands = []

        # Option 1: Delete all existing entries in the table
        # sql_commands.append("DELETE FROM dbc.db_item_12340;")

        # Option 2: Conditional delete (uncomment the next line if this is the desired approach)
        sql_commands.append(f"DELETE FROM dbc.db_item_12340 WHERE ID BETWEEN {entry_start} AND {entry_end};")

        # Generate INSERT statements
        for row in rows:
            sql_insert = f"INSERT INTO dbc.db_item_12340 (ID, ClassID, SubclassID, Sound_Override_subclassid, Material, DisplayInfoID, InventoryType, SheatheType) VALUES ({row['ID']}, {row['ClassID']}, {row['Sound_Override_subclassid']}, {row['Material']}, {row['DisplayInfoID']}, {row['InventoryType']}, {row['SheatheType']});"
            sql_commands.append(sql_insert)
        
        # Save to a SQL file
        with open('inserts_into_db_item_12340.sql', 'w') as file:
            file.write('\n'.join(sql_commands))
        
        print("SQL file with DELETE and INSERT statements generated successfully.")

finally:
    # Close the connection
    connection.close()
