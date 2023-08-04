# Acknowledgements

## Firmware
- Ricardo Guzman Christie, CD2RXU, for developing client and i‑gate firmware employing the compression algorithms presented in this white paper.
- Bernd Gasser, OE1ACM, for the earliest LoRa APRS experiments and code
- Christian Johann Bauer, OE3CJB, for the Base91 geolocation compression algorithm
- Peter Buchegger, OE5BPA, for providing a tracker and i‑gate firmware as open source code, in a handy [PlatformIO](https://platformio.org) environment, with [over-the-air (OTA)](https://en.wikipedia.org/wiki/Over-the-air_programming) i‑gate updates. This was the ideal starting point for running LoRa frame compression experiments.

## Codec
- Folkert Tijdens, PA0FOT, for contributing [`compression.cpp`](code/codec.cpp) and asking the right questions, rendering this document more scholarly
- Matthias Brändli, HB9EGM, for contributing the Arduino C implementation of the `tttt` codec algorithm.
- Pascal Schiks, PA3FKM, for providing insights about microcontroller stacks

## Frequency Selection
- Wolfgang Hallmann, DF7PN, for informing that, in a number of European countries, the ISM‑band extends from 433.05 to 434.79&nbsp;MHz.
- Gerhard Hickl, OE3GHB, for pointing out that, in Austria, the spectrum above 439.1&nbsp;MHz is receive only.

## Testing
- Erwin Fiten, ON8AR, for testing firmware and reporting on long distance car approaches to the LoRa i‑gate
- Jan Engelen, DL6ZG, for testing firmware and providing feedback
- Greg Stroobandt, ON3GR, for cycling around the city with a privacy invading tracker

## Infrastructure
- [ReadTheDocs.org](https://readthedocs.org/) for hosting the documentation of this project, free of charge
- [Github.com](https://github.com/) for hosting the project source files, free of charge
- The [Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator and its [extensions](https://sphinx-extensions.readthedocs.io/en/latest/)
- [executable{books}](https://executablebooks.org/en/latest/) for the Markedly Structured Text [MyST Python parser](https://myst-parser.readthedocs.io/en/stable/index.html) ([cheat sheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html), [syntax extensions](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html))
