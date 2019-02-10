# Reed-Solomon encoder and decoder

## Project
Project consists of 3 elements:
* GF arithmetic implementation
* RS encoder (implemented for 7bits long alphas, but it supports 8bit long ASCII chars)
* simple RS decoder

## Testing
Tests cover Bit, Polynomial, Alpha, GF, encoder and decoder implementation
* Running tests: `make test`

## Running
There is an example program which encodes and decodes message and then tries to decode too coruppted message (27 errors, when 26 is maximum for RS(127, 73)):
* `python run_example.py`
