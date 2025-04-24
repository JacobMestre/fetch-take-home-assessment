from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import date, time
import uuid

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$", description = "The name of the retailer or store the receipt is from")
    purchaseDate: date = Field(..., description = "The date of the purchase printed on the receipt")
    purchaseTime: time = Field(..., description = "The time of the purchase printed on the receipt. 24-hour time expected")
    items: List[Item] = Field(..., min_items=1)
    total: str = Field(..., pattern=r"^\\d+\\.\\d{2}$", description = "The amount paid on the receipt") 

class Item(BaseModel):
    #shortDescription
    #price