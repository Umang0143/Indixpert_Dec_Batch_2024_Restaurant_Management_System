class Validator:
    
    @staticmethod
    def is_valid_name(name):
        return name.isalpha()

    @staticmethod
    def is_valid_email(email):
        return (
            "@" in email and
            "." in email and
            email.index("@") < email.rindex(".") and
            email.count("@") == 1 and
            not email.startswith("@") and
            not email.endswith("@") and
            not email.endswith(".")
        )

    @staticmethod
    def is_valid_contact(contact):
        return (
            contact.isdigit() and
            len(contact) == 10 and
            contact != "0000000000"
        )

    @staticmethod
    def is_valid_address(address):
        return len(address.strip()) > 0
    
    @staticmethod
    def is_valid_password(password):
        return len(password) >= 6