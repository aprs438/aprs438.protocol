# Compressed Addressed Message Frames
Up to now, APRS has been unduly considered to be predominantly a one-way localisation technology.
This went to the point that many would mistake the letter "P" in the APRS acronym for "position" instead of "packet."
[Bob Bruninga WB4APR (SK)](http://www.aprs.org), the spiritual father of APRS, deeply resented this situation.

> _"APRS is not a vehicle tracking system.
> It is a two-way tactical real-time digital communications system between all assets in a network
> sharing information about everything going on in the local area."_

In Bob's view of APRS as being foremost a real-time situational and tactical tool, addressed messaging definitely merits its place.
Our goals is to render APRS messaging more popular by offering LoRa messaging pager terminals.

A compressed addressed message frame has a payload of **between 10 (for an empty ping) and 45 bytes.**
The available message length of 51 characters is largely sufficient for, for example, SOTA self-spotting using [APRS2SOTA](https://www.sotaspots.co.uk/Aprs2Sota_Info.php).

|_Callsign_|_SSID_,<br/>_Path Code_&nbsp;&<br/>_Data Type Code_|_Compressed Data_|
|:--------:|:-------------------------------------------------:|:---------------:|
|4 bytes|1 byte|5—40&nbsp;bytes|
|`CCCC`|`D`|`EEEEF(tttt…tttt)`|

where:

- `CCCC`: 4 bytes for the compressed **6 character** _Callsign_
- `D`: compresses into 1 byte:
  + the [_SSID_](#ssid) (between SSID 0 [none] and 15; included),
  + the [_Path Code_](#path-codes) (between path 0 [none] and 3; included), and
  + the [_Data Type Code_](#data-type-codes) = 3
- `EEEE`: 4 bytes for the compressed _Addressee_ (up to 6 character callsign)
- `F`: compresses into 1 byte:
  + the _Addressee SSID_ (between SSID 0 [none] and 15; included), and
  + the _Message No_ (from 0 to 15; included)
- `(tttt…tttt)`: up to 35 bytes of compressed text from a limited 42 character set, corresponding to a maximum of **51 uncompressed characters**

## Encoding and Decoding EEEE
The `EEEE` codec algorithms are identical to the [`CCCC` codec algorithms](#encoding-cccc).

## Encoding F
1. Perform input sanitisation, i.e. perform a modulus 16 operation on a _Message No_ originating from APRS‑IS.
2. Multiply the _SSID_ integer by&nbsp;16.
3. Then, algebraically add to this the _Message No_ integer.
4. Finally, convert the resulting integer to a single Base256 `F` byte.

## Decoding F
1. First, decode the given Base256 `F` byte to an integer.
2. The _SSID_ equals the integer quotient after [integer division](https://en.wikipedia.org/wiki/Division_(mathematics)#Of_integers) of the decoded integer by&nbsp;16.
3. Whereas the _Message No_ equals the [remainder](https://en.wikipedia.org/wiki/Remainder) of the decoded integer by&nbsp;16 ([modulo operation](https://en.wikipedia.org/wiki/Modulo_operation)).
4. When relaying the text message to APRS‑IS, the i‑gate will add the last digit of the minute the text message was received in front of the received _Message No._
