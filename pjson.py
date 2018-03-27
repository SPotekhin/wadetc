import json

# строка которую будем парсить
json_string = """ {
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """

# распарсенная строка
parsed_string = json.loads(json_string)
for r in parsed_string["orderContents"]:
    print(r)