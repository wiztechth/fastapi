from fastapi import FastAPI

from enum import Enum

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome to my web site, {name}"

class AvailableCuisines(str, Enum):
    somtum = "somtum"
    tomyum = "tomyum"
    curry = "curry"

food_items = {
    "somtum" : ["มะละกอ", "มะเขือเทศ"],
    "tomyum" : ["กุ้ง", "ตะไคร้-ใบมะกรูด"],
    "curry" : ["เนื้อสัน", "เครื่องแกง"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return (food_items.get(cuisine))

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return {'discount_amount': coupon_code.get(code)}
