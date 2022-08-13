import logging
logging.basicConfig(filename = "mylog.log", level = logging.DEBUG)


class OverTheLimitException(Exception):
    def __init__(self, message):
        self.msg = message

def withdrawl(amount):
    if(amount > 500):
        logging.error("Withdrawal is greater than 500")
        raise OverTheLimitException("You cannot withdraw more than $500 per day")

withdrawl(600)
