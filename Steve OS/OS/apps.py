## Used to create applications for SteveOS
import storage_control
import os
def run(name):
    class_reference = globals()[name.capitalize()]
    instance = class_reference()
    instance.run()


class Printer():
    def run(self):
        os.system('cls')
        print('Printer')
        print('*******')
        while True:
            filepath = input('Please provide a filepath: ')
            data = storage_control.read(filepath)
            if type(data) == dict:
                print('You have provided a directory.')
                
            else:
                print('You have provided a file.')
