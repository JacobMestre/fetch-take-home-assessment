from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import uuid

class Receipt(BaseModel):
    #retailer
    #purchaseDate 
    #purchaseTime
    #items (min of 1)
    #total 

class Item(BaseModel):
    #shortDescription
    #price