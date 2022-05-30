import os

files = [
    os.path.join('parsed', 'parsed_0.txt'),
    os.path.join('parsed', 'parsed_1.txt')
    ]
mail_seperator = '\n\n\n'


def main() -> None:
    # get all mails from seperate files and put them in a dict of lists
    mails_by_files = dict.fromkeys(files)
    for path in mails_by_files:
        with open(path) as file:
            file_string = file.read()

        mails_by_files[path] = [
            mail for mail in file_string.split(mail_seperator) if mail
            ]

    # get length of longest mail list
    mails = []
    length = 0
    for file in mails_by_files:
        num_mails = len(mails_by_files[file])
        if num_mails > length:
            length = num_mails

    # add the mails together in an alternating pattern
    for index in range(length):
        for file in mails_by_files:
            if index < len(mails_by_files[file]):
                mails.append(mails_by_files[file][index])

    # write all mails into a string
    file_string = ''
    for mail in mails:
        file_string += mail + mail_seperator

    # write that string to a file
    with open(os.path.join('parsed', f'parsed.txt'), 'w+') as file:
        file.write(file_string)


if __name__ == '__main__':
    main()