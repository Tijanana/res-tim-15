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


# Convert writer names to writer objects
def IdentifyWriters(writers_to_identify):
    identified_writers = []
    for writer_name in writers_to_identify:
        identified_writers.append(IdentifyWriter(writer_name))

    return identified_writers


# Convert writer name to writer object
def IdentifyWriter(writer_name):
    global writers
    for writer in writers:
        if writer.__str__() == writer_name:
            return writer
    return None


# Prompts user to change writer states
def ManageWriters():
    writers_to_change = SelectWriters()

    if not writers_to_change:
        return

    for writer in writers_to_change:
        writer.SwitchState()


# Gets writer names adapted for inquirer2 checkbox
def GetCheckboxWriters():
    global writers
    checkbox_writer_names = []
    for writer in writers:
        checkbox_writer_names.append({'name': writer.__str__()})

    return checkbox_writer_names


# Creates new writer and
def CreateWriter(show_result=True):
    new_writer = GenerateWriter()
    AddWriter(new_writer)

    if show_result:
        print(f'{new_writer} created successfully')
        input()


# Generates new writer
def GenerateWriter():
    os.system('cls' if os.name == 'nt' else 'clear')
    new_writer = Writer(next_writer_id)
    return new_writer


# Adds writer to data
def AddWriter(writer):
    global next_writer_id
    next_writer_id += 1
    writers.append(writer)
    writer_names.append(writer.__str__())


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


# Prompt user to select multiple writers
def SelectWriters():
    os.system('cls' if os.name == 'nt' else 'clear')
    checkbox_writer_names = GetCheckboxWriters()
    questions = [
        {
            'type': 'checkbox',
            'name': 'writers',
            'message': 'Select writers to switch state',
            'choices': checkbox_writer_names
        }
    ]
    answers = prompt.prompt(questions)
    writers_to_change = answers['writers']
    if not writers_to_change:
        return

    writers_to_change = IdentifyWriters(writers_to_change)
    return writers_to_change


if __name__ == '__main__':
    main()
