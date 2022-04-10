import re

def email_parse(email):
    parse_data = re.compile(r'(.+)@(.+)\.(.+)$').findall(email)
    if parse_data:
        username, domain, zone = parse_data[0]
    else:
        raise ValueError('Wrong email')

    data = {
        'username': username,
        'domain': f'{domain}.{zone}'
    }

    return data


print(email_parse('nikita@test.ru'))
print(email_parse('niki@ta@test.ru'))
print(email_parse('nikita_test.ru'))
print(email_parse('test.ru'))