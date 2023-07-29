# APRS 434

```{image} /images/aprs434.logo.png
:alt: APRS 434 logo
:width: 160px
:align: left
```
Welcome to the home of **APRS&nbsp;434**,
the 434&nbsp;MHz LoRa APRS amateur radio project that **extends range by saving bytes.**

Unlike some other ham radio LoRa APRS projects,
this project aims at **deploying LoRa the way it was intended;**
namely by being frugal about the number of bytes put on air.
Doing so, reaps a number of benefits:
<br clear="all"/>

- less airtime,
- increased battery life,
- higher chances of good packet reception,
- hence, increased range,
- lower probability of packet collisions,
- therefore, more channel capacity.

In dense urban environments and/or on flat terrain, LoRa works best when the data payload is kept to a strict minimum.
This can be achieved taking full advantage of all 256 characters available for transmission with LoRa.
The APRS frame compression protocols presented below aim precisely at doing that;
for LoRa, _or any other data link with an extended character set._

ESP32 [**tracker, text terminal and i‑gate firmware**](#esp32-firmware-downloads) adhering to these compression protocols is provided as well.

:::{attention}
This document is still subject to change. Check regularly for added clarifications and minor changes.
:::

```{toctree}
frame_compression.md
measurable_benefits.md
link_parameters.md
callsign-ssid-path-data_type.md
geolocation.md
weather_report.md
compressed_text.md
status_report.md
item_report.md
addressed_message.md
i-gate.md
hardware.md
social.md
acknowledgements.md
revisions.md
```
