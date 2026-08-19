from stridefy.cli import main


def test_multiple_files(tmp_path, monkeypatch, capsys):
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"

    first.write_text("https://example.com/login\n")
    second.write_text("https://example.com/admin/upload\n")

    monkeypatch.setattr(
        "sys.argv",
        ["stridefy", str(first), str(second)],
    )

    main()

    output = capsys.readouterr().out

    assert "(S)poofing:" in output
    assert "(T)ampering:" in output
    assert "(D)enial of Service:" in output
    assert "(E)levation of Privilege:" in output

    assert "https://example.com/login" in output
    assert "https://example.com/admin/upload" in output
