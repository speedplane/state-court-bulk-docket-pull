# State Court Bulk Docket Pull


## The Files:

### _auth.py

The first place you'll need to go before experimenting with this script.
You need to enter your Docket Alarm login information here.
When you aredone, rename it to "auth.py" by removing the underscore,
and you are ready to go!

### main.py

This is the file used to launch the program. It contains a variety of functions:

#### writeToJSONFile(folder, fileName, data)

takes in the name of a folder in the current directory, the name of
the file you want to create, and the json object you want to write to
the file.

#### authenticate()

Returns the authentication token to make API calls.
Make sure that auth.py is filled out!

#### list_courts()

Prints all the courts to the console and returns a list of courts.

#### get_parameters()

Returns all of the parameters you can use when making a post request to the /searchdirect endpoint.

#### get_results(party_name, docketnum)

Takes in the name of a party and the docket number as a parameter,
returns the Docket Alarm search results. You can make calls to the
/getdocket endpoint with these results to get more detailed information
on the docket you are looking for.

#### get_docket(docket)

Takes in a docket number as an argument and returns all the JSON data
available from Docket Alarm.

#### format_case_number(unformatted_case_number)

Trims off excess data from the case numbers
provided, and returns the same number in a
form that Docket Alarm can search for.

#### loop_dataframe()

loops through the spreadsheet listed in the global variable toward the top of
this script. Returns docket info from each.

### death-penalty-project.csv

The example csv file used. Feel free to change the file and tweak the script to 
suit your own use case!

### JSON files.zip

A backup of the 'result' folder from when I ran this script with isCached=True on 6/22/20.
This contains all the cases specified in the spreadsheet as JSON files.

### result folder

Where your JSON files will appear when you run the main.py script.
