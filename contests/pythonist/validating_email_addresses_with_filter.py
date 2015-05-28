# problem description: https://www.hackerrank.com/contests/pythonist/challenges/validate-list-of-email-address-with-filter

# Enter your code here. Read input from STDIN. Print output to STDOUT
def valid_email(e):
    tokens = e.split('@')
    if len(tokens) != 2: return False
    username, domain = tokens
    tokens = domain.split('.')
    if len(tokens) != 2: return False
    websitename, extension = tokens
    username = username.replace('-', '0')
    username = username.replace('_', '0')
    if username.isalnum() and websitename.isalnum() and len(extension) <= 3:
        return True
    return False

emails = []
for e in range(input()):
    emails.append(raw_input())
    
print list(sorted(filter(valid_email, emails)))
