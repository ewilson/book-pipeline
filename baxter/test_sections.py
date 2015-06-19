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


def test_clean_major_section():
    passage = """CHAPTER 1

                 THE OVERSIGHT OF OURSELVES"""

    assert clean_major_section(passage) == "CHAPTER 1 THE OVERSIGHT OF OURSELVES"


def test_is_minor_section():
    passage = """SECTION 1 -- THE NATURE OF THIS OVERSIGHT

   Having showed you, What it is to take heed to ourselves, I am to show
   you, next to all the flock in proportion to the measure
   of their sin."""

    assert not is_major_section(passage)
    assert is_minor_section(passage)


def test_is_not_minor_section():
    passage = """SECTION 1 -- THE NATURE OF THIS OVERSIGHT
   Having showed you, What it is to take heed to ourselves, I am to show
   you, next to all the flock in proportion to the measure
   of their sin."""

    assert not is_major_section(passage)
    assert not is_minor_section(passage)


