# Measurable Benefits

## Reduced Packet Error Rate
**APRS&nbsp;434** geolocation beacons will encode a total of **only 18 payload bytes** at a time, tremendously **increasing the chances of a flawless reception** by an [**APRS&nbsp;434&nbsp;LoRa&nbsp;i-gate**](https://github.com/aprs434/lora.igate). Other firmware tends to consume about six times as many LoRa payload bytes.

LoRa may receive up to 20&nbsp;dB under the noise floor, but keep in mind that [**the packet error rate (PER)**](https://en.wikipedia.org/wiki/Bit_error_rate#Packet_error_ratio) as a function of the bit error rate (BER) [increases with the number of transmitted bits](https://en.wikipedia.org/wiki/Bit_error_rate#Packet_error_ratio).

```{math}
PER = 1 - (1 - BER)^n \approx n \cdot BER$$
```

approximately, when {math}`BER` is small and {math}`n` is large, and where:

- {math}`(1-BER)`: the probability of receiving a bit correctly
- {math}`n`: the number of bits in a packet; which is 8 times the number of bytes

### PER Examples
When used with an explicit header, LoRa packets will have the following 36&nbsp;bit overhead:
a 16&nbsp;bit physical header `PHDR`, 4&nbsp;bits of header [CRC](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) `PHDR_CRC` and another 16&nbsp;bits of payload `CRC`.

|payload|17 bytes|24 bytes|28 bytes|45 bytes|113 bytes|
|:-----:|:------:|:------:|:------:|:------:|:-------:|
|overhead|36 bits|36 bits|36 bits|36 bits|36 bits|
|n|172 bits|228 bits|260 bits|396 bits|940 bits|
|BER|0.1%|0.1%|0.1%|0.1%|0.1%|
|PER|15.8%|20.4%|22.9%|32.7%|61.0%|

By consequence, the chances of correctly receiving a 17&nbsp;byte payload are more than twice as high as with a 113&nbsp;byte payload:

```{math}
\frac{1-0.158}{1-0.610} \approx 2.18
```

In reality, above calculations are more convoluted as LoRa employs symbols that are chip jumps or discontinuities in chirps to convey information.
Moreover, a preamble, consisting out of a configurable length preamble, a set sync word, a start frame delimiter (SDF) and a small pause precede the explicit header.
The variable preamble is important as it trains the receiver at receiving the signal. Hence, the symbol length of this [variable preamble also has an effect on the packet error rate](https://hal.archives-ouvertes.fr/hal-02316402/document). Details about the LoRa packet structure can be found [here](https://blog.csdn.net/weixin_43270276/article/details/122144556).


## Airtime Reduction
Keeping the payload as small as possible, has an even more important reason: to reduce the airtime required to send the LoRa frame.
As will be shown in the [next section](#lora-link-parameters), **LoRa is a slow data rate mode.**
Reducing the airtime also **saves battery power** of portable devices.

Due to the LoRa symbol encoding scheme, airtime reductions occur in abrupt steps of 5&nbsp;bytes when the spreading factor is SF12 and the bandwidth 125&nbsp;kHz (CR=1, explicit header, CRC=on). This is depicted as the stepped top trace on the figure below. (Adapted from [airtime-calculator](https://avbentem.github.io/airtime-calculator/ttn/eu868/4,14).)

```{figure} /images/lora.airtime-payload.18bytes.png
**Figure 1:** The top trace is for SF12BW125. The dot represents a total payload of 17 bytes as proposed for geolocation packets with compression.
```

|payload|5 bytes|17 bytes|24 bytes|28 bytes|45 bytes|113 bytes|
|:-----:|:-----:|:------:|:------:|:------:|:------:|:-------:|
|airtime with SF12|0.83&nbsp;s|1.32&nbsp;s|1.48&nbsp;s|1.65&nbsp;s|2.14&nbsp;s|4.43&nbsp;s|
|airtime with SF11|0.50&nbsp;s|0.66&nbsp;s|0.82&nbsp;s|0.91&nbsp;s|1.15&nbsp;s|2.46&nbsp;s|
|airtime with SF10|0.25&nbsp;s|0.33&nbsp;s|0.37&nbsp;s|0.41&nbsp;s|0.56&nbsp;s|1.23&nbsp;s|

[The Things Network (TTN)](https://www.thethingsnetwork.org) organisation, albeit a global LoRaWAN, is exemplary in stressing [the importance of maintaining LoRa payloads small](https://www.thethingsnetwork.org/docs/devices/bytes/).
