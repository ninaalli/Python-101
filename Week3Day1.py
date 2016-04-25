A relational database is a collection of data organised in tables.
There are relations among the tables. The tables are formally described. They consist of rows and columns.

SQL (Structured Query Language) is a database computer language designed for managing data in relational database management systems.

A table is a set of values that is organised using a model of vertical columns and horizontal rows.

The columns are identified by their names. A schema of a database system is its structure described in a formal language. It defines the tables, the fields, relationships, views, indexes, procedures, functions, queues, triggers, and other elements.

A database row represents a single, implicitly structured data item in a table. It is also called a tuple or a record.

sqlite> .help
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail on|off           Stop after hitting an error.  Default OFF
.binary on|off         Turn binary output on or off.  Default OFF
.clone NEWDB           Clone data into NEWDB from the existing database
.databases             List names and files of attached databases
.dbinfo ?DB?           Show status information about the database
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo on|off           Turn command echo on or off
.eqp on|off            Enable or disable automatic EXPLAIN QUERY PLAN
.exit                  Exit this program
.explain ?on|off?      Turn output mode suitable for EXPLAIN on or off.
                         With no args, it turns EXPLAIN on.
.fullschema            Show schema and the content of sqlite_stat tables
.headers on|off        Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indexes ?TABLE?       Show names of all indexes
                         If TABLE specified, only show indexes for tables
                         matching LIKE pattern TABLE.
.limit ?LIMIT? ?VAL?   Display or change the value of an SQLITE_LIMIT
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         ascii    Columns/rows delimited by 0x1F and 0x1E
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator strings
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.once FILENAME         Output for the next SQL command only to FILENAME
.open ?FILENAME?       Close existing database and reopen FILENAME
.output ?FILENAME?     Send output to FILENAME or stdout
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.save FILE             Write in-memory database into FILE
.scanstats on|off      Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
.separator COL ?ROW?   Change the column separator and optionally the row
                         separator for both the output mode and .import
.shell CMD ARGS...     Run CMD ARGS... in a system shell
.show                  Show the current values for various settings
.stats on|off          Turn stats on or off
.system CMD ARGS...    Run CMD ARGS... in a system shell
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.timer on|off          Turn SQL timer on or off
.trace FILE|off        Output each SQL statement as it is run
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   Set column widths for "column" mode
                         Negative values right-justify
sqlite> 

 CREATE statement is used to create tables, indexes, views, and triggers
 ALTER TABLE statement changes the structure of a table. 
 DROP statement removes tables, indexes, views, or triggers.

DATA TYPES:
NULL — The value is a NULL value
INTEGER — a signed integer
REAL — a floating point value
TEXT — a text string
BLOB — a blob of data


With boolean operators we perform logical operations. SQLite has three boolean operators: AND, OR, and NOT. Boolean operators return true or false. In SQLite, 1 is true, 0 is false.

The AND operator evaluates to true if both operands are true.
Relational operators are used to compare values.

Symbol	Meaning
<	strictly less than
<=	less than or equal to
>	greater than
>=	greater than or equal to
= or ==	equal to
!= or <>	not equal to
These operators always result in a boolean value.

on the foreign ID page:
click on gym, click create Foreign key on the MANY, links the gym to the members
    will show foreign key association
ERD IS ON THE FINAL, rows represent column names
    Foreign key should always be in the MANY

conn = sqlit3.conn ('fitness.db')

cursor = db.cursor()

by adding AUTOINCREMENT: will auto create numbers for the columns
    Foreign Key column should be a unique key
    
will need to put the identifying table if you are looking at more than two tables

OOP, MVC, SQL, reversing strings

by adding '%email%' will give you all the ones with THAT specific email address
by adding LIKE 'V%' it will give you all variables that start with that letter
by adding LIKE '%V' it will give you all variables that end with that letter
