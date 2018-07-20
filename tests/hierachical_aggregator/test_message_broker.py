import pytest

from hierachical_aggregator.message_broker import MessageSchema, MessageError


def test_MessageSchema__success():
    s = MessageSchema({"word": str})
    s.validate_message({"word": "bird"})


def test_MessageSchema__fail():
    s = MessageSchema({"word": str})
    with pytest.raises(MessageError):
        s.validate_message({"word": 123})
