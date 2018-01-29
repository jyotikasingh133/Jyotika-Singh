#dictionary data type in python
>>> student={"name":"jyotika", "age":19}       #NAME,AGE: KEYS & JYOTIKA,AGE ARE VALUES#
>>> student
{'name': 'jyotika', 'age': 19}
>>> student["name"]
'jyotika'
>>> student["age"]=21              #AGE IS UPDATED FROM 19 TO 21
>>> student
{'name': 'jyotika', 'age': 21}
>>> student["college"]="ITS"       #WE ADDED ONE MORE KEY THAT IS COLLEGE IN THE DICTIONARY
>>> student
{'name': 'jyotika', 'age': 21, 'college': 'ITS'}
>>> del student["college"]         #DEL KEYWORD IS USED TO DELETE THE KEY COLLEGE#
>>> student                        
{'name': 'jyotika', 'age': 21}
>>> student.keys()                 #TOTAL NO. OF KEYS ARE MENTIONED USING KEYS() FUNCTION#
dict_keys(['name', 'age'])
>>> student.values()
dict_values(['jyotika', 21])       #TOTAL NO. OF VALUES ARE MENTIONED USING VALUES() FUNCTION#
>>> student1={"college":"ITS","rollno.":1}
>>> student1
{'college': 'ITS', 'rollno.': 1}
>>> student.update(student1)       #UPDATING THE DICTIONARY STUDENT USING UPDATE() F(n)#
>>> student
{'name': 'jyotika', 'age': 21, 'college': 'ITS', 'rollno.': 1}
>>> student.clear()                #CLEARING THE DICTIONARY USING CLEAR() F(n)#
>>> student
{}
>>> del student                  
>>> student
Traceback (most recent call last):           #AS WE HAVE DELETED THE DICTIONARY USING DEL() FUNCTION, 
  File "<pyshell#18>", line 1, in <module>    #SO, NOTHING IS LEFT AND THUS ERROR OCCURS#
    student
NameError: name 'student' is not defined
>>> 
