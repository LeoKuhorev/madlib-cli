import os
import re


TEMPLATE_PATH = 'madlib_cli/template.txt'
SAVE_TO_PATH = 'madlib_cli/result.txt'


def read_file(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                new_template = f.read()
        except IOError:
            print(f'Could\'t read the file {file_path}')
            return False
        else:
            return new_template
    else:
        print(f'File {file_path} doesn\'t exist')
        return False


def save_result(text, file_path):
    with open(file_path, 'w') as f:
        f.write(text)


def get_user_answers(questions):
    answers = []
    total = len(questions)
    for i in range(total):
        print(
            f'Please type {questions[i]} and press enter to submit ({i}/{total} answered)')
        answers.append(input())
    return answers


def replace_words(pattern, content, template):
    for word in content:
        template = re.sub(pattern, word, template)
    return template


def run_game():
    print('Welcome!')
    template = read_file(TEMPLATE_PATH)
    if template:
        words_to_replace = re.findall('{([^\}]*)}', template)
        answers = get_user_answers(words_to_replace)
        template = replace_words('{[^\}]*}', answers, template)
        save_result(template, SAVE_TO_PATH)
        print(template)


if __name__ == "__main__":
    run_game()
