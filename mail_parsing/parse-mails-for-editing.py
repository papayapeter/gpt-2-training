import os
from datetime import datetime
from glob import glob
import re

import modules.mail as email


def main() -> None:
    # get all mails from directory
    emls_glob = glob(os.path.join('dataset', 'mails', '*.eml'))
    mails = [email.from_eml(eml) for eml in emls_glob]

    # sort mails by date
    def get_date(mail: email.Mail) -> datetime:
        return mail.get_date()

    mails.sort(key=get_date)

    # split bodies by sentence
    mail_dict = [{
        'datetime': mail.get_date(),
        'sender': mail.get_sender(),
        'body': mail.get_body()
        } for mail in mails]

    for mail in mail_dict:
        mail['body'] = re.split(r'(?<=[.?!;])', mail['body'])

    # print split mails to file
    with open(os.path.join('dataset', 'for_pasting.txt'), 'w') as file:
        for mail in mail_dict:
            file.write(
                f'''---\nsender: {mail["sender"]}\ndatetime: {mail["datetime"].strftime("%d.%m.%Y, %H:%M:%S")}\n\n'''
                )

            file.write('\n'.join((line.strip() for line in mail['body'])))

            file.write('\n\n')


if __name__ == '__main__':
    main()