import re

MAJOR_SECTION_PATTERN = re.compile(r"""^[A-Z]     # First character capital letter
                                       +[^a-z]+\n # no lowercase letters on line
                                       [ \t]*\n   # next line is whitespace only
                                       [^a-z]+    # third line has no lowercase letters
                                       [A-Z]+$    # ends with capital letter""", re.VERBOSE)


MINOR_SECTION_PATTERN = re.compile(r"""^[A-Z]                      # First character capital letter
                                       +[^a-z]+\n                  # no lowercase letters on line
                                       [ \t]*\n                    # next line is whitespace only
                                       [ \t]*[A-Z]+[a-z ][a-z]+    # third line has lowercase letters
                                       """, re.VERBOSE)

BLANK_LINE = r"[ \t]*\n[ \t]*\n[ \t]*"
WHTIE_ENDS = r"[ \t]*\n[ \t]*"

def extract_headers(chunks):
    return []


def is_major_section(chunk):
    return MAJOR_SECTION_PATTERN.match(chunk) is not None


def clean_major_section(s):
    return ' '.join(re.split(BLANK_LINE,s))


def is_minor_section(chunk):
    return MINOR_SECTION_PATTERN.match(chunk) is not None


def clean_minor_section(s):
    [head, tail] = re.split(BLANK_LINE, s, 1)
    return head, ' '.join(re.split(WHTIE_ENDS,tail))
