# USI-Lab

### Anypoint API def
<img width="497" alt="Screenshot 2022-12-06 at 6 17 26 PM" src="https://user-images.githubusercontent.com/56363189/205978723-81f8f581-95d1-44d4-9aac-1bff6bb12f35.png">

### RAML File
```yaml
#%RAML 1.0
title: DATE-API
version: v1
baseUri: http://localhost:8081
types:
  Foramted_Date:
    properties:
      date: string

/date:
  get:
    description: Transform Date
    queryParameters:
      day_week: number
      day_month: number
      month: number
      year: number
    responses:
        200:
          body:
            application/json:
              type: Foramted_Date
              example: { "date": "Monday, March 12, 2019" }
```