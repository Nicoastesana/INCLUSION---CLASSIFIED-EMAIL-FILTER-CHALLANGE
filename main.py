def open_email(email):
    with open(email, 'r') as file:
        return file.read()


def open_classified_expressions(classified):
    with open(classified) as file:
        return file.read().splitlines()


# "find_all_insensitive" return the position the sub (substring) found with insensitive lower/upper case.
def find_all_insensitive(text, sub):
    start = 0
    idx = []
    email = text.lower()
    element = sub.lower()
    while True:
        start = email.find(element, start)
        if start == -1:
            return idx
        idx.append(start)
        start += len(element)


# "insensitive_replace" replace a designed substring with censored ***** characters.
def insensitive_replace(sub, new_sub, text):
    index_l = find_all_insensitive(text, sub)
    for idx in index_l:
        text = text[:idx] + new_sub + text[idx + len(sub):]
    return text


def classified_email_filter(classified, email):
    if isinstance(classified, str):
        s_email = open_email(email)
        l_classified = open_classified_expressions(classified)
    else:
        s_email = email
        l_classified = classified
    new_s_email = s_email
    for element in l_classified:
        new_s_email = insensitive_replace(element, '*' * len(element), new_s_email)

    return not new_s_email == s_email, new_s_email


print(classified_email_filter('Data/classified_expressions.csv', 'Data/email_1.txt'))
print(classified_email_filter('Data/classified_expressions.csv', 'Data/email_2.txt'))
print(classified_email_filter('Data/classified_expressions.csv', 'Data/email_3.txt'))
print(classified_email_filter('Data/classified_expressions.csv', 'Data/email_4.txt'))

print(classified_email_filter(['cia', 'c.i.a', 'terrorist', 'drug', 'al qaeda', 'al-qaeda', 'gun', 'weapon'],
                              '''Hi Scott,
Thanks for the e-mail.　 It is always nice to hear from people, especially
from you, Scott.

I have not got any reply, a positive or negative one, from Seibido yet.
Let's wait and hope that it will make a BOOK.

Have you finished your paperwork for Kaken and writing academic articles?
If you have some free time in the near future, I want to meet you and
explain to you our next project.

Why not drink out in Hiroshima if we are accepted?
We need to celebrate ourselves, don't we?
Let's have a small end-of-the-year party!

Sincerely, K. Nakagawa'''))
