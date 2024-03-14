def check_exception():
    name, email, age = line.split()

    if name_check(name) is False:
        raise NameError('Имя содержит не только буквы.')
    elif check_email(email) is False:
        raise SyntaxError('Поле e-mail не содержит @ и .точку()')
    elif check_age(age) is False:
        raise ValueError('Поле возраста выходит за диапазон от 10 до 99')
    else:
        file_good.write(line)
def name_check(name):
    if str(name).isalpha():
        return True
    else:
        return False

def check_email(email):
    if "@" in email or "." in email:
        return True
    else:
        return False

def check_age(age):
    if 10 <= int(age) <= 99:
        return True
    else:
        return False


file_registration = open('registrations.txt', "r", encoding='utf8')
file_bad = open('registrations_bad.log', "w", encoding='utf8')
file_good = open('registrations_good.log', "w", encoding='utf8')

for line in file_registration:
    try:
        check_exception()
    except (NameError, ValueError, SyntaxError) as exc:
        file_bad.write(f"{line} вид ошибки: {exc}")

file_registration.close()
file_good.close()
file_bad.close()
