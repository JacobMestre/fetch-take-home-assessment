from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import date
import uuid

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$", description = "The name of the retailer or store the receipt is from")
    purchaseDate: date = Field(..., description = "The date of the purchase printed on the receipt")
    #purchaseTime
    # items: 
    #total 

class Item(BaseModel):
    #shortDescription
    #price