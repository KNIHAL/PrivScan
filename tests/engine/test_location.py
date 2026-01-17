from privscan.engine.location import offset_to_line_col


def test_offset_to_line_col():
    text = "a\nb\nsecret"
    offset = text.index("secret")
    line, col = offset_to_line_col(text, offset)

    assert line == 3
    assert col == 1
