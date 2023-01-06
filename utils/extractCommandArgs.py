import re

def extract_args(text: str) -> str | None:
    """
    Returns the argument after the command.
    Used in Telegram. Replace / with your handler. (Example: "?, .")
    Examples:
    extract_arguments("/echo hello"): 'hello'
    extract_arguments("/echo"): ''
    extract_arguments("/echo@YourBot hello"): 'hello'
    
    :param text: String to extract the arguments from a command
    :return: the arguments if `text` is a command (according to is_command), else None.
    """

    regexp = re.compile(r"/\w*(@\w*)*\s*([\s\S]*)", re.IGNORECASE)
    result = regexp.match(text)
    return result[2] if text.startswith('/') else None