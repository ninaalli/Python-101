=	Equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
<>	Not equal to
LIKE	*See note below

Enter select statements to:
Display the first name and age for everyone that's in the table.
select first,
        age
  from empinfo;

Display the first name, last name, and city for everyone that's not from Payson.
select first, 
        last, 
        city 
    from empinfo
  where city <> 'Payson';

Display all columns for everyone that is over 40 years old.
select * from empinfo 
    where age >40;

Display the first and last names for everyone whose last name ends in an "ay".
select first, last from empinfo 
  where last LIKE '%ay'
  
Display all columns for everyone whose first name equals "Mary".
select * from empinfo 
  where first = 'Mary';

Display all columns for everyone whose first name contains "Mary".
select * from empinfo
  where first like 'Mary%';

This will only select rows where the first name equals 'Eric' exactly.
select * from empinfo
  where first = 'Eric';
  
  


