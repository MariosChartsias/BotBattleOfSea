import os
def redirect(isValidationSuccess):
    script_dir = os.path.dirname(__file__)  # Get the directory of the current script
    templates = os.path.join(script_dir, '..')
    if(isValidationSuccess):
        return "success.html"
    else:
        return "registration.html"