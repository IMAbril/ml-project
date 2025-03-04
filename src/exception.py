import sys
import logging

def error_message(error: Exception, error_detail: sys) -> str:
    """
    Generates a detailed error message including the script name, line number, and error description.

    Args:
        error (Exception): The exception that was raised.
        error_detail (sys): The sys module to extract exception details.

    Returns:
        str: A formatted error message containing script name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name: str = exc_tb.tb_frame.f_code.co_filename
    message: str = "Error occurred in Python script [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return message

class CustomException(Exception):
    """
    A custom exception class that provides detailed error messages.

    Attributes:
        error_message (str): A formatted error message with script name, line number, and error details.
    """

    def __init__(self, error: Exception, error_detail: sys):
        """
        Initializes the CustomException with a formatted error message.

        Args:
            error (Exception): The exception that was raised.
            error_detail (sys): The sys module to extract exception details.
        """
        super().__init__(str(error))
        self.error_message: str = error_message(error, error_detail)

    def __str__(self) -> str:
        """
        Returns the error message.

        Returns:
            str: The formatted error message.
        """
        return self.error_message
