from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import uuid

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$", description = "The name of the retailer or store the receipt is from")
    #purchaseDate 
    #purchaseTime
    # items: 
    #total 

class Item(BaseModel):
    #shortDescription
    #price