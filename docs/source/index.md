# APRS 438

:::{image} /images/aprs438.round.png
:alt: APRS 438 logo
:width: 160px
:align: left
:::
Welcome to the home of **APRS&nbsp;438**,
the 438&nbsp;MHz amateur radio LoRa [automatic packet reporting system](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System) that **extends range by saving bytes.**

Unlike some other [ham radio](https://en.wikipedia.org/wiki/Amateur_radio) LoRa APRS projects,
this project aims at **deploying [LoRa](https://en.wikipedia.org/wiki/LoRa) the way it was intended;**
namely by being frugal about the number of bytes put on air.
Doing so, reaps a number of benefits:
<br clear="all"/>

- less airtime,
- increased battery life,
- higher chances of good packet reception,
- hence, increased range,
- lower probability of packet collisions,
- therefore, more channel capacity.

In dense urban environments and/or on flat terrain, **LoRa works best when the data payload is kept to a strict minimum.**
This can be achieved by taking full advantage of all 256 characters available for transmission with LoRa.
The APRS frame compression protocols presented in this [white paper](https://en.wikipedia.org/wiki/White_paper) aim precisely at doing that; for LoRa, _or any other data link with an extended character set._

ESP32 firmware adhering to these compression protocols is provided as well:

- Tracker documentation
- Terminal documentation
- i-gate documentation

:::{caution}
Unlike the vast majority of [other LoRa projects](https://thethingsnetwork.org), the firmware of this project employs **licensed frequency spectrum** exclusive to the use of [amateur radio](https://en.wikipedia.org/wiki/Amateur_radio). **You need a valid amateur radio license to be able to use APRS 438 firmware.**
Contact your national government or local amateur radio club to find out how to obtain an amateur radio license.
:::

:::{attention}
This document is still subject to change. Check regularly for changes and added clarifications.
:::

:::{toctree}
link_parameters.md
frame_compression.md
i-gate.md
revisions.md
road_map.md
future_plans.md
firmware.md
hardware.md
social.md
acknowledgements.md
:::
