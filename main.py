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
    CreateWriter(show_result=False)
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
    selected_writer = SelectWriter()

    if not selected_writer:
        return

    selected_writer.Menu()


# Get list of names of all active writers
def GetActiveWriterNames():
    global writers
    active_writer_names = []
    for writer in writers:
        if writer.activity:
            active_writer_names.append(writer.__str__())

    return active_writer_names


# Convert writer name to writer object
def IdentifyWriter(writer_name):
    global writers
    for writer in writers:
        if writer.__str__() == writer_name:
            return writer
    return None


# Prompts user to change writer states
def ManageWriters():
    # TODO: Implement
    #  Implement
    pass


# Creates new writer and
def CreateWriter(show_result=True):
    # TODO: Implement
    #  Implement
    pass


# Prompt user to select a writer
def SelectWriter():
    os.system('cls' if os.name == 'nt' else 'clear')
    active_writers = GetActiveWriterNames()
    if not active_writers:
        print('No active writers')
        input()
        return

    global writer_names
    questions = [
        {
            'type': 'list',
            'name': 'writer',
            'message': 'Select writer',
            'choices': active_writers
        }
    ]
    answers = prompt.prompt(questions)
    selected_writer = IdentifyWriter(answers['writer'])
    return selected_writer


if __name__ == '__main__':
    main()
