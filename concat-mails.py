import os

files = [os.path.join('output', 'parsed_0.txt'), os.path.join('output', 'parsed_1.txt')]
mail_seperator = '\n\n\n'

def main() -> None:
    mails_by_files = dict.fromkeys(files)
    for path in mails_by_files:
        with open(path) as file:
            file_string = file.read()
        
        mails_by_files[path] = [mail for mail in file_string.split(mail_seperator) if mail]

    mails = []
    if len(list(mails_by_files.values())[0]) - len(list(mails_by_files.values())[1]) < 0:
        pass

if __name__ == '__main__':
    main()