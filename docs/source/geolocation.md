# Compressed Geolocation Frames
A compressed geolocation frame has a payload of either exactly **17 or 19 bytes.**

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|12 (or 14) bytes|
|`CCCC`|`D`|`/XXXXYYYY$cs(aa)`|

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid-recommendations) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) = 0
- `/`: the _Symbol Table Identifier_
- `XXXX`: the Base91 compressed longitude
- `YYYY`: the Base91 compressed latitude
- `$`: the _Symbol Code_
- `cs`: the compressed course (in degrees) and speed (in knots)
- `(aa)`: optionally, the compressed altitude (in feet)

Note:

- Terrestrial objects do not require sending altitude data. Anyhow, GPS height readings are notorious for being significantly inaccurate.
- APRS-IS already understands Base91 `XXXXYYYY` compression when altitude `aa` is not used.
- In absence of altitude `aa`, the i‑gate adds the _Compression Type Byte_ `T` right behind `cs`.
- When `aa` is present, the i‑gate will instead need to decompress the whole frame and forward the uncompressed frame to APRS‑IS.
- The parenthesis are not sent; these merely indicate optionality.
