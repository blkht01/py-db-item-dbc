A simple python script that I use for exporting entries from item_template database to easily import into item.dbc

The way I do it:
- Edit the python script and set desired item_template.entry range.
- Run python script. On linux: sudo python3 py-db-item-dbc.py
- Import inserts_into_db_item_12340.sql to my dbc database
- Use WDBX editor to import from dbc.db_item_12340
- Profit
