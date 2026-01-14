from pydantic import BaseModel , EmailStr , Field
from typing import Optional

class Student(BaseModel):
    name:str
    age: Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0 , lt=10 , default=5 , description='A decimal value representing the cgpa of the student , if the pattern is ot followed then do not sccept the value')

new_student = {'name':'anurag' , 'age' : 25 ,'email':'anurag@gmail.com' , 'cgpa':1} #data must be string other wise it will throw error

student = Student(**new_student)
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()