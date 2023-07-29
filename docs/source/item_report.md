# Compressed Item Report Frames
A compressed item report frame has a payload of between **20 and 24 bytes.**

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|15—19 bytes|
|`CCCC`|`D`|`/XXXXYYYY$csTttt(tttt)`|

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid-recommendations) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) = 2
- `/`: the _Symbol Table Identifier_
- `XXXX`: the Base91 compressed longitude
- `YYYY`: the Base91 compressed latitude
- `$`: the _Symbol Code_
- `cs`: the compressed course and speed
- `ttt(tttt)`: 3 to 7 bytes for the compressed _Item Name_ (**between 3 and 9 characters** of the limited 42 character set)

Notes:

- The i‑gate adds the _Compression Type Byte_ `T` right behind `cs`.
- The parenthesis are not sent; these merely indicate optionality.
