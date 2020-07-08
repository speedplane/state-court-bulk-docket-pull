from modules import global_variables
from modules import file_browser
import main
import os

def select_paths_menu(pdfOption=True):
    """
    This displays a menu to the user allowing them to choose file paths to save their downloaded data to.
    It handles their choices and changes the global variables representing the file paths for saving.
    """
    print("Below are the current settings for finding and saving files:\n")
    print(f"[1] The CSV file filled with docket numbers is located at:\n{os.path.abspath(global_variables.CSV_INPUT_PATH)}\n")
    print(f"[2] JSON Files are saved to and retrieved from:\n{os.path.abspath(global_variables.JSON_INPUT_OUTPUT_PATH)}\n")
    if pdfOption == True:
        print(f"[3] PDF Files are saved to:\n{os.path.abspath(global_variables.PDF_OUTPUT_PATH)}\n")
    print("To change these paths. Type the number for the path you want to change and press ENTER.\n")
    print("If you are happy with the current selection, simply press ENTER.\n")

    # Prompts the user for a choice and saves it in a variable.
    userChoice = input()

    # Choice 1 is to edit the path to the input csv full of docket numbers.
    if userChoice == "1":
        print("Select the path of your input csv file.")
        print("Press ENTER to open the file browser.")
        input()

        csvChoice = file_browser.browseCSVFiles()

        # global global_variables.CSV_INPUT_PATH
        global_variables.CSV_INPUT_PATH = csvChoice

        main.clear()
        select_paths_menu()

    # Choice 2 is to edit the path to the json files.
    if userChoice == "2":
        print("Select the path where you would like to store your JSON files.")
        print("Press ENTER to open the file browser.")
        input()
        jsonChoice = file_browser.browseDirectories('json-output')

        # global global_variables.JSON_INPUT_OUTPUT_PATH
        global_variables.JSON_INPUT_OUTPUT_PATH = jsonChoice

        main.clear()
        select_paths_menu()

    # Choice 3 is to edit the path where the folders full of PDF files will be saved.
    if userChoice == "3":
        print("Select the path where you would like to store your PDF files.")
        print("Press ENTER to open the file browser.")
        input()
        pdfChoice = file_browser.browseDirectories('pdf-output')

        # global global_variables.PDF_OUTPUT_PATH
        global_variables.PDF_OUTPUT_PATH = pdfChoice

        main.clear()
        select_paths_menu()

    # If the user doesnt make a choice and just presses ENTER, the program exits this menu and moves forward
    else:
        main.clear()