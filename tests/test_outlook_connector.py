import pytest
from unittest.mock import patch, MagicMock
from email_handlers.outlook_connector import OutlookConnector

@patch('win32com.client.Dispatch')
def test_outlook_connector_init(mock_dispatch):
    # Arrange
    mock_namespace = MagicMock()
    mock_dispatch.return_value.GetNamespace.return_value = mock_namespace

    # Act
    connector = OutlookConnector()

    # Assert
    mock_dispatch.assert_called_once_with("Outlook.Application")
    mock_dispatch.return_value.GetNamespace.assert_called_once_with("MAPI")
    assert connector.outlook == mock_namespace

def test_get_folder():
    with patch('win32com.client.Dispatch') as mock_dispatch:
        # Arrange
        mock_namespace = MagicMock()
        mock_inbox = MagicMock()
        mock_dispatch.return_value.GetNamespace.return_value = mock_namespace
        mock_namespace.GetDefaultFolder.return_value = mock_inbox

        # Mock folders structure
        mock_starbucks_folder = MagicMock()
        mock_proofs_folder = MagicMock()
        mock_inbox.Folders.__getitem__.side_effect = lambda name: mock_starbucks_folder if name == "Starbucks" else mock_proofs_folder
        mock_starbucks_folder.Folders.__getitem__.return_value = mock_proofs_folder

        # Act
        connector = OutlookConnector()
        result = connector.get_folder(["Starbucks", "Proofs"])

        # Assert
        assert result == mock_proofs_folder, "The result should match the mocked Proofs folder"
