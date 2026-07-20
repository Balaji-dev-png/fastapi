from fastapi import FastAPI
from pydantic.v1 import BaseModel

app = FastAPI()

@app.get("/")
def greet():
    return "welcome to FastAPI!"


@app.post("/contact")
def contact():
    return "Contact us at"

@app.get("/about")
def about():
    return "This is a FastAPI application."


@app.get("/home")
def home():
    return "this is home page"










#http methods : post, get, put, delete, patch

@app.post("/postmethod")
def post_method():
    return "this is post method"


@app.put("/putmethod")
def put_method():
    return "this is put method"

@app.delete("/deletemethod")
def delete_method():
    return "this is delete method"


@app.patch("/patchmethod")
def patch_method():
    return "this is patch method"



@app.get("/query")
def query(name: str, age: int):
    return {"name": name, "age": age}









#parameter : 
#path parameter
#when we want specific data from the url we use path parameter
@app.get("/students/{id}")
def path_param(id: int):

    #create a list of student in which each student contains id, name, dept, cgpa and is entered id in url is in list return student data else return student not found

    students = [
        {"id": 0, "name": "John", "dept": "CSE", "cgpa": 3.5},
        {"id": 1, "name": "Jane", "dept": "ECE", "cgpa": 3.8},
        {"id": 2, "name": "Bob", "dept": "MECH", "cgpa": 3.2},
        {"id": 3, "name": "Alice", "dept": "CIVIL", "cgpa": 3.9},
        {"id": 4, "name": "Tom", "dept": "EEE", "cgpa": 3.6}
    ]

    for std in students:
        if std["id"] == id:
            return f"student id : {std}"

    return "student not found"




#query parameter
@app.get("/student")
def query_param(dept: str, cgpa: float):
    students = [
        {"id": 0, "name": "John", "dept": "CSE", "cgpa": 5.9},
        {"id": 1, "name": "Jane", "dept": "ECE", "cgpa": 3.8},
        {"id": 2, "name": "Bob", "dept": "MECH", "cgpa": 3.2},
        {"id": 3, "name": "Alice", "dept": "CIVIL", "cgpa": 3.9},
        {"id": 4, "name": "Tom", "dept": "EEE", "cgpa": 3.6}
    ]

    student = []
    for std in students:
        if std["dept"] == dept and std["cgpa"] >= cgpa:
            student.append(std)

    return student







#pydantic : automatic data validation and serialization
#where we pass request body or getting response body
#there is a high chance that user will enter wrong details in wrong field
from pydantic import BaseModel, EmailStr, Field

class student(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50)
    dept: str = Field(..., min_length=3, max_length=50)
    cgpa: float = Field(..., gt=0, lt=10)
    email: EmailStr

#create a list of student send request body and store it into list and return list

students = []


@app.post("/student")
def addstudent(student: student):
    students.append(student)
    return students
