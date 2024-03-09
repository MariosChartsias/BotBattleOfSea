def redirect(isValidationSuccess):
    if(isValidationSuccess):
        return "success.html"
    else:
        return "registration.html"