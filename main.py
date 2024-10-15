from email_handlers.outlook_connector import OutlookConnector
from email_handlers.email_manager import EmailManager
from email_handlers.message_processor import MessageProcessor

def main():
    # Initialize Outlook connection and folder navigation
    connector = OutlookConnector()
    folder_path = ["Starbucks", "Proofs"]  # Path to the specific folder
    proofs_folder = connector.get_folder(folder_path)

    # Manage emails in the folder
    email_manager = EmailManager(proofs_folder)

    # Get flagged emails
    flagged_emails = email_manager.get_flagged_emails()

    # Process messages
    processor = MessageProcessor()

    if flagged_emails:
        processor.process_flagged_emails(flagged_emails)
    else:
        first_email = email_manager.get_first_email()
        processor.process_first_email(first_email)

if __name__ == "__main__":
    main()
