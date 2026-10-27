
import os

# Get the name from the environment variable
# Use "World" if no name is provided
name = os.getenv("WHO_TO_GREET", "World")

# Display the greeting
print(f"Hello {name}!")

# Display a message about GitHub Actions
print("This program is running inside GitHub Actions.")
