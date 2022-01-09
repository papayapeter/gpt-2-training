import argparse
import re

# parse arguments
parser = argparse.ArgumentParser(
    description="extracts a dataset from a raw mail conversation"
    )

parser.add_argument(
    "file",
    type=str,
    metavar="path_to_txt_file",
    help="specify the path to a text file containing the raw mail conversation"
    )
parser.add_argument(
    '-n',
    '--names',
    type=str,
    nargs='*',
    help='names of the conversation partners'
    )

args = parser.parse_args()


def main() -> None:
    # read file into lines
    with open(args.file) as file:
        raw_lines = file.readlines()

    # strip indentations
    lines = [line.strip() for line in raw_lines]

    # concat all lines into one string
    data = ""
    for line in lines:
        data += line + "\n"

    # get pattern for splitting from names of the conversation partners
    split_pattern = "("
    for index, name in enumerate(args.names):
        split_pattern += f"\n{name}\n"
        if index < len(args.names) - 1:
            split_pattern += r"|"
    split_pattern += ")"

    # split into mails
    raw_mails = re.split(split_pattern, data)

    # put split delimiters back into mails
    mails = []
    for index, mail in enumerate(raw_mails):
        if index % 2 == 0 and index + 1 < len(raw_mails):
            mails.append(mail + raw_mails[index + 1])

    # extract sender and date

    # add to dataframe

    # save as json or csv


if __name__ == "__main__":
    main()