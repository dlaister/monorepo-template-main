#--------------------CLASS--------------------#
class Logger:
    _instance = None  # Private class variable to hold the single instance

    """
    Pre refactor, commented/modified down.
    """
    def __init__(self):
        # self.messages = [] # moved down
        pass

    def add_message(self, message):
        self.messages.append(message)

    """
    Refactored singleton class based on lecture slide 66, "Toy Example in Python".
    
    Singleton class from example replaced with local class, Logger. 
    """
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls) #creats the instance of
            print("Logger created exactly once") # validation of single creation
            cls._instance.init_Logger()
        else:
            print("Logger already created") #if the logger does exist, print this
        return cls._instance

    def init_Logger(self):
        self.messages = []

#--------------------MAIN--------------------#
def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
