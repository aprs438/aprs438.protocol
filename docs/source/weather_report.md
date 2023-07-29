# Compressed Weather Report Frames
A compressed weather report frame has a payload of either exactly **28 or 29 bytes.**

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|23 (or 24) bytes|
|`CCCC`|`D`|`/XXXXYYYY_csgtrrppPPhbb(S)`|

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid-recommendations) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) = 0
- `/`: the _Symbol Table Identifier_
- `XXXX`: the Base91 compressed longitude
- `YYYY`: the Base91 compressed latitude
- `_`: the weather report _Symbol Code_
- `cs`: the compressed wind direction (in degrees) and sustained one-minute wind speed (in knots)
- `g`: gust (half of peak wind speed in km/h in the last 5 minutes)
- `t`: temperature (in kelvin above 173.15 K)
- `rr`: rainfall (in mm) over the past hour
- `pp`: rainfall (in mm) over the past 24 hours
- `PP`: rainfall (in mm) since midnight
- `h`: humidity (in %)
- `bb`: barometric pressure (in Pa above 50000)
- `(S)`: optionally, snowfall (in cm) over the past 24 hours

Notes:

- All numerical encodings are one or two byte Base256 encodings.
- Here is a fascinating list of [weather records](https://en.wikipedia.org/wiki/List_of_weather_records).
- The i‑gate adds the _Compression Type Byte_ `T` right behind `cs`.
- The parenthesis are not sent; these merely indicate optionality.
