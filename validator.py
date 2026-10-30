class validator:
    @staticmethod
    def get_int(prompt, minimum=None, maximum=None):
        while True:
            raw = input(prompt).strip()
            try:
                value = int(raw)
            except ValueError:
                print("Please enter a whole number.")
                continue
            if minimum is not None and value < minimum:
                print("Must be at least {}.".format(minimum))
                continue
            if maximum is not None and value > maximum:
                print("Must be at most {}.".format(maximum))
                continue
            return value

    @staticmethod
    def get_float(prompt, minimum=None):
        while True:
            raw = input(prompt).strip()
            try:
                value = float(raw)
            except ValueError:
                print("Please enter a number.")
                continue
            if minimum is not None and value < minimum:
                print("Must be at least {}.".format(minimum))
                continue
            return value

    @staticmethod
    def get_str(prompt):
        while True:
            raw = input(prompt).strip()
            if raw:
                return raw
            print("Cannot be empty.")

    @staticmethod
    def get_choice(prompt, choices):
        valid = [c.upper() for c in choices]
        while True:
            raw = input(prompt).strip().upper()
            if raw in valid:
                return raw
            print("Invalid choice. Options: " + ", ".join(valid))