import os
import re
import threading

from inquirer2 import prompt

from components.logger import Logger
from components.replicator_receiver import ReplicatorReceiver
from components.writer import Writer
from constants.codes import Codes
from constants.readers import readers

writers = []
writer_names = []
next_writer_id = 1


def main():  # pragma: no cover
    Execute()


def Execute():  # pragma: no cover
    automatic_replicator_receiver_thread = threading.Thread(target=ReplicatorReceiver.SendData)
    automatic_writer_thread = threading.Thread(target=Writer.StartWriter)
    logger_writer_thread = threading.Thread(target=Logger.StartLogger)
    automatic_replicator_receiver_thread.start()
    automatic_writer_thread.start()
    logger_writer_thread.start()
    CreateWriter(show_result=False)
    Menu()


def Menu():  # pragma: no cover
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
            'choices': ['Use writer',
                        'Get values for code in a time interval',
                        'Turn On/Off writers',
                        'Create new writer',
                        'Exit']
        }
    ]
    answers = prompt.prompt(questions)
    return answers['menu']


# Executes selected action
def ExecuteUserInput(user_input):  # pragma: no cover
    if user_input == 'Use writer':
        UseWriter()
    elif user_input == 'Get values for code in a time interval':
        GetValuesByInterval()
    elif user_input == 'Turn On/Off writers':
        ManageWriters()
    elif user_input == 'Create new writer':
        CreateWriter()
    elif user_input == 'Exit':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Shutting down...')
        Writer.terminate = True
        ReplicatorReceiver.terminate = True
        exit()


# Select and use active writer
def UseWriter():  # pragma: no cover
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


def GetValuesByInterval():  # pragma: no cover
    questions = [
        {
            'type': 'list',
            'name': 'code',
            'message': 'Code',
            'choices': Codes,
        },
        {
            'type': 'input',
            'name': 'start_date',
            'message': 'Enter start date: (YYYY-MM-DD)',
            'validate': lambda x: True if ValidateRegex(x, '^[0-9]{4}-[0-9]{2}-[0-9]{2}$') else 'Invalid'
        },
        {
            'type': 'input',
            'name': 'start_time',
            'message': 'Enter start time: (HH:MM-SS)',
            'validate': lambda x: True if ValidateRegex(x, '^[0-9]{2}:[0-9]{2}:[0-9]{2}$') else 'Invalid'
        },
        {
            'type': 'input',
            'name': 'end_date',
            'message': 'Enter end date: (YYYY-MM-DD)',
            'validate': lambda x: True if ValidateRegex(x, '^[0-9]{4}-[0-9]{2}-[0-9]{2}$') else 'Invalid'
        },
        {
            'type': 'input',
            'name': 'end_time',
            'message': 'Enter end time: (HH:MM-SS)',
            'validate': lambda x: True if ValidateRegex(x, '^[0-9]{2}:[0-9]{2}:[0-9]{2}$') else 'Invalid'
        }
    ]
    answers = prompt.prompt(questions)
    code = answers['code']
    s_date = answers['start_date']
    s_time = answers['start_time']
    e_date = answers['end_date']
    e_time = answers['end_time']
    dataset = MapCodeToDataset(code)
    reader = readers[dataset]
    values = reader.GetValuesByInterval(code, s_date, s_time, e_date, e_time)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Values:')
    for value in values:
        print(f'\t{value}')
    input()


def ValidateRegex(user_input, regex):
    if re.match(regex, user_input):
        return True
    else:
        return False


def MapCodeToDataset(code):
    if code in ['CODE_ANALOG', 'CODE_DIGITAL']:
        return 1
    elif code in ['CODE_CUSTOM', 'CODE_LIMITSET']:
        return 2
    elif code in ['CODE_SINGLENOE', 'CODE_MULTIPLENODE']:
        return 3
    elif code in ['CODE_CONSUMER', 'CODE_SOURCE']:
        return 4


# Prompts user to change writer states
def ManageWriters():  # pragma: no cover
    writers_to_change = SelectWriters()

    if not writers_to_change:
        return

    for writer in writers_to_change:
        writer.SwitchState()


# Gets writer names adapted for inquirer2 checkbox
def GetCheckboxWriters():  # pragma: no cover
    global writers
    checkbox_writer_names = []
    for writer in writers:
        checkbox_writer_names.append({'name': writer.__str__()})

    return checkbox_writer_names


# Creates new writer and
def CreateWriter(show_result=True):  # pragma: no cover
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
def AddWriter(writer):  # pragma: no cover
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
def SelectWriters():  # pragma: no cover
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


if __name__ == '__main__':  # pragma: no cover
    main()
