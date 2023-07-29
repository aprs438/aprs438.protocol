# Compressed Status Report Frames
A compressed status report frame has a payload of between **6 and 24 bytes.**

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|1—19&nbsp;bytes|
|`CCCC`|`D`|`t(tttt…tttt)`|

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid-recommendations) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) = 1
- `t(tttt…tttt)`: between 1 and 19 bytes of compressed text from a limited 42 character set, corresponding to a maximum of **28 uncompressed characters**
