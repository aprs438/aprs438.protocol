# Callsign, SSID, Path and Data Type Compression
Callsigns contain only capital letters, digits and empty spaces.
Up to six characters from such a 37 character set can easily be compressed into 4 `CCCC` bytes of the extended 256 character set.

Hence, all compressed APRS frames in this standard begin with 5 `CCCCD` bytes, irrespectively of the [_Data Type_](#data-type-codes).
Furthermore, **the compressed frame length is voluntarily limited by design to maximum 45&nbsp;bytes,** which leaves up to 40&nbsp;bytes of payload.
For certain _Data Types,_ the maximum length is even significantly lower.
A maximum frame length of 45&nbsp;bytes corresponds to a maximum airtime of 1.15&nbsp;s with SF11.

:::{important}
I‑gates should test whether the payload length of a received frame is in correspondence to the declared _Data Type_.
**Frames that do not comply, should be rejected.**

The combination of the four first `CCCC` Base256 _Callsign_ bytes and the in `D` declared _Data Type_ with the corresponding payload length form **the key** —so to speak— to the i‑gate.
This is what allows for a headerless frame design.
It prevents the i‑gate from relaying frames that are not intended for this compressed frame link.
:::

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|≤&nbsp;40&nbsp;bytes|
|`CCCC`|`D`||

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) (between type 0 and 3; included)

## Base37
Base37 consist out of the following 37 ordered digits, starting with a space character:

```python
digits = ' 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

(encoding-cccc)=
## Encoding CCCC
1. Perform input sanitisation and right padding with spaces up to 6 characters.
2. Treat the given 6&nbsp;character callsign string as a Base37 encoding. Decode it first to an integer.
3. Then, encode this integer as a 4&nbsp;byte Base256 `CCCC` bytestring.

## Decoding CCCC
1. First, decode the given 4&nbsp;byte Base256 `CCCC` bytestring to an integer.
2. Then, encode this integer as a 6&nbsp;character Base37 string, corresponding to the callsign.

## Encoding D
1. Perform input sanitisation.
2. Multiply the _SSID_ integer by&nbsp;16.
3. Multiply the _Path Code_  by&nbsp;4.
4. Then, algebraically add to these intermediate results to the _Data Type Code_ integer from {numref}`table-data-type-codes`.
5. Finally, convert the resulting integer to a single Base256 `D` byte.

## Decoding D
1. First, decode the given Base256 `D` byte to an integer.
2. The _SSID_ equals the integer quotient after [integer division](https://en.wikipedia.org/wiki/Division_(mathematics)#Of_integers) of the decoded integer by&nbsp;16.
3. The [remainder](https://en.wikipedia.org/wiki/Remainder) of above integer division is subjected to a second integer division by&nbsp;4.
4. The _Path Code_ equals the integer quotient of this second integer division.
5. Whereas the _Data Type Code_ equals the remainder this second integer division.

(ssid)=
## SSID Recommendations
A secondary station identifier is a number in the range 0-15, as an adjunct to the station _Callsign_.
Similarly as with IEEE 802.11 wireless networks, an APRS SSID identifies a set of APRS station capabilities.

:::{table} SSID recommendations
:name: table-ssid
|_SSID_|APRS station type|
|:----:|:---------------:|
|0|primary station; usually fixed and message capable|
|1|generic additional station, digi, mobile, wx, etc.|
|2|generic additional station, digi, mobile, wx, etc.|
|3|generic additional station, digi, mobile, wx, etc.|
|4|generic additional station, digi, mobile, wx, etc.|
|5|other networks (D‑STAR, DMR, smartphones etc.)|
|6|special activity, satellite ops, camping, etc.|
|7|walkie talkies, HTs or other human portable|
|8|boats, sailboats, RVs or second main mobile|
|9|primary mobile (usually message capable)|
|10|Internet, **(LoRa) i‑gates,** echolink, Winlink, AVRS, APRN, etc.|
|11|balloons, aircraft, spacecraft, etc.|
|12|APRStt, DTMF, RFID, devices, **one‑way (LoRa) trackers,** etc.|
|13|weather stations|
|14|truckers or generally full time drivers|
|15|generic additional station, digi, mobile, wx, etc.|
:::

:::{tip}
One-way trackers best use the 12 one‑way _SSID_ indicator,
whereas _SSID_ 9 usually means a ham with full communication capabilities; both APRS message and voice.
:::

(data-type-codes)=
## Data Type Codes
Of all the _Data Types_ defined in the [APRS Protocol Reference](https://hamwaves.com/prs/doc/2000.aprs.1.01.pdf), a subset was selected, based on popularity and suitability for LoRa.

:::{table} Data Type Codes
:name: table-data-type-codes
|_Data Type_|_ID_ (not&nbsp;used)|_Data Type Code_|payload|
|:---------:|:------------------:|:--------------:|:-----:|
|compressed [**geolocation**](#geolocation) — no&nbsp;timestamp|`!`&nbsp;or&nbsp;`=`|0|17 or 19 bytes|
|complete [**weather report**](#weather_report) — with compressed geolocation, no&nbsp;timestamp|`!`&nbsp;or&nbsp;`=`|0|28 or 29 bytes|
|[**status report**](#status_report) (≤&nbsp;28&nbsp;characters)|`>`|1|6—24 bytes|
|[**item report**](#item_report) — with compressed geolocation|`)`|2|20—24 bytes|
|[**addressed message**](#addressed_message) (≤&nbsp;51&nbsp;characters)|`:`|3|10—45 bytes|
:::

:::{note}
- APRS 438 will not transmit any _ID_ byte over LoRa. The _ID_ will be added at the i‑gate.
- Weather reports use the same _IDs_ and _Data Type Codes_ as position reports but with a _Symbol Code_ `_` overlay.
- A _Symbol Table Identifier_ nor a _Symbol Code_ can be compressed.
:::

(path-codes)=
## Path Codes
The path codes are of little importance to LoRa APRS&nbsp;438.
Path codes mainly serve to instruct (VHF) APRS digipeaters.
These digipeaters may be co‑located with a LoRa i‑gate or may obtain packets from Internet APRS‑IS.
See also {ref}`no-digipeating`.

:::{table} Data Type Codes
:name: table-path-codes
|station|recommended `n-N` paradigm path|_Path Code_|
|:-----:|:-----------------------------:|:---------:|
|no digipeating||0|
|metropolitan fixed, mountain expeditions, balloons&nbsp;& aircraft|`WIDE2-1`|1|
|extremely remote fixed|`WIDE2-2`|N/A|
|metropolitan mobile|`WIDE1-1,WIDE2-1`|2|
|extremely remote mobile|`WIDE1-1,WIDE2-2`|N/A|
|space satellites|`ARISS,WIDE2-1`|3|
:::

:::{important}
- The first `n` digit in `n-N` paradigm paths indicates the coverage level of the digipeater, whereby `1` is for local fill‑in digipeaters and `2` is for county-level digipeaters.
- The second `N` digit indicates the number of repeats at the indicated coverage level.
:::
