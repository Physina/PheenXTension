import time
import datetime as dt

def display_txt(texts:list[str], yield_mode:bool=False, pass_query:bool=False) -> None | str:
    """Displays all text segments from input list in order, waiting (len(segment)*2)*{0.33} seconds in-between\n
    * yield_mode: Wether or not this function should behave as a generator, simply **passing on** the individual texts or not.
    * pass_query: *If* texts-argument is a list, return the last string after printing for use in... oh, idk... THE GODFATHER FUNCTION: gtx.confirmor! :D
    """
    if texts is []: raise ValueError("display_txt failed bc an empty list was passed... WHERE B DA TEXT??")
    else: print(f"DEBUG: {texts} appears not empty. Continuing!")
    while texts != []:
        try:
            text:str = str(texts[0])
            t = len(text)*8/100
            print("DEBUG:", t)
            if yield_mode == True:
                yield text; print(f"[[DEBUG: display_sleep_start, sleeping {t}secs...]]"); time.sleep(t); print("[[DEBUG: display_sleep_end]]")
            else:
                if pass_query == True and len(texts) == 1:
                    time.sleep(t)
                    return text
                else:
                    print(text)
                    time.sleep(t)
            del texts[0]
        except TypeError as te: raise TypeError(f"Exception when attempting to convert {texts[0]} of {texts} to str: {te}")
    return None



def stdz_input(instruction:str|list[str]):
    """Applies custom formatting (see below) to input function, for io-optics' sake! :D\n
    -> takes one singular string, passes it as 'prompt' argument to input(), and returns the input given by user.\n
    (Essentially just a "make-fancy" wrapper around input().)
    ( Naturally, this is compatible with display_txt(yield_mode=True), since it returns one string to be used in this function here! )\n
    Format printed:\n
      \>\> {instruction}\n
      << {...input by user...}"""
    if type(instruction) == str:
        print("\n >>", instruction)
        return input(" << ")
    elif type(instruction) == list:
        print("############\nDEBUG: Is input list deminishing...?\nLength =", len(instruction), "\n############")
        if len(instruction) not in [1, 0]:
            print(display_txt(instruction[0], yield_mode=True))
        elif len(instruction) == 1:
            print(" >> ", instruction[0])
        else:
            assert instruction == []
            return input(f" << ")
    else: raise TypeError("'instructions' argument of stdz_input is neither str nor list[str].")



def confirmor(texts:str|list[str]="Do you wish to continue?", log_inverse:bool=False, add_True_opt=[], add_False_opt=[], retries:int=3) -> bool:
    """This is a general purpose confirmor function. Any user input (i.e. decisions, settings, etc.!), accidental or otherwise, can require confirmation this way.
    ...In console only, I should accentuate. :/
    * Prompt format: "[text] (y/n):"
    * Retries possible, but default to 3 (see DOCU below!)
    * ALSO COMPATIBLE WITH DISPLAY.TXT()!!!

    DOCUMENTATION:\n
    NOTE THAT INPUT IS CASE-INSENSITIVE ON LETTERS!
    * text: Any text to be parsed as hold-up question to the user. If list is parsed, last element of list is used to ask for confirmation.
    * log_inverse: Illustrated best by default text: function would output True if choice was "Yes". Reverse outputs the logical not-operation.
    * add_True_opt: Pass lists here for custom availability of options to be chosen, i.e. anticipated typos, quirky responses, or easter eggs! ;)
    * add_False_opt: Same custom flexibility as add_True_opt here. :)
    * retries: confirmor is embedded in a for loop to allow for misspells to happen without undesires behaviour. The "retries" argument specifies the iteration limit, as I am unwilling to specify a default output. I think that would be hurrendous! >:o
    """
    for attempts in range(retries):
        if type(texts) == str:
            inp = input(f"{texts} (y/n): \n>> ").lower()
        elif type(texts) == list[str]:
            # TODO: (MAYBEEE?!) IMPLEMENT LATER!!!
            # Very stressed by procrastination rn...! ,:)
            # --23.07.2024
            """for text in texts:
                print("############\nDEBUG: Is input list deminishing...?\nLength =", len(instruction), "\n############")
                if len(texts) not in [2, 1]:
                    print(display_txt(texts, yield_mode=True))
                elif len(texts) == 2:
                    print(" <<", texts[1])
                else:
                    inp:str = input("\n >>", instruction[0])
                    return inp"""

        True_Options = ["yes", "ye", "y", "absolutely", "definetly", "totally", "totally!", "fuck this!", "yes, fuck this!", "yes please!", "yes please", "yes, please", "yes please!"]
        False_Options = ["no", "n", "please no!", "not done yet", "i'm not done yet", "i'm not done yet!"]
        x:str
        for x in add_True_opt:
            True_Options.append(x.lower())
        for x in add_False_opt:
            False_Options.append(x.lower())

        if inp in True_Options:
            out = True
            if log_inverse == True:
                out = False
            break
        elif inp in False_Options:
            out = False
            if log_inverse == True:
                out = True
            break
        print("Error, try again!")
    if attempts == retries-1:
        display_txt(texts=["Well shit! You made it past the decision limit... Happy Glühstrumpf! ._.", "The confirmor will pass your response instead of a boolean now instead! :)"])
        time.sleep(2.0)
    return out



def current_dt() -> str:
    "return {nows.year}{nows.month}{nows.day}-{nows.hour}{nows.minute}\n\n...In case you were interested. :)"
    nows = dt.datetime.now()
    return f"{nows.year}{nows.month}{nows.day}-{nows.hour}{nows.minute}"





"""IDEA 22.06.24:
Diagnostics:
(i.e. for catching errors and getting information about those errors at runtime already via console! ;D)

to be printed:
* variable type vs. expected type
* ...

def exception_handler():
## EXAMPLES:
    #####
    i = input("Try floats, tuples, etc...!\n")
    try:
        i = tuple(i)
    except Exception as e: print(e)
    #####
    if type(Dimensions) != tuple:
            try:
                Dimensions = tuple(Dimensions)
            except Exception as e:
                print("Yo, sometingg wong with Board Dimensions: ", e)
        else: pass

"""





def type_corrector(obj, desired_type:type):
    """FOR REFERENCE:
    while True:
        i = input("Try floats, tuples, etc...!\n")
        try:
            t = tuple(i)
            print(type(t), ": ", t)
        except Exception as e: print(e)
        try:
            l = list(i)
            print(type(l), ": ", l)
        except Exception as e: print(e)
        try:
            fl = float(i)
            print(type(fl), ": ", fl)
        except Exception as e: print(e)
    """
    if type(obj) != desired_type:
        try:
            obj = desired_type(obj)
        except Exception as e:
            print("Calling type_corrector was unable to solve the issue: ", e)
            # IDEALLY OFC MORE COMES AFTER THIS BASED ON THE EXCEPTION TYPE!!
            # ...that's ironic! I determine behaviour of a type correction function based on the type of an Exception! ;D

    else: print("Calling type_corrector was a waste of time ??")
    return obj






## DEBUG::
if __name__ == "__name__":
    display_txt(["AAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAA"])