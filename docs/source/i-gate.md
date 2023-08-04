# I-Gate


## I-Gate Functionality
I-gates will, <u>in the listed order of priority</u>, and with respect for the received _Path Code:_

1. **Reject** any received frame which payload length does not correspond to the declared _Data Type_.
2. Keep a **list of all stations heard** on the uplink channel over the last hour. This implies that all end devices need to send a geolocation frame or at least a status report when switched on and when not having transmitted over the course of an hour.
3. Transmit on the downlink channel all frames heard on the uplink channel, **other than addressed text messages.**
4. Transmit **text messages addressed to end devices the i‑gate heard recently.** These addressed text messages may originate from the uplink, from an attached packet APRS digipeater or from Internet APRS‑IS.
5. Transmit **situational awareness frames** from an attached packet APRS digipeater or APRS‑IS, when these are applicable to the geographical coverage area of the i‑gate.

When the downlink channel gets saturated, above listed order of priority applies in terms of dropping frames or keeping a frame wait list stack.


(no-digipeating)=
## No Digipeating on the Uplink
:::{caution}
**<u>REFRAIN</u> from digipeating on the uplink frequency!**
:::

Since LoRa SF11 is a slow data rate mode, digipeating on the LoRa uplink channel quickly leads to unwanted channel congestion.
Unlike AX.25 packet radio, LoRa does not offer [carrier sensing (CS)](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access);
only [channel activity detection (CAD)](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/channel-activity-detection-ensuring-your-lora-packets-are-sent/how-to-ensure-your-lora-packets-are-sent-properly/).

Also consider that:

- LoRa was merely intended as an **Internet access technology.**
- Most LoRa gateways are connected to the APRS‑IS Internet server network and many users are merely interested in reaching APRS‑IS.
- There are hardly any low power portable LoRa devices able to display situational awareness in relation to other LoRa devices.
- Only in extremely remote areas without Internet access, digipeating may be considered, but only on the downlink frequency or the alternative downlink frequency.

:::{important}
Hence, `n-N` paradigm paths could be interpreted foremost as crossover AX.25 packet digipeating paths for any (VHF) digipeater co‑located with the LoRa (i‑)gate.
:::

:::{hint}
However, suppose meshing or `n-N` paradigm digipeating were to be allowed on a single LoRa channel; even for trackers.
This would offer interesting emergency capabilities when no Internet is available. However, this would absolutely require switching from SF11 to the higher data rate offered by SF10, as demonstrated in {numref}`table-airtime`. In such a scenario, _Path Code_ stands for the LoRa device communicating its digipeating requirements to the mesh network.
:::
