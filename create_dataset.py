from typing import List
from pandas import DataFrame
from datetime import datetime

import argparse
import re
import pandas as pd

# parse arguments
parser = argparse.ArgumentParser(
    description="extracts a dataset from a raw mail conversation"
    )

parser.add_argument(
    "stream",
    type=str,
    metavar="path_to_txt_file",
    help="specify the path to a text file containing the raw mail conversation"
    )
parser.add_argument(
    '-s',
    '--swimmers',
    type=str,
    nargs='*',
    help='names of the conversation partners'
    )

args = parser.parse_args()


def parse_mails(raw_mails: str, names: List[str]) -> DataFrame:
    # read file into lines
    with open(raw_mails) as file:
        raw_lines = file.readlines()

    # strip indentations
    lines = [line.strip() for line in raw_lines]
    #remove empty lines
    lines = [line for line in lines if line != '']

    split_points = []
    for index, line in enumerate(lines[:-2]):
        for name in names:
            if line == name:
                if 'P.S.: ' in lines[index + 1]:
                    split_points.append(index + 2)
                else:
                    split_points.append(index + 1)

    mail_lines = [lines[:split_points[0]]]
    for index, split_point in enumerate(split_points[:-1]):
        mail_lines.append(lines[split_point:split_points[index + 1]])
    mail_lines.append(lines[split_points[-1]:])

    mails = []
    for index, mail_line in enumerate(mail_lines):
        mails.append("")
        for line in mail_line:
            mails[index] += line + '\n'

    # add to dataframe
    df_mails = pd.DataFrame(
        columns=['sender', 'date', 'hello', 'goodbye', 'mail']
        )

    df_mails['mail'] = mails

    # extract name & date
    df_mails['sender'] = df_mails['mail'].map(extract_sender)
    df_mails['date'] = df_mails['mail'].map(extract_date)

    # remove header and appendix
    df_mails['mail'] = df_mails['mail'].map(reduce_mail)

    # extract data
    df_mails['hello'] = df_mails['mail'].map(extract_hello)
    df_mails['goodbye'] = df_mails['mail'].map(extract_goodbye)

    # drop carcasses
    df_mails = df_mails.drop(
        df_mails.loc[df_mails['mail'] == "not a mail"].index
        )

    #return
    return df_mails


def extract_sender(mail: str) -> str:
    # split mail into lines
    lines = mail.split('\n')

    # remove empty lines
    lines = [line for line in lines if line != '']

    for line in lines:
        if ' ' not in line:
            name = line

    return name


def extract_date(mail: str) -> str:
    # split mail into lines
    lines = mail.split('\n')

    # remove empty lines
    lines = [line for line in lines if line != '']

    if 'Am ' in lines[0]:
        date = re.sub(r'Am | um.*', '', lines[0])
    elif 'On ' in lines[0]:
        date = re.sub(r'On |,.*', '', lines[0])
    elif 'Ein ' in lines[0]:
        date = re.sub(r'Ein \w*, | \+.*', '', lines[0])
    elif 'Sent: ' in lines[1]:
        date = re.sub(r'Sent: ', '', lines[1])
    else:
        date = 'not found'

    return date


def extract_hello(mail: str) -> str:
    # split mail into lines
    lines = mail.split('\n')

    # remove empty lines
    lines = [line for line in lines if line != '']

    return lines[0]


def extract_goodbye(mail: str) -> str:
    if mail == 'not a mail':
        return 'not found'

    # split mail into lines
    lines = mail.split('\n')

    # remove empty lines
    lines = [line for line in lines if line != '' and 'P.S.: ' not in line]

    return f'{lines[-2]}\n{lines[-1]}'


def reduce_mail(mail: str) -> str:
    # split mail into lines
    match = re.search(r'\w* \w*,\n', mail)

    if match:
        return mail[mail.index(match.group(0)):]
    else:
        print(f'could not reduce:\n{mail}\n---------------------')
        return 'not a mail'


if __name__ == '__main__':
    mails = parse_mails(args.stream, args.swimmers)
    mails.to_csv('dataset/mails.csv')