# Link Parameters
The following LoRa link parameters are proposed for amateur radio LoRa APRS&nbsp;438:

|LoRa parameter|uplink|downlink|
|:------------:|:----:|:------:|
|frequency|438.025&nbsp;MHz|439.625&nbsp;MHz|
|use|APRS‑IS&nbsp;uplink&nbsp;access & client‑to‑client|i‑gate&nbsp;downlink & digipeating for situational&nbsp;awareness|
|SF|11|11|
|BW|125&nbsp;000&nbsp;Hz|125&nbsp;000&nbsp;Hz|
|CR|1 (5/4)|1 (5/4)|
|preamble sync length|8&nbsp;symbols|8&nbsp;symbols|
|preamble sync&nbsp;word|`0x12`|`0x12`|
|header mode|explicit (20&nbsp;bits)|explicit (20&nbsp;bits)|
|[CRC](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)|on (16&nbsp;bits)|on (16&nbsp;bits)|
|[IQ](https://en.wikipedia.org/wiki/In-phase_and_quadrature_components) polarisation|normal|inversed|

- Above proposed frequencies are outside the interfering 433—435&nbsp;MHz [ISM band](https://en.wikipedia.org/wiki/ISM_radio_band). Moreover, these frequencies maintain sufficient spectrum separation among one another as well as from the ubiquitous car lock keys and home weather stations on 433.920&nbsp;MHz.
- In order to achieve a maximum range, [Semtech](https://en.wikipedia.org/wiki/Semtech) —&nbsp;the company that developed LoRa&nbsp;— recommends selecting the maximum spreading factor {math}`SF = 12`. However, SF12 is extremely slow, offering only a mere 36.6&nbsp;byte/s.
- {math}`SF = 11` corresponds to 11&nbsp;raw bits per symbol. Therefore, each symbol (or frequency chirp) holds {math}`2^{11} = 2048\,\text{chips}`.
- Likewise, the bandwidth is set to the smallest commonly available bandwidth among all LoRa ICs, namely {math}`BW = 125\,\text{kHz}`. This is by definition also the chip rate {math}`R_c = BW`.
- To avoid any further overhead in an already slow mode, the [forward error correction (FEC)](https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction) coding rate is kept at {math}`CR = 1`, which corresponds to {math}`\frac{data}{data + FEC} = \frac{4}{5}`.
- It was observed that amateur radio predominantly employs the LoRa sync word `0x12`; which is manufacturer recommended for private networks, and differs from LoRaWAN.

With these settings, the symbol rate is:

```{math}
R_s = \frac{R_c}{2^{SF}} = \frac{BW}{2^{SF}} = \frac{125\,000}{2^{11}} \approx 61\,\text{symbols/s}
```

Whereas the effective data rate {math}`DR` or bit rate {math}`R_b` can be calculated as follows:

```{math}
DR = R_b =  \frac{BW}{2^{SF}} \cdot SF \cdot \frac{4}{4 + CR} = \frac{125\,000}{2^{11}} \cdot 11 \cdot \frac{4}{5} \approx 537\,\text{bits/s} \approx 67\,\text{byte/s}
```

Above parameters seem adequate for sending LoRa frames with short, compressed payloads over the next longest possible distance when the number of participant nodes is relatively low.

:::{seealso}
For an in depth tutorial slide series about LoRa (and LoRaWAN), please refer to [Mobilefish.com](https://www.mobilefish.com/developer/lorawan/lorawan_quickguide_tutorial.html), also available in video format on [YouTube](https://youtube.com/playlist?list=PLmL13yqb6OxdeOi97EvI8QeO8o-PqeQ0g).
:::

## Why 438&nbsp;MHz and Up

## Why SF11
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
taking advantage of the reduced airtime offered by SF11 (see [graph](#airtime-reduction)).

Unfortunately, most cheap i‑gates currently in use by ham operators are only capable of receiving one preset spreading factor.
Therefore, the choice was made to use SF11 exclusively.
Considering what some members of the amateur radio community have come to expect of LoRa,
the faster data rate offered by SF11 is more than warranted.
