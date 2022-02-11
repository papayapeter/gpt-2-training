from typing import List

import re
from email import utils
from email import policy
from email.parser import BytesParser
from datetime import datetime

class Mail:
    """
    Mail object with body, from, to and date properties.
    """
    def __init__(self, body: str = None, sender: str = None, receiver: str = None, date: datetime = None) -> None:
        self._body = body
        self._sender = sender
        self._receiver = receiver
        self._date = date

    def get_body(self) -> str:
        return self._body

    def get_sender(self) -> str:
        return self._sender

    def get_receiver(self) -> str:
        return self._receiver

    def get_date(self) -> datetime:
        return self._date

def from_eml(path_to_eml: str) -> Mail:
    """
    Loads a mail from an eml file and returns it as a Mail instance.
    """
    # open the file
    with open(path_to_eml, 'rb') as file:
        message = BytesParser(policy=policy.default).parse(file)

    text = str(message.get_body(preferencelist=('plain')).get_content())

    # remove non breaking spaces
    text = text.replace(u'\xa0', u' ')
    # remove single newlines
    text = re.sub(r'([^\n])\n([^\n])',  r'\1 \2', text)

    # split text into paragraphs
    lines = []
    raw_lines = [line.strip() for line in text.split('\n') if line != '']
    # get the last paragraph and split the mail there
    for index, line in enumerate(raw_lines):
        lines.append(line)
        if ' ' not in line and ',' not in line:
            if index + 1 < len(raw_lines) and 'P.S.:' in raw_lines[index + 1]:
                lines.append(raw_lines[index + 1])
            break

    return Mail(body='\n'.join(lines), sender=message.get('From'), receiver=message.get('To'), date=utils.parsedate_to_datetime(message.get('Date')))

        