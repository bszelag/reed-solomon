import pytest
from tests.config import test_messages
from src.basics.exceptions import CannotDetectErrorException


@pytest.mark.parametrize("message", test_messages)
def test_encoder(message, decoder, encoder):
    encoded_message = encoder.encode(message)
    decoded_message = decoder.decode(encoded_message, 'basic')
    print(decoded_message)
    assert message in decoded_message


@pytest.mark.parametrize("message", test_messages)
def test_encoder_fix_errors(message, decoder, encoder):
    encoded_message = encoder.encode(message)
    for i in range(1, 27):
        encoded_message.elements[i] = encoded_message.elements[i].multiplicative_inversion()
    decoded_message = decoder.decode(encoded_message, 'basic')
    print(decoded_message)
    assert message in decoded_message


@pytest.mark.parametrize("message", test_messages)
def test_encoder_fails(message, decoder, encoder):
    encoded_message = encoder.encode(message)
    for i in range(0, 28):
        encoded_message.elements[i] = encoded_message.elements[i].multiplicative_inversion()
    with pytest.raises(CannotDetectErrorException):
        decoder.decode(encoded_message, 'basic')
