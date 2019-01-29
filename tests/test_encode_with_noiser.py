import pytest
from tests.config import k, tests_types, test_messages
from src.encoder import Encoder
from src.decoder import Decoder
import random
import time
import logging

from src.basics.exceptions import CannotDetectErrorException

passed = open("passed.txt", "a")
failed = open("failed.txt", "a")


@pytest.mark.parametrize("ii", [ii for ii in range(0, 20)])
@pytest.mark.parametrize("k", k)
@pytest.mark.parametrize("test_type", tests_types)
@pytest.mark.parametrize("message", test_messages)
def test_encoder_fix_errors(ii, k, test_type, message):
    e = Encoder()
    d = Decoder(coding_polynomial=e.coding_polynomial, k=e.k, t=e.r, gf_index=e.gf.index)
    encoded_message = e.encode(message)

    if test_type == 'multiple':
        random_indexes = random.sample(range(0, len(encoded_message)), k)
    else:
        random_start = random.randint(0, len(encoded_message)-k-1)
        random_indexes = [i for i in range(random_start, random_start + k)]
    # print("{}): {}".format(k, random_indexes))
    for i in random_indexes:
        encoded_message.elements[i] = encoded_message.elements[i].multiplicative_inversion()
    try:
        start = time.time()
        decoded_message = d.decode(encoded_message, 'basic')
        stop = time.time()
        passed.write("{}, {}, {}, {}, {}\n".format(k, test_type, message, random_indexes, stop-start))
    except CannotDetectErrorException as c:
        failed.write("{}, {}, {}, {}\n".format(k, test_type, message, random_indexes))
        assert False
    assert message in decoded_message
