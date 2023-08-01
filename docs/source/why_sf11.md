# Why SF11
Depending on how popular APRS over LoRa becomes and on how intensely it will get used,
there might come a time when the LoRa channel gets saturated.
Unlike packet radio, LoRa has no carrier sensing capability.
Sending longer text messages, even when compressed, may aggravate the situation.

In order to prevent such a congestion, APRS&nbsp;438 decided to **only employ SF11.**

Doing so, effectively doubles the data rate over SF12.
It also saves 50% on airtime and batteries.
The slight range penalty from switching from SF12 to SF11 is in most circumstances absolutely acceptable,
provided the availability of i‑gates in an area is sufficient.

With a payload of only 17&nbsp;bytes, the compressed geolocation frame is perfectly geared towards
taking advantage of the reduced airtime offered by SF11 (see [graph](#fig-airtime)).

Unfortunately, most cheap i‑gates currently in use by ham operators are only capable of receiving one preset spreading factor.
Therefore, the choice was made to use SF11 exclusively.
Considering what some members of the amateur radio community have come to expect of LoRa,
the faster data rate offered by SF11 is more than warranted.
