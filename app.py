#create employee model with attributes id, name min length 3, max length 50, email, dept min length 2, max length 20, salary > 0 and experience > 2, and create a list of employee send request body and store it into list and return list

from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel, EmailStr, Field

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=60)
    dept: str = Field(..., min_length=2, max_length=20)
    salary: float = Field(..., gt=0)
    experience: float = Field(..., gt=2)

employees = []

@app.post("/employee")
def create_employee(employee: Employee):
    employees.append(employee)
    return employees