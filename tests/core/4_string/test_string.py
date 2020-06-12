class TestString:
    def test_implicit_concatenation(self):
        title = "Meaning " 'of' " Life"
        assert title == 'Meaning of Life'

    def test_slicing(self):
        some_text = 'abcdefghijklmnop'
        assert some_text[1:10:2] == 'bdfhj'
        assert some_text[::2] == 'acegikmo'
        assert some_text[slice(5, 1, -1)] == 'fedc'
        assert some_text[1:5:-1] == ''

    def test_convert_to_str(self):
        assert "15" + str(42) == "1542"

    def test_representation(self):
        assert repr('spam') == "\'spam\'"


# Formatting expression String methods will be covered as needed in any other section
