# Link Parameters
The following LoRa link parameters are proposed for amateur radio LoRa APRS&nbsp;438:

:::{table} APRS 438 link parameters
:name: table-link-parameters
:width: 100%
|LoRa parameter|uplink|downlink|alternative downlink|
|:------------:|:----:|:------:|:------------------:|
|frequency|438.050&nbsp;MHz|439.550&nbsp;MHz|434.425&nbsp;MHz|
|spreading factor SF|11|11|11|
|bandwith BW|125&nbsp;kHz|125&nbsp;kHz|125&nbsp;kHz|
|code rate [CR](https://en.wikipedia.org/wiki/Code_rate)|1 (5/4)|1 (5/4)|1 (5/4)|
|preamble sync length|8&nbsp;symbols|8&nbsp;symbols|8&nbsp;symbols|
|preamble sync&nbsp;word|`0x12`|`0x12`|`0x12`|
|header mode|explicit (20&nbsp;bits)|explicit (20&nbsp;bits)|explicit (20&nbsp;bits)|
|[CRC](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)|on (16&nbsp;bits)|on (16&nbsp;bits)|on (16&nbsp;bits)|
|[IQ](https://en.wikipedia.org/wiki/In-phase_and_quadrature_components) polarisation|normal|inversed|inversed|
:::

:::{note}
Above preferred frequencies are outside the interfering 433—435&nbsp;MHz [ISM band](https://en.wikipedia.org/wiki/ISM_radio_band).
:::

:::{attention}
The alternative downlink frequency is only intended for those countries where amateur radio is not allowed to transmit (e.g. Austria) or has secondary status (e.g. The Netherlands) on the preferred downlink frequency. Terminal-type end devices will expose an option to select the alternative downlink.

**I‑gates using the alternative downlink frequency are fervently advised to emit at higher power levels (e.g. 7.5&nbsp;W)** to overcome the interference caused by ISM systems.
:::

:::{note}
- In order to achieve a maximum range, [Semtech](https://en.wikipedia.org/wiki/Semtech) —&nbsp;the company that developed LoRa&nbsp;— recommends selecting the maximum spreading factor $SF = 12$. However, SF12 is extremely slow, offering only a mere 36.6&nbsp;byte/s.
- $SF = 11$ corresponds to 11&nbsp;raw bits per symbol. Therefore, each symbol (or frequency chirp) holds $2^{11} = 2048\,\text{chips}$.
- Likewise, the bandwidth is set to the smallest commonly available bandwidth among all LoRa ICs, namely $BW = 125\,\text{kHz}$. This is by definition also the chip rate $R_c = BW$.
- To avoid any further overhead to an already slow mode, the [forward error correction (FEC)](https://en.wikipedia.org/wiki/Error_correction_code#Forward_error_correction) [code rate](https://en.wikipedia.org/wiki/Code_rate) is kept at $CR = 1$, which corresponds to $\frac{data}{data + FEC} = \frac{4}{5}$.
- It was observed that amateur radio predominantly employs the LoRa sync word `0x12`; which is manufacturer recommended for private networks, and differs from the `0x34` for a LoRaWAN.
:::

With these settings, the symbol rate is:

$$R_s = \frac{R_c}{2^{SF}} = \frac{BW}{2^{SF}} = \frac{125\,000}{2^{11}} \approx 61\,\text{symbols/s}$$

Whereas the effective data rate $DR$ or bit rate $R_b$ can be calculated as follows:

$$DR = R_b =  \frac{BW}{2^{SF}} \cdot SF \cdot \frac{4}{4 + CR} = \frac{125\,000}{2^{11}} \cdot 11 \cdot \frac{4}{5} \approx 537\,\text{bits/s} \approx 67\,\text{byte/s}$$ (eq-data-rate)

Above parameters are adequate for sending LoRa frames with short, compressed payloads over the almost longest possible distance when the number of participant nodes is relatively low.

:::{seealso}
For an in depth tutorial slide series about LoRa (and LoRaWAN), please refer to [Mobilefish.com](https://www.mobilefish.com/developer/lorawan/lorawan_quickguide_tutorial.html), also available in video format on [YouTube](https://youtube.com/playlist?list=PLmL13yqb6OxdeOi97EvI8QeO8o-PqeQ0g).
:::

:::{toctree}
438.md
sf11.md
:::
