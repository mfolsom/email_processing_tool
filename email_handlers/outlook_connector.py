import win32com.client

class OutlookConnector:
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(6)  # 6 corresponds to the Inbox

    def get_folder(self, folder_path):
        """Navigate to a specific folder given a list of folder names."""
        current_folder = self.inbox
        for folder_name in folder_path:
            current_folder = current_folder.Folders[folder_name]
        return current_folder
