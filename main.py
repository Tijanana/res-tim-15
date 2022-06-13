import os
import threading

from inquirer2 import prompt

from components.writer import Writer

writers = []
writer_names = []
next_writer_id = 1


def main():
    Execute()


def Execute():
    automatic_writer_thread = threading.Thread(target=Writer.StartWriter)
    automatic_writer_thread.start()
    CreateWriter()
    Menu()


def Menu():
    while True:
        user_input = GetUserInput()
        ExecuteUserInput(user_input)


# Gets user input for main menu
def GetUserInput():
    os.system('cls' if os.name == 'nt' else 'clear')
    questions = [
        {
            'type': 'list',
            'name': 'menu',
            'message': 'Select option',
            'choices': ['Use writer', 'Turn On/Off writers', 'Create new writer', 'Exit']
        }
    ]
    answers = prompt.prompt(questions)
    return answers['menu']


# Executes selected action
def ExecuteUserInput(user_input):
    if user_input == 'Use writer':
        UseWriter()
    elif user_input == 'Turn On/Off writers':
        ManageWriters()
    elif user_input == 'Create new writer':
        CreateWriter()
    elif user_input == 'Exit':
        os.system('cls' if os.name == 'nt' else 'clear')
        Writer.terminate = True
        exit()


# Select and use active writer
def UseWriter():
    # TODO: Implement
    #  Implement
    pass


# Prompts user to change writer states
def ManageWriters():
    # TODO: Implement
    #  Implement
    pass


# Creates new writer and
def CreateWriter():
    # TODO: Implement
    #  Implement
    pass


if __name__ == '__main__':
    main()
