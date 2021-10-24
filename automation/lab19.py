# Given a document potential-contacts, find and collect all email addresses and phone numbers.
# Phone numbers may be in various formats.
# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.
# Once emails and phone numbers are found they should be stored in two separate documents.
# The information should be sorted in ascending order.
# Duplicate entries are not allowed.
import re

def find_emails(text):
    
    email_re = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(email_re, text)
    # print(emails)
    unique_emails = list(set(emails))
    unique_emails.sort()
    return unique_emails

def find_phones(text):
    phone_re ="(\d{3}\d{3}\d{4})"
    # phone_re = r"^(d{3}-)d{3}d{4}$"
    phones = re.findall(phone_re, text)
    # print(phones)
    phones = list(set(phones))
    phones.sort()
    return phones
# reading the content of the file
with open('automation/assets/potential-contacts.txt', 'r+') as file:
    text = file.read()


# print(find_emails(text))
# saving the emails
with open('automation/assets/emails.txt','w+') as file:
    emails = find_emails(text)
    str1 = ''.join(str(e+"\n") for e in emails)
    file.write(str1)

# print(find_phones(text))
# saving the phone numbers
with open('automation/assets/phones.txt','w+') as file:
    phones = find_phones(text)
    print(phones)
    str1 = ''.join(str(e+"\n") for e in phones)
    file.write(str1)

