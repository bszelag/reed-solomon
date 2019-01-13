import pytest
from tests.config import decoder, proper_codewords, codeword_with_error, codeword_without_fix
from src.decoder import Decoder
from src.basics.exceptions import CannotDetectErrorException


@pytest.mark.parametrize("codewords", proper_codewords)
def test_encoder(codewords):
    decoded_message = decoder.decode(codewords['codeword'])
    print(decoded_message)
    assert codewords['message'] in decoded_message


@pytest.mark.parametrize("codewords", codeword_with_error)
def test_encoder_with_errors(codewords):
    decoded_message = decoder.decode(codewords['codeword'])
    print(decoded_message)
    assert codewords['message'] in decoded_message


@pytest.mark.parametrize("codewords", codeword_without_fix)
def test_encoder_cannot_fix_codeword(codewords):
    with pytest.raises(CannotDetectErrorException):
        decoder.decode(codewords['codeword'])
