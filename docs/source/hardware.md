# Recommended Hardware

## LoRa ICs and Modules
- [Semtech LoRa products](https://www.semtech.com/lora/lora-products)
- [Semtech SX1278](https://www.semtech.com/products/wireless-rf/lora-core/sx1278)
- [HopeRF LoRa modules](https://www.hoperf.com/modules/lora/index.html)
- [HopeRF RFM98W](https://www.hoperf.com/modules/lora/RFM98.html)
- [G-NiceRF Lora1278F30 1 watt module](https://www.aliexpress.com/item/32686822638.html)

## Tracker Hardware
- TTGO T-Beam 433&nbsp;MHz v0.7 or v1.1
- longer 433&nbsp;MHz antenna with [SMA male](https://en.wikipedia.org/wiki/SMA_connector) connector
- 16.9&nbsp;mm long tiger tail wire soldered to the female SMA socket
- 5&nbsp;V, 3&nbsp;A USB charge adapter with appropriate microUSB or USB‑C cable
- Panasonic NCR18650B Li-ion cell, or quality equivalent
- glue gun to stick the GPS antenna to the cell holder
- SH1106 1.3" I²C (4‑pin) OLED display (slightly larger than the usual 0.8" displays often sold with the TTGO T-Beam)
- enclosure

## I-Gate Hardware
- Either:
  + [TTGO LORA32 433&nbsp;MHz v2](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1319&FId=t3:50060:3) ([U.FL](https://en.wikipedia.org/wiki/Hirose_U.FL) or [SMA female](https://en.wikipedia.org/wiki/SMA_connector) RF socket), or
  + maybe Heltec ESP32 LoRa 433&nbsp;MHz **v2** ([U.FL](https://en.wikipedia.org/wiki/Hirose_U.FL) female RF socket); subject to satisfactory receiver testing
- 70&nbsp;cm amateur radio colinear groundplane antenna with coaxial cable and connectors
- 16.9&nbsp;mm long tiger tail wire soldered to the RF socket
- 5&nbsp;V, 1&nbsp;A USB power supply with appropriate microUSB or USB‑C cable
- enclosure

:::{caution}
**<u>DO NOT USE</u>** Heltec ESP32 LoRa 433&nbsp;MHz **v1** as it is as deaf as a post!
:::
