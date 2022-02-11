import os
from glob import glob

import modules.mail as email
import modules.parse as parse

# --- constants ---
target_length = 200
split_by = parse.PARAGRAPH
hello_goodbye_seperator = '\n'
mail_seperator = '\n\n\n'

# --- main script ---
def main() -> None:
    # get all mails from directory
    emls_glob = glob(os.path.join('dataset', 'mails', '*.eml'))
    mails = [email.from_eml(eml) for eml in emls_glob]

    # get all reqiured parsing information in the terminal
    # which senders to parse
    all_senders = dict.fromkeys(set([mail.get_sender() for mail in mails]), '')
    print('mails from which senders should be parsed? format: e.g. 101 (first & third one). default: all')
    print(*[f'{index}: {sender}' for index, sender in enumerate(all_senders)], sep=', ')
    response = input('> ')
    
    senders = {}
    if response:
        for index, sender in enumerate(all_senders):
            if int(response[index]):
                senders[sender] = ''
    else:
        senders = all_senders
    
    # which senders belong together
    teams = {0: [], 1: []}
    print('which senders belong together? format: e.g. 011')
    response = ''
    while len(response) != len(senders):
        response = input('> ')
        if len(response) != len(senders):
            print('wrong input!')

    for index, sender in enumerate(senders):
        teams[int(response[index])].append(sender)

    submails_by_teams = {0: [], 1: []} 
    for mail in mails:
        hello = parse.isolate_hello(mail.get_body())
        goodbye = parse.isolate_goodbye(mail.get_body(), 36)
        ps = parse.isolate_ps(mail.get_body())
        stripped = parse.strip_mail(mail.get_body(), hello, goodbye, ps)

        submails = parse.get_submails(stripped, target_length, split_by, prepend=f'{hello}{hello_goodbye_seperator}', append=f'{hello_goodbye_seperator}{goodbye}')

        for team in teams:
            if mail.get_sender() in teams[team]:
                [submails_by_teams[team].append(submail) for submail in submails]

    for team in submails_by_teams:
        file_string = ''
        for submail in submails_by_teams[team]:
            file_string += submail + mail_seperator
        
        with open(os.path.join('output', f'parsed_{team}.txt'), 'w+') as file:
            file.write(file_string)

    print('parsed mails')


if __name__ == '__main__':
    main()