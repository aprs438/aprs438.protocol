# APRS Frame Compression
This [white paper](https://en.wikipedia.org/wiki/White_paper) presents an open standard for APRS frame compression.

As a physical layer, LoRa permits sending any of the [256 characters](https://en.wikipedia.org/wiki/Extended_ASCII) from `\00` to `\ff`. This is double the amount of the [7‑bit, 128 ASCII character set](https://en.wikipedia.org/wiki/ASCII#Character_set). Hence, there are ample opportunities for compressing [AX.25](https://en.wikipedia.org/wiki/AX.25) ([packet radio](https://en.wikipedia.org/wiki/Packet_radio)) unnumbered information (UI) frames at the [data link layer](https://en.wikipedia.org/wiki/Data_link_layer), namely:

|[AX.25](https://en.wikipedia.org/wiki/AX.25) UI frame&nbsp;field|compression opportunities with&nbsp;LoRa|
|:-:|:-:|
|_Flag_|**not required**; explicit header provided by LoRa|
|_Destination Address_|**not required**; software version provided by the i‑gate|
|_Source Address_|6 out of **37** possible characters: 26 capital letters + 10 digits + space|
|_SSID_|1 out of [**16** hexadecimal digits](https://en.wikipedia.org/wiki/Hexadecimal)|
|_Digipeater Address_|any out of [**5** recommended `n-N` paradigm paths](#path-codes)|
|_Control Field_|**not required**|
|_Protocol ID_|**not required**|
|_Information Field_|256 characters of which [**95** printable ASCII characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters)<br/>first character = [_Data Type ID_](#data-type-codes)|
|_Frame Check Sequence_|**not required**; [FEC](https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction)&nbsp;& [CRC](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) are provided by LoRa|
|_Flag_|**not required**|

- _Source Address, SSID_ and _Data Type ID_ can be compressed into only 5 payload bytes, compared to 26 payload bytes with OE5BPA firmware.
- It is customary to compress latitude, longitude, symbol, course and speed using [Base91](https://en.wikipedia.org/wiki/List_of_numeral_systems#Standard_positional_numeral_systems), which results in another 13 payload bytes; _Data Type ID_ not included. **APRS&nbsp;434** will not differ in this respect.
- If APRS Mic-E compression were to be used instead, that would require another 16 payload bytes to compress latitude, longitude, symbol, course and speed; 7&nbsp;bytes in the superfluous _Destination&nbsp;Address_ and 9&nbsp;bytes in the _Information&nbsp;Field; Data Type ID_ included. Hence, this is not a good option.

```{toctree}
measurable_benefits.md
link_parameters.md
callsign-ssid-path-data_type.md
geolocation.md
weather_report.md
compressed_text.md
status_report.md
item_report.md
addressed_message.md
```
