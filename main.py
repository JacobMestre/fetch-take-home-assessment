from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import date, time
from math import ceil
import uuid

api = FastAPI()

class Item(BaseModel):
    shortDescription: str = Field(..., pattern=r"^[\w\s\-]+$", description = "The short product description for the item.")
    price: str = Field(..., pattern = r"^\d+\.\d{2}$", description= "The total price paid for this item.")

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$", description = "The name of the retailer or store the receipt is from.")
    purchaseDate: date = Field(..., description = "The date of the purchase printed on the receipt.")
    purchaseTime: time = Field(..., description = "The time of the purchase printed on the receipt. 24-hour time expected.")
    items: List[Item] = Field(..., min_items=1)
    total: str = Field(..., pattern=r"^\d+\.\d{2}$", description = "The amount paid on the receipt.") 




@api.post('/receipts/process')

def process_receipt(receipt: Receipt):
    points = 0

    # Rule 1: 1 point for every alphanumeric character in the retailer name
    for character in receipt.retailer:
        if character.isalnum():
            points += 1
    print(f"After Rule 1: {points} points")
    # Rule 2: 50 points if the total is a round dollar amount
    if float(receipt.total).is_integer():
        points += 50
    print(f"After Rule 2: {points} points")
    # Rule 3: 25 points if the total is a multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
        points += 25
    print(f"After Rule 3: {points} points")
    # Rule 4: 5 points for every 2 items on the receipt
    points += 5* (len(receipt.items) // 2)
    print(f"After Rule 4: {points} points")

    # Rule 5: If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in receipt.items:
        stripped = item.shortDescription.strip()
        if len(stripped) % 3 == 0:
            points += ceil(float(item.price) * 0.2)
    print(f"After Rule 5: {points} points")
    
    # Rule 6: 6 points if the day in the purchase date is odd.
    if receipt.purchaseDate.day % 2 == 1:
        points += 6
    print(f"After Rule 6: {points} points")
    
    # Rule 7: 10 points if purchase is after 2:00PM and before 4:00pm

    if time(14,0) < receipt.purchaseTime < time(16,0):
        points += 10
    print(f"After Rule 7: {points} points")

    return points
