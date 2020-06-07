import os
import re

from textwrap import dedent


TEMPLATE_PATH = 'madlib_cli/template.txt'
SAVE_TO_PATH = 'madlib_cli/result.txt'
ERROR_LOG = 'madlib_cli/error_log.txt'
WELCOME_MESSAGE = """
    **************************************
    **    Welcome to the MadLib game!   **
    **         Please follow the        **
    **        instructions below        **
    ** To quit at any time, type "quit" **
    **************************************
    """

FINAL_MESSAGE = """
    ***********************************
    **   Here\'s your story, enjoy!  **
    ***********************************
    """


def read_file(file_path: str) -> str:
    """Reads provided file if exists and returns its content, otherwise returns False

    Args:
        file_path (str): Path to the file to read

    Returns:
        str: File's content
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                new_template = f.read()
        except IOError as err:
            log_error(err)
            print(f'Could\'t read the file {file_path}')
            return False
        else:
            return new_template
    else:
        print(f'File {file_path} doesn\'t exist')
        return False


def save_result(text: str, file_path: str) -> None:
    """Saves given string into the file

    Args:
        text (str): Text to be saved
        file_path (str): Path to the file
    """
    try:
        with open(file_path, 'w') as f:
            f.write(text)
    except IOError as err:
        log_error(err)
        print('File coudn\'t be saved')


def get_user_answers(questions: list) -> list:
    """Function that prompts the user to answer the given questions ans returns those answers

    Args:
        questions (list): List of questions to be asked

    Returns:
        list: List of user entries
    """
    answers = []
    total = len(questions)
    for i in range(total):
        print(
            f'Please type {questions[i]} and press enter to submit ({i}/{total} answered)')
        user_input = input()
        if user_input == 'quit':
            print('We\'re sorry to see you go, please come back!')
            return False
        else:
            while not user_input:
                print(f'{questions[i]} can\'t be empty')
                user_input = input()
            answers.append(user_input)
    return answers


def replace_words(pattern: str, content: list, template: str) -> str:
    """Iteratively replaces the next instance of found pattern with a given list of words within a given template 

    Args:
        pattern (str): RegEx pattern
        content (list): List words to use as replacement
        template (str): Text to be modified

    Returns:
        str: Given template with words replaced
    """
    for word in content:
        template = re.sub(pattern, word, template, 1)
    return template


def log_error(err: str) -> None:
    """Saves an error into the log file

    Args:
        err (str): Error message
    """
    save_result(err, ERROR_LOG)


def run_game():
    """Runs the game by calling other functions
    """
    try:
        print(dedent(WELCOME_MESSAGE))
        template = read_file(TEMPLATE_PATH)
        if template:
            questions = re.findall('{([^\}]*)}', template)
            answers = get_user_answers(questions)
            if answers:
                template = replace_words('{[^\}]*}', answers, template)
                save_result(template, SAVE_TO_PATH)
                print(dedent(FINAL_MESSAGE))
                print(template)
    except KeyboardInterrupt:
        print('We\'re sorry to see you go, please come back!')


if __name__ == "__main__":
    run_game()
