# Name: menus
# Description: Text based menus

#INIT#
#imports#
import time

#objects#
class TBMenu:
    """
    text based menu
    parameters: string title, string[] info, string[] keys, string[] options, func[] functions, list[] parameters, string escape_key=
    """
    def __init__(self, title, info, keys, options, functions, parameters, escape_key='x'):
        """
        inits a text based menu
        """
        self.title = title
        self.info = info
        self.keys = keys
        self.options = options
        self.functions = functions
        self.escape_key = escape_key
        self.prompt = 'input: '
        self.escape = '\'{}\' to escape'
        self.error = 'invalid input'
        self.parameters = parameters
        self.sep_func = lambda: print('\n')
        #process#
        for i in range(len(keys)):
            keys[i] = str(keys[i])

    def display(self):
        """
        displays a text based menu
        parameters: none | returns: none
        """
        while True:
            self.sep_func()
            #title#
            if self.title != None:
                print(self.title)
                print('')
            #info#
            if self.info != None:
                for line in self.info:
                    print(line)
                print('')
            #options#
            if self.options != None:
                for i in range(len(self.options)):
                    print('{}. {}'.format(self.keys[i], self.options[i]))
            if self.escape != None:
                print(self.escape.format(self.escape_key))
            print('')
            #input#
            inp = input(self.prompt)
            if inp == self.escape_key:
                break
            elif inp not in self.keys:
                print(self.error)
                time.sleep(2)
                continue
            #action#
            self.functions[self.keys.index(inp)](*self.parameters[self.keys.index(inp)])

#MAIN#
if __name__ == '__main__':
    sub_menu = TBMenu('SUB MENU', ['some info or whatever'], ['1', '2'], ['print 1', 'print 2'],
                  [lambda: input('1'), lambda: input('2')], [[], []])
    main_menu = TBMenu('MAIN MENU', ['some info or whatever'], ['1', '2'], ['sub menu', 'pause'],
                  [sub_menu.display, input], [[], []])
    main_menu.display()

# Author: Jack Martin
# Start: 11/23/2020, Completion: 11/23/2020ish