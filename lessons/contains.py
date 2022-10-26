"""An example of a list utility algorithm."""

    # Name: Contains
    # Function with 2 parameters:
    # needle - what we're seaching for
    # haystack - what we're seaching through
    # Return type: bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Start from frist index   
    i: int = 0
    # Loop through each index of list
    while i < len(haystack):
        #   Test if equal to needle
        if haystack[i] == needle:
         #       # Yes! Return True
            return True
        i += 1
    # Return False
    return False
