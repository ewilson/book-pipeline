from baxter.sections import *


def test_is_major_section():
    passage = """CHAPTER 1

                 THE OVERSIGHT OF OURSELVES"""

    assert is_major_section(passage)


def test_if_lowercase_is_not_major_section():
    passage = """Chapter 1

                 Let's just get started herE"""

    assert not is_major_section(passage)


def test_if_no_blank_line_is_not_major_section():
    passage = """CHAPTER 1
                 OF THE BOOK
                 THAT I WROTE"""

    assert not is_major_section(passage)
