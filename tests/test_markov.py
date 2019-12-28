"""Tests for the markov handling logic."""
from pytest import fixture
from maho.modules import markov


@fixture
def sample_lines():
    """Get some sample lines."""
    return [
        "This is some lines.",
        "yeah quite a few.",
        "In real life this would be real messages.",
        "From real discord users.",
        "But for privacy reasons.",
        "And testing purposes.",
        "We must instead provide some dummy messages.",
        "In this list.",
        "I am honestly not sure.",
        "What other messages should go here.",
        "But whatever.",
        "This should be good enough.",
        "Or so I thought.",
        "For if there isn't enough message diversity,",
        "There just arent any good results it seems?",
    ]


def test_markov(sample_lines):
    """Test that a valid markov chain message is generated."""
    message = markov.get_markov_message(sample_lines)
    assert len(message)
    assert message[-1] in [".", "?", "!"]
    assert len(message.split(" ")) > 3
