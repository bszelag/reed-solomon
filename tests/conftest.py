import pytest

from src.encoder import Encoder
from src.decoder import Decoder


@pytest.fixture(scope="function")
def encoder():
    e = Encoder()
    return e


@pytest.fixture(scope="function")
def decoder(encoder):
    d = Decoder(coding_polynomial=encoder.coding_polynomial, k=encoder.k, t=encoder.r, gf_index=encoder.gf.index)
    return d
