import os


class Logger:
    @staticmethod
    def StartLogger():
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        f = open("log.txt", "w")
        f.close()

    @staticmethod
    def LogAction(action: str):
        with open("log.txt", "a") as file:
            file.write(f'{action}\n')
