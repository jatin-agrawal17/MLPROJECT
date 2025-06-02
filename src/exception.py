import sys  # Import sys to get exception details like line number and file name
import logging
from src.logger import logging
# Function to format a detailed error message
def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Get traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the name of the file where the error occurred
    error_message = "ERROR OCCURED IN PYTHON SCRIPT name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Use line number and error message
    )
    return error_message  # Return the formatted string

# Create a custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the base class constructor
        self.error_message = error_message_details(error_message, error_detail=error_detail)  # Create detailed message

    def __str__(self):
        return self.error_message  # What to print when this exception is shown
    


    
