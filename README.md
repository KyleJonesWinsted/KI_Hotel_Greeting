# Hotel Greeting

## How to run

To run the program simply clone this repository and run "app.py" in the Python 3 shell.

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

Finally, I chose to use "set_file_path()" in the main app file to add references to the JSON files that were being loaded in. Since this method of loading data is specific to this implementation of a greeting app I thought it would be important to make it obvious at the top of the app file that we were importing JSON files. This is similar to how I would typically include any database connection code at the start of the main app file to make it obvious where the application data was coming from.

## Reason for Python

I chose to use python for 3 main reasons.

1. Python is my most fluent language. I felt most comfortable utilizing list comprehension, raising custom error messages, and writing Unit Tests in Python.
2. Python can run on macOS and most distributions of Linux without installing any additional software thanks to the inclusion of the Python shell. The Python standard library also contained all of the functionality I knew I would need without requiring the user to install additional packages.
3. This assignment requires loading data from JSON and Python is, in my opinion, the best language for working with files local to the users computer, as well as accepting user input on the console.

## Verifying Correctness

Correctness of program was verified in two ways.

1. Acceptance Testing - I ran through the finished program to verify that all the requirement of the assignment were met. Then I ran through multiple times, each time attempting an unexpected user input to ensure the program handled all possible exceptions properly.

2. Black Box Testing - I also created multiple unit tests to verify all critical functions in each class produced the expected output or exception for the given input. The tests can be run with the following command.

        python3 -m unittest discover -vb


## Next Steps

If given more time to work on improving this application I would first work on a few things.

1. Move to a proper database instead of using JSON files to store application data. This would enable many of the following improvements.

2. Full create, update, and delete functionality for users created templates.

3. Support for querying guests and reservations rather than loading the entire contents of the Guests.json at program launch.

4. Implementing a proper GUI. The specific language and framework would depend on the deployment strategy for the application. For example, you could design a front-end web app in React and use the classes and functionality in this application to support a Flask or Django server running the necessary RESTful APIs.

5. Create test JSON files to run more of my code against without risk of damaging production data. This would also prevent tests from failing due to changes in production data.

