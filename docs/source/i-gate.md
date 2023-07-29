# I-Gate

## No Digipeating on the Uplink Channel
> **⚠ <u>REFRAIN</u> from digipeating on the uplink LoRa channel!**
> Since LoRa is a slow data rate mode, digipeating on the LoRa 438.100&nbsp;MHz uplink channel quickly leads to unwanted channel congestion.
> Unlike AX.25 packet radio, LoRa does not offer [carrier sensing (CS)](https://en.wikipedia.org/wiki/Carrier-sense_multiple_access);
> only [channel activity detection (CAD)](https://lora-developers.semtech.com/documentation/tech-papers-and-guides/channel-activity-detection-ensuring-your-lora-packets-are-sent/how-to-ensure-your-lora-packets-are-sent-properly/)

Also consider that:

- LoRa was merely intended as an Internet access technology.
- Most LoRa gateways are connected to the APRS‑IS Internet server network and many users are merely interested in reaching APRS‑IS.
- There are hardly any, if any, low power portable LoRa devices able to display situational awareness in relation to other LoRa devices.
- Only in extremely remote areas without Internet access, digipeating may be considered, but only on the downlink channel 438.300&nbsp;MHz.

Hence, below `n-N` paradigm paths could be interpreted foremost as crossover AX.25 packet digipeating paths for any (VHF) digipeater co‑located with the LoRa (i‑)gate.

However, suppose meshing or `n-N` paradigm digipeating were to be allowed on a single LoRa channel; even for trackers. This would offer interesting emergency capabilities when no Internet is available. However, this would absolutely require switching from SF12 to the higher data rate offered by SF11 [as explained before](#considerations-for-switching-to-sf11). In such a scenario, below table represents the LoRa device communicating its digipeating requirements to the mesh network.


## I-Gate Functionality
I-gates will, in the listed order of priority, and with respect for the received _Path Code:_

1. Keep a list of all stations heard on the uplink channel over the last hour. This implies that all clients need to send a geolocation frame or at least a status report when switched on and when not having transmitted over the course of an hour.
2. Transmit on the downlink channel all frames heard on the uplink channel, other than addressed text messages.
3. Transmit text messages addressed to clients it heard recently. These addressed text messages may originate from the uplink, from an attached packet APRS digipeater or from Internet APRS‑IS.
4. Transmit situational awareness frames from an attached packet APRS digipeater or APRS‑IS, when these apply to the geographical coverage area of the i‑gate.

When the downlink channel gets saturated, above listed order of priority applies.
