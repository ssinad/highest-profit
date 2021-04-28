# highest-profit challenge

To run the example, simply execute the script named `run` using a shell of your choice.

Part 1 and 2 are done inside the Python file.  
As for the third part, if the non-numeric values are assumed to be NULL in the table, the following queries should do the same in SQL.
```sql
    ALTER TABLE datatable
    ALTER COLUMN "Profit (in millions)" Profit;
    ALTER TABLE datatable
    ALTER COLUMN "Revenue (in millions)" Revenue;

    SELECT COUNT(*) 
    FROM datatable;
    
    SELECT COUNT(*) 
    FROM datatable
    WHERE profit IS NOT NULL;

    SELECT * FROM datatable
    WHERE profit IS NOT NULL
    ORDER BY profit DESC
    LIMIT 20;
```