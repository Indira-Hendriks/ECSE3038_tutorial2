from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

data = [
 {
 "name": "John Doe",
 "occupation": "Software Engineer",
 "address": "123 Main St"
 },
 {
 "name": "Jane Smith",
 "occupation": "Data Scientist",
 "address": "456 Elm St"
 },
 {
 "name": "Michael Johnson",
 "occupation": "Web Developer",
 "address": "789 Oak St"
 },
 {
 "name": "Emily Brown",
 "occupation": "UX Designer",
 "address": "101 Maple Ave"
 },
 {
 "name": "David Lee",
 "occupation": "Product Manager",
 "address": "202 Pine St"
 },
 {
"name": "Sarah Taylor",
 "occupation": "Marketing Specialist",
 "address": "303 Cedar St"
 },
 {
 "name": "Chris Evans",
 "occupation": "Graphic Designer",
 "address": "404 Walnut St"
 },
 {
 "name": "Jessica White",
 "occupation": "Financial Analyst",
 "address": "505 Birch St"
 },
 {
 "name": "Matthew Miller",
 "occupation": "Systems Administrator",
 "address": "606 Spruce St"
 },
 {
 "name": "Amanda Martinez",
 "occupation": "HR Coordinator",
 "address": "707 Chestnut St"
 }
 ]
@app.get("/name")
async def get_all_names():
    names = [person["name"] for person in data]
    return {"names": names}

@app.get("/occupation")
async def get_occupations():
    occupations = [person["occupation"] for person in data]
    return {"occupations": occupations}

@app.get("/address")
async def get_addresses():
    addresses = [person["address"] for person in data]
    return {"addresses": addresses}
    

