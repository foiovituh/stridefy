from stridefy.parser import parse_file


def test_parse_file(tmp_path):
    target = tmp_path / "targets.txt"
    target.write_text("\nhttps://example.com/login\n\nhttps://example.com/api?id=1\n")

    assert parse_file(target) == [
        "https://example.com/login",
        "https://example.com/api?id=1",
    ]
