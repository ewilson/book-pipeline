import re

MAJOR_SECTION_PATTERN = re.compile(r"""^[A-Z]     # First character capital letter
                                       +[^a-z]+\n # no lowercase letters on line
                                       [ \t]*\n   # next line is whitespace only
                                       [^a-z]+    # third line has no lowercase letters
                                       [A-Z]+$    # ends with capital letter""", re.VERBOSE)


def extract_headers(chunks):
    return []


def is_major_section(chunk):
    return MAJOR_SECTION_PATTERN.match(chunk) is not None
