import os


TEMPLATE_PATH = 'template.txt'
user_answers = {
    'adjectives': {
        'message': 'an Adjective',
        'value': [''] * 6},
    'first_name': {
        'message': 'First Name',
        'value': ''},
    'past_tense_verb': {
        'message': 'a Past Tense Verb',
        'value': ''},
    'plural_nouns': {
        'message': 'a Plural Noun',
        'value': [''] * 5},
    'large_animal': {
        'message': 'a Large Animal',
        'value': ''},
    'small_animal': {
        'message': 'a Small Animal',
        'value': ''},
    'girls_name': {
        'message': 'a Girl\'s name',
        'value': ''},
    'numbers': {
        'message': 'a number',
        'value': [None] * 3},
}


def print_welcome():
    print('welcome user, here are the rules')


def read_template(template_path):
    if os.path.exists(template_path):
        try:
            with open(template_path, 'r') as t_file:
                new_template = t_file.read()
        except IOError:
            print(f'Could\'t read the file {template_path}')
        else:
            return new_template
    else:
        print(f'File {template_path} doesn\'t exist')


def get_user_answers():
    for key, value in user_answers.items():
        if type(value['value']) == list:
            for val in value['value']:
                print(f'Please enter {value["message"]} and press enter')
        else:
            print(f'Please enter {value["message"]} and press enter')


def prepare_template(template):
    # Replace adjectives with user input values
    for i in range(len(user_answers['adjectives']['value'])):
        template = template.replace(
            '{Adjective}', f'{user_answers["adjectives"]["value"][i]}', 1)

    # Replace first name
    template = template.replace(
        '{A First Name}', f'{user_answers["first_name"]["value"]}', 2)

    template = template.replace(
        "{First Name's}", f'{user_answers["first_name"]["value"]}\'s')

    # Replace Past Tense Verb
    template = template.replace(
        "{Past Tense Verb}", f'{user_answers["past_tense_verb"]["value"]}')

    # Replace Plural Noun
    for i in range(len(user_answers['plural_nouns']['value'])):
        template = template.replace(
            '{Plural Noun}', f'{user_answers["plural_nouns"]["value"][i]}', 1)

    # Replace Large Animal
    template = template.replace(
        "{Large Animal}", f'{user_answers["large_animal"]["value"]}')

    # Replace Small Animal
    template = template.replace(
        "{Small Animal}", f'{user_answers["small_animal"]["value"]}')

    # Replace Girl's Name
    template = template.replace(
        "{A Girl's Name}", f'{user_answers["girls_name"]["value"]}')

    # Replace Numbers
    template = template.replace(
        "{Number 1-50}", f'{user_answers["numbers"]["value"][0]}')

    for i in range(1, len(user_answers['numbers']['value'])):
        template = template.replace(
            '{Number}', f'{user_answers["numbers"]["value"][i]}', 1)

    return template


def run_game():
    print_welcome()
    get_user_answers()
    template = read_template(TEMPLATE_PATH)
    template = prepare_template(template)
    print(template)


if __name__ == "__main__":
    run_game()
