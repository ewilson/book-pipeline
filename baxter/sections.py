import re

MAJOR_SECTION_PATTERN = re.compile(r"""^[A-Z]     # First character capital letter
                                       +[^a-z]+\n # no lowercase letters on line
                                       [ \t]*\n   # next line is whitespace only
                                       [^a-z]+    # third line has no lowercase letters
                                       [A-Z]+$    # ends with capital letter""", re.VERBOSE)


MINOR_SECTION_PATTERN = re.compile(r"""^[A-Z]                      # First character capital letter
                                       +[^a-z]+\n                  # no lowercase letters on line
                                       [ \t]*\n                    # next line is whitespace only
                                       [ \t]*[A-Z][a-z ]+    # third line has lowercase letters
                                       """, re.VERBOSE)

LC_PATTERN = re.compile(r'.*[a-z]+.*')

BLANK_LINE = r"[ \t]*\n[ \t]*\n[ \t]*"
WHTIE_ENDS = r"[ \t]*\n[ \t]*"


def extract_headers(chunks):
    current_chapter = ''
    author = "Richard Baxter"
    title = "Reformed Pastor"
    sections = []
    for c in chunks[3:-3]:
        if is_major_section(c):
            current_chapter = clean_major_section(c)
        elif is_minor_section(c):
            stitle, stext = clean_minor_section(c)
            section_title = "%s %s" % (current_chapter, stitle) if len(current_chapter) > 0 else stitle
            d = {'author': author, 'title': title, 'section_title': section_title, 'section_text': stext}
            sections.append(d)
        else:
            print("WARNING: didn't know what to do with: %s" % c)
    return sections

def is_major_section(chunk):
    return MAJOR_SECTION_PATTERN.match(chunk) is not None


def clean_major_section(s):
    return ' '.join(re.split(BLANK_LINE,s))


def is_minor_section(chunk):
    return MINOR_SECTION_PATTERN.match(chunk) is not None


def clean_minor_section(s):
    parts = re.split(BLANK_LINE, s, 2)
    if LC_PATTERN.match(parts[1]) is not None:
        head = parts[0]
        tail = ' '.join(parts[1:])
    else:
        head = ' '.join(parts[:2])
        tail = parts[2] if len(parts) == 3 else ""
    return ' '.join(re.split(WHTIE_ENDS,head)), ' '.join(re.split(WHTIE_ENDS,tail))
