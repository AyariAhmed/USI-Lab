from typing import Union
from fastapi import FastAPI, status, Response
from typing import List

app = FastAPI()

days_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

months_dict = {1: "January",
               2: "February",
               3: "March",
               4: "April",
               5: "May",
               6: "June",
               7: "July",
               8: "August",
               9: "September",
               10: "October",
               11: "November",
               12: "December"}


@app.get("/day")
def get_date(number: int):
    if number not in days_dict:
        body = f"""
        <error>
            <status>{status.HTTP_400_BAD_REQUEST}</status>
            <message>number {number} Couldn't be mapped to a day</message>
        </error>"""
        return Response(content=body, status_code=status.HTTP_400_BAD_REQUEST, media_type="application/xml")
    body = f"""
    <day>
     <number>{number}</number>
     <name>{days_dict[number]}</name>
    </day>"""
    return Response(content=body, status_code=status.HTTP_200_OK, media_type="application/xml")


@app.get("/month")
def get_month(number: int):
    if number not in months_dict:
        body = f"""
        <error>
            <status>{status.HTTP_400_BAD_REQUEST}</status>
            <message>number {number} Couldn't be mapped to a month</message>
        </error>"""
        return Response(content=body, status_code=status.HTTP_400_BAD_REQUEST, media_type="application/xml")
    body = f"""
    <month>
     <number>{number}</number>
     <name>{months_dict[number]}</name>
    </month>"""
    return Response(content=body, status_code=status.HTTP_200_OK, media_type="application/xml")
