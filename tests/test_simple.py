from susi_python import susi_client as susi


# Check a simple reply
def test_reply():
    answer = susi.ask("hi")
    assert answer is not None
