# APRS Frame Compression
LoRa, as a physical layer, permits sending any of the [256 characters](https://en.wikipedia.org/wiki/Extended_ASCII) from `\00` to `\ff`; double the amount of the [7‑bit, 128 ASCII character set](https://en.wikipedia.org/wiki/ASCII#Character_set). [AX.25](https://en.wikipedia.org/wiki/AX.25) ([packet radio](https://en.wikipedia.org/wiki/Packet_radio)) unnumbered information (UI) frames at the [data link layer](https://en.wikipedia.org/wiki/Data_link_layer) are no different in this respect.

However, as [previously demonstrated](#link_parameters), the effective data rate of LoRa SF11 is much slower than what can be achieved with 1200&nbsp;baud packet. Hence, the need to compress data with LoRa is more urgent. 

|[AX.25](https://en.wikipedia.org/wiki/AX.25) UI frame&nbsp;field|compression opportunities|
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

:::{note}
- _Source Address, SSID_ and _Data Type ID_ can be compressed into only 5 payload bytes, compared to 26 payload bytes with OE5BPA firmware.
- It is customary to compress latitude, longitude, symbol, course and speed using [Base91](https://en.wikipedia.org/wiki/List_of_numeral_systems#Standard_positional_numeral_systems), which results in another 13 payload bytes; _Data Type ID_ not included. **APRS&nbsp;438** will not differ in this respect.
- If APRS Mic-E compression were to be used instead, that would require another 16 payload bytes to compress latitude, longitude, symbol, course and speed; 7&nbsp;bytes in the superfluous _Destination&nbsp;Address_ and 9&nbsp;bytes in the _Information&nbsp;Field; Data Type ID_ included. Hence, this is not a good option.
:::

:::{toctree}
measurable_benefits.md
ccccd.md
geolocation.md
weather_report.md
tttt.md
status_report.md
item_report.md
addressed_message.md
codec.md
:::
