'''
    plugin template, implement setup and run method, this is entry point of tool box
'''
class Plugin:
    def __init__(self) -> None:
        self._name = "world"

    def setup(self):
        '''
            set the necessary parameters
        '''
        self._name = input("Enter your name: ")
        pass
    
    def run(self):
        '''
            run
        '''
        print("Hello ", self._name)