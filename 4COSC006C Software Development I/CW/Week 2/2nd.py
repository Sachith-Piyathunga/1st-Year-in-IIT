#1ST semester my code - 20221948
#program for students to predict their credits

# Import the graphics module
import graphics

 # Function to get credits and calculate progression output
def get_progress_output():
    PASS_credits = 0
    DEFER_credits = 0
    FAIL_credits = 0

       # Get and check the credits for error handling
    PASS_input = input("Please enter your credits at pass: ")
       # # If the user inputs letters or symbols code stop through here
    if not PASS_input.isdigit():
        print("Please enter integer number only")  # Ask the user to enter Integer only
        return None
    PASS_credits = int(PASS_input)

    DEFER_input = input("Please enter your credits at defer: ")
       # If the user inputs letters or symbols code stop through here
    if not DEFER_input.isdigit():
        print("Please enter integer number only")  # Ask the user to enter Integer only
        return None
    DEFER_credits = int(DEFER_input)

    FAIL_input = input("Please enter your credits at fail: ")
       # If the user inputs letters or symbols code stop through here
    if not FAIL_input.isdigit():
        print("Please enter integer number only")  # Ask the user to enter Integer only
        return None
    FAIL_credits = int(FAIL_input)

            # Calculate total credits
    total_credits = PASS_credits + DEFER_credits + FAIL_credits

            # First check if all the  credits are in valid range or not
    if PASS_credits not in [0, 20, 40, 60, 80, 100, 120] or \
       DEFER_credits not in [0, 20, 40, 60, 80, 100, 120] or \
       FAIL_credits not in [0, 20, 40, 60, 80, 100, 120]:
        print("Out of range.")
        return None

            # Secondly check total credits are equal to 120
    if total_credits != 120:
        print("Total incorrect.")
        return None

            # Determine the outputs of the progression based on credits values
    if 80 <= PASS_credits < 100:
        print("Progress (module trailer)")
    elif 60 <= PASS_credits < 80:
        print("Progress")
    elif 40 <= PASS_credits < 60:
        if 60 <= FAIL_credits < 80:
            print("Retriever")
        elif FAIL_credits >= 80:
            print("Exclude")
        else:
            print("Do not progress – Retriever")
    elif PASS_credits == 20:
        if 40 <= DEFER_credits < 60:
            print("Retriever")
        elif DEFER_credits >= 60:
            print("Exclude")
        else:
            print("Do not progress – Retriever")
    elif PASS_credits == 0:
        if FAIL_credits >= 40:
            print("Exclude")
        else:
            print("Do not progress – Retriever")

            # Function to display histogram
def display_histogram(data):
    win = GraphWin("Progress Output Histogram", 400, 400)  # Create the graphics window

    categories = ["Progress", "Trailing", "Retriever", "Exclude"] # Define categories for the histogram
    colors = ["blue", "yellow", "purple", "green"]  # Get the colours for each category

    total_students = len(data) # Get the total number of students

            # Draw rectangles in the histogram for every category
    for i, category in enumerate(categories):
        count = data.count(i) # Count number of students are in each category
        height = count / total_students * 400 # Calculate the height of the rectangle
        rect = Rectangle(Point(i * 100, 400), Point((i + 1) * 100, 400 - height))
        rect.setFill(colors[i]) # Set the one colour to fill the rectangle
        rect.draw(win) # Draw the rectangle in the window

    win.getMouse() # Add mouse click to close the window
    win.close() # Close the graphics window

# Main loop for multiple outputs
data = [] # Initialize an empty list to store progression for outputs
while True:
    output = get_progress_output() # Get progression outputs for a student
    if output is not None:
        data.append(output) # Add output to the list

    user_input = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit: ")
    if user_input.lower() == 'q':
        break

# Display histogram
display_histogram(data)
