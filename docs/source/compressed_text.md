# Compressed Text
In order to prevent channel congestion, it is crucial to limit the character set of messages. This allows for more frame compression.
In resemblance to Morse code, the character set would contain only 26 Latin capital letters, the 10&nbsp;digits, space and a few punctuation marks and symbols. Limiting the set to 42 characters makes it fit 6 times in the 256 character set of LoRa.

|character subset|# of characters|
|:--------------:|:-------------:|
|Latin capital letters|26|
|digits|10|
|space|1|
|punctuation `.`&nbsp;`?`|2|
|symbols `-`&nbsp;`/`&nbsp;`@`|3|
|**TOTAL**|**42**|

## Encoding tttt
1. Perform input sanitisation.
2. Perform character replacement and filtering on the given string; only allow for characters of the [42&nbsp;character set](#compressed-text).
3. Treat the resulting text string as a Base42 encoding. Decode it first to an integer.
4. Then, encode this integer as a Base256 `tttt` bytestring.

## Decoding tttt
1. First, decode the given Base256 `tttt` bytestring to an integer.
2. Then, encode this integer as a Base42 string, corresponding to the text.


:::{caution}
**<u>REFRAIN</u> from adding any APRS comments!**
Adding more bytes to a LoRa frame only reduces the chances on successful reception.
Rather, consider sending an occasional [status report](#compressed-status-report-frames).
:::
