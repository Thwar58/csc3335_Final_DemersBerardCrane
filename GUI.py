import PySimpleGUI as sg
import DictPoemGen as pg
# got a lot of help from the documentation https://pypi.org/project/PySimpleGUI/ because it is
# all of our first times making a python gui
def startGUI():
    # Define the window's contents
    layout = [[sg.Text("Please enter nouns (comma separated)")],
            [sg.Input(key='-NOUNS-')],
            [sg.Text("Please enter verbs (comma separated)")],
            [sg.Input(key='-VERBS-')],
            [sg.Button('Generate'), sg.Button('Quit')]]

    # Create the window
    window = sg.Window('Mad Libs Poems', layout)

    # Display and interact with the Window using an Event Loop
    
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        window.close()
    if event == 'Generate':
        nouns = values['-NOUNS-'].replace(" ", "").split(',')
        verbs = values['-VERBS-'].replace(" ", "").split(',')
        poem = pg.genPoem(8)
        print("creates poem")
        window.close()
    
        #replaces nouns and verbs here
        poem = pg.replaceNouns(poem,nouns)
        poem = pg.replaceVerbs(poem,verbs)


        #makes layout for display window
        displayLayout = [[sg.Text('Finalized Mad Lib Poem')],
                    [sg.Text(poem)],
                    [sg.Button('Try Again'), sg.Button('Quit')]]
        print("creates layout")
        # Finish up by removing from the screen
        #window.close()
        print("closes window")
        # Create the window
        finalWindow = sg.Window('Final Poem', displayLayout)
        event, values = finalWindow.read()
        print("opens new window")
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            finalWindow.close()
        if(event == 'Try Again'):
            finalWindow.close()
            startGUI()
startGUI()