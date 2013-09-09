from QuickKeylogger import keylogger

class KeyBinder(keylogger.KeyLogger):

    def __init__(self, func_dict={}):
        self.func_dict = func_dict

    def respond(self, key):
        """ Responds to presses

        Takes only one argument that contains key press data.
        """
        func = self.func_dict.get(key, None)
        if func:
            func()

    def register_bindings(self, user_dict, force=True):
        """ Register user defined dictionary of functions

        If force is True, override existing registered functions
        """
        if force:
            self.func_dict.update(user_dict)
        else:
            dupes = set(self.func_dict.keys()) ^ set(user_dict)
            reduc = {k:v for k,v in user_dict.iteritems() if k not in dupes}
            self.func_dict.update(user_dict)

if __name__ == "__main__":
    import xerox

    kb = KeyBinder()

    def stop():
        """ Ends key capturing

        """
        kb.stop_capture()

    def transpose_csv():
        """ Transposes csv data

        Takes copied csv data from the copy buffer, rotates it, and
        replaces it
        """
        data = xerox.paste().split("\n")
        transposed = zip(*[ x.strip().split(",") for x in data])
        new_text = "\n".join([",".join(y) for y in transposed])
        xerox.copy(new_text)

    bindings = {"ctrl+shift+F3" : transpose_csv,
                "ctrl+shift+F1" : stop}
    kb.register_bindings(bindings)
    kb.start_capture()
