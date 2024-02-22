import os.path
import converter
import wmaFinder
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty

Window.size = (480, 480)
# wmaFinder.find_wma(folder="/home/spiced/Music/Music/Music/System Of A Down/Unknown Album/")


class MainInterface(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return self

    # def on_enter_pressed(self, ID, input):
    #     print("enter has been pressed")

    def search_button(self, ID, input):
        path = input.text
        # Check if the entered text is a directory
        if os.path.isdir(path):
            # Use the file finder function to search for .wma files recursively
            file_list = wmaFinder.find_wma(folder=f"{path}")
            # check if any .wma files were found
            if file_list:
                num_files = len(file_list)
                # Filter the file list to include only .wma files
                wma_files = [file for file in file_list if file.endswith('.wma')]
                # Create a string with the number of files found and their names
                songs_found = f"Number of files found: {num_files}\n\n"
                songs_found += '\n\n'.join(wma_files)
                # Here we assign the text to the label
                ID.text = songs_found
            # This statement returns an error when no wma files were found
            else:
                ID.text = 'No .wma file were found.'
        # This statement returns an error when no file path was provided
        else:
            ID.text = 'Please input a correct file directory.'

    def wma_convert(self, ID, input):
        ID.text = "Please wait, this may take awhile."
        wma_dir = input.text
        if os.path.isdir(wma_dir):
            converter.convert_wma(directory=f'{wma_dir}')
            file_list = wmaFinder.find_wma(folder=f"{wma_dir}")
            wma_files = [file for file in file_list if file.endswith('.wma')]
            mp3_files = f"Files converted: \n\n"
            mp3_files += '\n\n'.join(wma_files).replace(".wma", ".mp3")
            ID.text = mp3_files
        else:
            ID.text = "No valid file directory was provided."


class ScrollableLabel(ScrollView):
    # This class allows use of scrollable text box
    text = StringProperty('')


class MyApp(App):
    pass


MyApp().run()
