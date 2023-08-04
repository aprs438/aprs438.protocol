# Future Plans

## From Pure to Reservation ALOHA
Recent academic research investigated the collision of two LoRa packets of equal power when collided with a start time offset.
It was found that first LoRa packet stands a high chance of being correctly received as long as
its [cyclic redundancy check (CRC)](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) information was not interfered by the second LoRa packet.
This very sensitive CRC information of a LoRa packet is sent in the explicit header, towards the beginning of the packet.

Most LoRa APRS implementations allow end devices to transmit at any moment of time.
This inevitably results in packet collisions and the loss of the information of one or more packets.
This situation is called [pure ALOHA (P‑ALOHA)](https://en.wikipedia.org/wiki/ALOHAnet#Pure_ALOHA).
It is comparable to a pile up during a DXpedition.

Above situation can be improved upon by allowing the packet transmissions to start only at well defined moments in time.
This form of [medium access control (MAC)](https://en.wikipedia.org/wiki/Medium_access_control) is called [slotted ALOHA (S‑ALOHA)](https://en.wikipedia.org/wiki/ALOHAnet#Slotted_ALOHA).
However, even with slotted ALOHA, packet collisions can still occur.

Taking this a step further, with [reservation ALOHA (R‑ALOHA)](https://en.wikipedia.org/wiki/Reservation_ALOHA)
the i‑gate temporarily assigns a time slot to an end device that was successful in reaching the i‑gate in one of the vacant time slots.
With this MAC scheme, packet collisions now can only occur at first access; resulting in a vastly more efficient use of the channel.
This scheme is comparable to a controlled HF&nbsp;net.

|[pure ALOHA](https://en.wikipedia.org/wiki/ALOHAnet#Pure_ALOHA)|[slotted ALOHA](https://en.wikipedia.org/wiki/ALOHAnet#Slotted_ALOHA)|
|:-:|:-:|
|![Pure ALOHA protocol](https://upload.wikimedia.org/wikipedia/commons/3/35/Pure_ALOHA1.svg)|![Slotted ALOHA protocol](https://upload.wikimedia.org/wikipedia/commons/7/7a/Slotted_ALOHA.svg)|
