# 220f0dd206544e3b85673729222906

from operator import index
import requests
import json
import pandas as pd
citys = ["London", "Tehran", "new_york", "Los_Angeles", "canada"]
col1 = "city"
col2 = "country"
col3 = "TEMP (c)"
col4 = "TEMP (f)"
col5 = "weather condition"
col6 = "ICON"
col7 = "DATE"
listCity = []
listCountry = []
listTempC = []
listTempf = []
listText = []
listDate = []

for i in range(len(citys)):
    Api = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key=220f0dd206544e3b85673729222906&q={citys[i]}&aqi=no").json()
    listCity.append(Api["location"]["name"])
    listCountry.append(Api["location"]["country"])
    listDate.append(Api["current"]["last_updated"].split(" ")[0])
    listTempC.append(Api["current"]["temp_c"])
    listTempf.append(Api["current"]["temp_f"])
    listText.append(Api["current"]["condition"]["text"])


data = pd.DataFrame({
    col1: listCity,
    col2: listCountry,
    col3: listTempC,
    col4: listTempf,
    col5: listText,
    col7: listDate
})
data.to_excel("test.xlsx", sheet_name="sheet1", index=False, na_rep='NaN')

print("DONE!")
