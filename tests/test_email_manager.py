import pytest
from unittest.mock import MagicMock
from email_handlers.email_manager import EmailManager

@pytest.fixture
def mock_folder():
    """Fixture to provide a mocked folder with mock messages."""
    folder = MagicMock()
    mock_message1 = MagicMock()
    mock_message1.Subject = "Test Subject 1"
    mock_message1.Body = "This is the body of email 1."
    mock_message1.FlagStatus = 2  # Flagged

    mock_message2 = MagicMock()
    mock_message2.Subject = "Test Subject 2"
    mock_message2.Body = "This is the body of email 2."
    mock_message2.FlagStatus = 0  # Not flagged

    folder.Items = MagicMock()
    folder.Items.GetFirst.side_effect = [mock_message1, None]  # First call returns mock_message1, then None
    folder.Items.GetNext.side_effect = [mock_message2, None]  # First call returns mock_message2, then None

    return folder

def test_email_manager_init(mock_folder):
    # Act
    email_manager = EmailManager(mock_folder)

    # Assert
    assert email_manager.folder == mock_folder, "EmailManager should store the provided folder"

def test_get_flagged_emails(mock_folder):
    # Arrange
    email_manager = EmailManager(mock_folder)

    # Act
    flagged_emails = email_manager.get_flagged_emails()

    # Assert
    assert len(flagged_emails) == 1, "There should be one flagged email"
    assert flagged_emails[0].Subject == "Test Subject 1", "The flagged email should have the correct subject"

def test_get_first_email(mock_folder):
    # Arrange
    email_manager = EmailManager(mock_folder)

    # Act
    first_email = email_manager.get_first_email()

    # Assert
    assert first_email.Subject == "Test Subject 1", "The first email should have the correct subject"
    assert first_email.Body == "This is the body of email 1.", "The first email should have the correct body"
