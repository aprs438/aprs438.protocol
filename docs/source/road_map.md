(road-map)=
# Road Map

## Tracker

|firmware|completed|feature|payload|compatible with OE5BPA i‑gate|
|:------:|:-------:|:-----:|:-----:|:---------------------------:|
|v0.0.0|✓|original [OE5BPA tracker](https://github.com/lora-aprs/LoRa_APRS_Tracker)|113 bytes|✓|
|v0.1.0|✓|byte-saving [`tracker.json`](https://github.com/aprs434/lora.tracker/blob/master/data/tracker.json)|87 bytes|✓|
|v0.2.0|✓|fork of the [OE5BPA tracker](https://github.com/lora-aprs/LoRa_APRS_Tracker)<br/>with significantly less transmitted&nbsp;bytes|44 bytes|✓|
|v0.3.0|✓|[Base91](https://en.wikipedia.org/wiki/List_of_numeral_systems#Standard_positional_numeral_systems) compression of  location, course&nbsp;and speed&nbsp;data|31 bytes|✓|
|[v0.4.0](https://github.com/aprs434/lora.tracker)|✓|removal of the transmitted [newline](https://en.wikipedia.org/wiki/Newline) `\n`&nbsp;character at&nbsp;frame&nbsp;end|30 bytes|✓|
|v1.0.0|Q3 2023|frame compression|17 bytes|Use the APRS&nbsp;438 i‑gate!|

:::{note}
Currently, the APRS&nbsp;434 tracker is still compatible with the i-gate developed by Peter Buchegger, OE5BPA.
:::

:::{important}
The release of frame compression will require migration to [new frequencies, SF11](#link-parameters) and use of the APRS&nbsp;438 i‑gate.
:::

Compressed geolocation frames are already flawlessly received by the APRS&438 terminal and being forwarded to APRS‑IS.
The release of tracker firmware is kept on hold until the i‑gate firmware gets released.


## Terminal
![](/images/tui.read_msg.jpg)

Currently under development.

Ricardo Guzman Christie, CD2RXU, brought this project in a well advanced stage.
Together with Matthias Brändli, HB9EGM, both are now working on the ESP32 Arduino C++ implementation of the text compression algorithm.


## I-Gate
Currently under development.

Works, but needs some more attention and care. Manfred Heindl, DC2MH, recently offered Ricardo help with this.
