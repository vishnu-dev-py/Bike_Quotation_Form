from fastapi import FastAPI, Body
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import uvicorn
import mysql.connector
app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=['*'], allow_methods = ['*']
)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql12",
    database="quotation"
)


@app.post("/submit")
async def submit(bForm_details:Dict = Body(...)):
    bForm_details = jsonable_encoder(bForm_details)
    try:
        cursor = connection.cursor()
        statement = "insert into quotation (name,mno,mail,bName,make,payment) values('{}',{},'{}','{}','{}','{}')".format(bForm_details['name'],
                                                                                            bForm_details['mno'],
                                                                                            bForm_details[
                                                                                                'mail'],bForm_details['bName'],bForm_details['make'],bForm_details['payment'])
        cursor.execute(statement)
        connection.commit()
        return "Form Submit Successfully...!"

    except Exception as e:
        return "Form Submit Failed...!"
