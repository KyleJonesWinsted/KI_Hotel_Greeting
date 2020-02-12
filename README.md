# Hotel Greeting

## How to run

To run the program simply clone this repository and run "app.py" in the Python shell.

    python3 app.py

Numbered menus will be presented to you. Simply type the number that corresponds to the option you would like.

    Select an option:

    [1] Option 1
    [2] Option 2

    > 1

When typing a custom greeting you must include the square brackets in your placeholder elements.

    Enter your custom greeting:

    > Hello [firstName]!
    # Outputs "Hello Kyle!"

At any time you can press Control + C to return to the main menu. If you are already on the main menu, the program will quit.

## Design Decisions

### UI

I chose to go with a simple command line utility so I could spend most of my time writing good object oriented code. This also allows the app to run on the widest variety of hardware since all you need is the Python shell, no need to worry about platform specific UI frameworks.

### Code

I decided to split each one of my classes into its own file to maximize readability and then imported each class where I needed it. 

Every class is self contained with good separation of concerns, so if any piece were to be swapped out everything would still work as expected. For example, DataController could be swapped out for one which connects to an SQL database and as long as there was still a class method called "get_all_guests()" the rest of the program could continue to reference "DataController.get_all_guests()" as it does now.

Though Python does not technically support private methods, I still chose to implement the standard practice of prefacing private methods with and underscore. This helps improve readability by making it obvious which methods are designed to be called outside the class itself.

Finally, I chose to use "add_file_path()" in the main app file to add references to the JSON files that were being loaded in. Since this method of loading data is specific to this implementation of a greeting app I thought it would be important to make it obvious at the top of the app file that we were importing JSON files. This is similar to how I would typically include any database connection code at the start of the main app file to make it obvious where the application data was coming from.

## Reason for Python

I chose to use python for 3 main reasons.

1. Python is my most fluent language. I felt most comfortable utilizing list comprehension, raising custom error messages, and writing Unit Tests in Python.
2. Python can run on macOS and most distributions of Linux without installing any additional software thanks to the inclusion of the Python shell. The Python standard library also contained all of the functionality I knew I would need without requiring the user to install additional packages.
3. This assignment requires loading data from JSON and Python is, in my opinion, the best language for working with files local to the users computer.

## Verifying Correctness

## Next Steps



