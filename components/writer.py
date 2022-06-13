import os
import threading
import time
from random import randint

from inquirer2 import prompt

from components.replicator_sender import ReplicatorSender
from constants.codes import Codes, Code
from models.receiver_property import ReceiverProperty


class Writer:
    terminate = False

    def __init__(self, id):
        self.id = id
        self.activity = True

    @staticmethod
    def Menu():
        questions = [
            {
                'type': 'list',
                'name': 'option',
                'message': 'Select option',
                'choices': ['Send data', 'Exit writer']
            }
        ]
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            answers = prompt.prompt(questions)
            selected_option = answers['option']
            if selected_option == 'Send data':
                Writer.__SendDataPrompt()
            elif selected_option == 'Exit writer':
                break

    # To Replicator Sender
    @staticmethod
    def __SendDataPrompt():
        questions = [
            {
                'type': 'list',
                'name': 'code',
                'message': 'Code',
                'choices': Codes,
            },
            {
                'type': 'input',
                'name': 'value',
                'message': 'Value',
                'validate': lambda x: True if Writer.__ValidateValue(x) else 'Invalid value'
            }
        ]
        answers = prompt.prompt(questions)
        code = Code[answers['code']]
        value = int(answers['value'])
        data = ReceiverProperty(code, value)
        ReplicatorSender.ReceiveData(data)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Data sent')
        input()

    @staticmethod
    def StartWriter():
        new_thread = threading.Thread(target=Writer.__AutomaticallySendData)
        new_thread.start()

    @staticmethod
    def __AutomaticallySendData():
        while True and not Writer.terminate:
            time.sleep(2)
            code = Code[Codes[randint(0, 7)]]
            value = randint(1, 99999)
            receiver_property = ReceiverProperty(code, value)
            ReplicatorSender.ReceiveData(receiver_property)

    @staticmethod
    def __ValidateValue(value):
        try:
            if (int(value)) > 0:
                return True
            return False
        except:
            return False

    def SwitchState(self, new_state=None):
        if new_state is None:
            self.activity = not self.activity
        else:
            self.activity = new_state

    def __str__(self):
        activity = ''
        if self.activity:
            activity = 'On'
        else:
            activity = 'Off'
        return f'Writer {self.id} {activity}'
