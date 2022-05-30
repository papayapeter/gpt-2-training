from typing import List, Union, Literal

import re

SENTENCE = 0
PARAGRAPH = 1

def isolate_hello(body: str) -> str:
    """
    Gets only the greeting from a mail.
    """
    return body.split('\n')[0]

def isolate_goodbye(body: str, max_length : int = 20) -> str:
    """
    Gets only the goodbye part.
    """
    lines = [line for line in body.split('\n')]
    goodbye_lines = []
    for line in reversed(lines):
        if len(line) > max_length and 'P.S.:' not in line:
            break
        if 'P.S.:' not in line:
            goodbye_lines.append(line)
    return '\n'.join(reversed(goodbye_lines))

def isolate_ps(body: str) -> str:
    """
    Gets only the 'P.S.:'.
    """
    last_line = [line for line in body.split('\n')][-1]
    return last_line if 'P.S.:' in last_line else None

def strip_mail(body: str, hello: str = None, goodbye: str = None, ps: str = None) -> str:
    """
    Strips the mail body of hello, goodbye and 'P.S.:'.
    """
    stripped = body
    if hello:
        stripped = stripped[len(hello):]
    if goodbye:
        end = goodbye
        if ps:
            end += f'\n{ps}'
        stripped = stripped[:len(stripped) - len(end)]

    return stripped

def get_submails(body: str, target_length: int, split_by, prepend: str = None, append: str = None) -> List[str]:
    """
    Splits the mail into smaller pieces.

    body: preferrably a mailbody stripped of hello, goodbye and 'P.S.:'
    target_length: the target length in characters of the splits
    split_by: a string of characters that shall be used for splitting (e.g. '.;\n')
    prepend: e.g. a greeting that should be appended to every submail
    append: e.g. a goodbye that should be prepended to every submail
    """
    if split_by == SENTENCE:
        splits = re.findall(r'.*?[.!\?]', body)
    elif split_by == PARAGRAPH:
        splits = body.split('\n')
    else:
        raise ValueError("split_by parameter must be either 'SENTENCE' or 'PARAGRAPH'")

    if not body:
        return []

    # remove empty items and strip
    splits = [split.strip() for split in splits if split]

    submails = [splits[0]]
    submail_count = 0
    for split in splits[1:]:
        submail_length = len(submails[submail_count])
        split_length = len(split)
        if abs(target_length - (submail_length + split_length)) < abs(target_length - submail_length):
            submails[submail_count] = f"{submails[submail_count]} {split}"
        else:
            submails.append(split)
            submail_count += 1

    return [f"{prepend if prepend else ''}{submail}{append if append else ''}" for submail in submails]