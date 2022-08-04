import logging


class Loggen:
    @staticmethod
    def log():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fhandler=logging.FileHandler(filename='.\\Logs\\automaton.log',mode='a')
        formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger
