class EmailManager:
    def __init__(self, folder):
        self.folder = folder
        self.messages = self.folder.Items
        self.messages.Sort("[ReceivedTime]", True)  # Sort by received time, descending

    def get_flagged_emails(self):
        """Retrieve all flagged emails in the folder."""
        flagged_emails = []
        message = self.messages.GetFirst()

        while message:
            try:
                if message.FlagStatus == 2:  # 2 means the message is flagged
                    flagged_emails.append(message)
                message = self.messages.GetNext()
            except Exception as e:
                print(f"Error processing message: {e}")
                break
        
        return flagged_emails

    def get_first_email(self):
        """Retrieve the first email in the folder."""
        return self.messages.GetFirst()
