import readline
import sys

class AcronymGenerator:
    def __init__(self):
        pass

    def get_user_input(self):
        while True:
            try:
                # Check if command line arguments are provided
                if len(sys.argv) > 1:
                    return ' '.join(sys.argv[1:])
                else:
                    # Get user input as a string
                    user_input = str(input("Enter a Phrase (Ctrl+C to exit): "))

                    # Check if the input is not empty
                    if user_input:
                        return user_input
                    else:
                        print("Please enter a non-empty phrase.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption
                print("\nProgram interrupted. Exiting.")
                return None
            except Exception as e:
                # Handle other exceptions
                print(f"An error occurred: {e}")

    def generate_acronym(self, user_input):
        # Split the input into a list of words
        text = user_input.split()

        # Printing splitted text for debugging
        print("Splitted Text:", text)

        # Initialize an empty string for the acronym
        acronym = " "

        # Iterate through each word in the input
        for word in text:
            # Concatenate the first letter of each word (converted to uppercase) to the acronym
            acronym = acronym + str(word[0]).upper()

        # Print the final acronym
        print("Acronym:", acronym)

if __name__ == "__main__":
    # Create an instance of the AcronymGenerator class
    generator = AcronymGenerator()

    # Get user input
    user_input = generator.get_user_input()

    # If user input is provided, generate acronym
    if user_input:
        generator.generate_acronym(user_input)
