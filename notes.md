[Microsoft Python Video Series](https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6)

# General

+ '#' hash for comment 
+ '\n' is new line


# strings

#### basics

capitalize is a string function that caps the first letter  
[Python Docs String functions](https://docs.python.org/2/library/string.html)

+ string_name = 'value'
+ print('hello ' + stringVal1 + ' ' + stringVal2)
+ print('hello ' + stringVal1.capitalize + ' ' + stringVal2)

#### format operator

[Python Docs Format](https://docs.python.org/2/library/string.html#formatspec)

All these give the same output
+ output = 'Hello, {} {}'.format(Var1, Var2)
+ output = 'Hello, {0} {1}'.format(Var1, Var2)
+ output = f'Hello, {Var1} {Var2}'

# Numbers

#### math ops

+ +-*/
+ ** == Exponent aka, the power of

#### different variable types / type conversion

This will not work, different data types
```
days_feb = 28
print(days_feb + 'text')
```


This will work decalring str() function to overide the number
```
days_feb = 28
print(str(days_feb) + 'text')
```

Var1 is string Var2 is int
```
Var1 = '5'
Var2 = 5
```
Types
+ str()
+ int()
+ float()


# Datetime

[Python Docs Datetime](https://docs.python.org/2/library/datetime.html?highlight=datetime#module-datetime)


Basic Datetime
```
from datetime import datetime, timedelta
current_date = datetime.now()
print('today is: ' + str(current_date))
print('todays day is: ' + str(current_date.day))
print('todays month is: ' + str(current_date.month))

```

Timedelta
```
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('yesterday was: ' str(yesterday))
```