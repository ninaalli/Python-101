
Format of CREATE TABLE if you were to use optional constraints:

create table "tablename"
("column1" "data type" 
         [constraint],
 "column2" "data type" 
         [constraint],
 "column3" "data type" 
        [constraint]);
 [ ] = optional
 
 
 Here are the MOST COMMON Data types:

char(size)	Fixed-length character string. Size is specified in parenthesis. Max 255 bytes.
varchar(size)	Variable-length character string. Max size is specified in parenthesis.
number(size)	Number value with a max number of column digits specified in parenthesis.
date	Date value
number(size,d)	Number value with a maximum number of digits of "size" total, with a maximum number of "d" digits to the right of the decimal.
  Example:
    create table employee
(first varchar(15),
 last varchar(20),
 age number(3),
 address varchar(30),
 city varchar(20),
 state varchar(20));
 
 
 =	Equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
<>	Not equal to
LIKE	*See note below


You have just started a new company. It is time to hire some employees. You will need to create a table that will contain the following information about your new employees: firstname, lastname, title, age, and salary. After you create the table, you should receive a small form on the screen with the appropriate column names. If you are missing any columns, you need to double check your SQL statement and recreate the table. Once it's created successfully, go to the "Insert" lesson.

create table 
  myemployees_ts0211
(firstname varchar(30),
 lastname varchar(30),
 title varchar(30),
 age number(2),
 salary number(8,2));



HOW TO SEARCH:
Display everyone's first name and their age for everyone that's in table.
select first, 
       age 
  from empinfo;
  
Display the first name, last name, and city for everyone that's not from Payson.
select first, 
       last, 
       city 
  from empinfo
where city <> 
  'Payson';
  
Display all columns for everyone that is over 40 years old.
select * from empinfo
       where age > 40;
       
Display the first and last names for everyone whose last name ends in an "ay".
select first, last from empinfo
       where last LIKE '%ay';
       
Display all columns for everyone whose first name equals "Mary".
select * from empinfo
       where first = 'Mary';
       
Display all columns for everyone whose first name contains "Mary".
select * from empinfo
       where first LIKE '%Mary%';
       
