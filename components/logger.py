import os


class Logger:
    @staticmethod
    def StartLogger():  # pragma: no cover
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        f = open("log.txt", "w")
        f.close()

    @staticmethod
    def LogAction(action: str):  # pragma: no cover
        with open("log.txt", "a") as file:
            file.write(f'{action}\n')
