class MessageProcessor:
    @staticmethod
    def print_message_info(message):
        """Print the subject and body of the given message."""
        print(f"Subject: {message.Subject}")
        print(f"Body: {message.Body}")

    def process_flagged_emails(self, flagged_emails):
        """Process the flagged emails if any are found."""
        if len(flagged_emails) > 0:
            first_flagged = flagged_emails[0]
            print(f"Number of flagged emails: {len(flagged_emails)}")
            self.print_message_info(first_flagged)
        else:
            print("No flagged emails found.")
    
    def process_first_email(self, message):
        """Process the first email if no flagged emails are found."""
        print("Retrieving the first email.")
        self.print_message_info(message)
