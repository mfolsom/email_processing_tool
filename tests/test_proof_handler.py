import pytest
from email_handlers.proof_handler import ProofHandler

@pytest.fixture
def dummy_email():
    """Fixture to provide a dummy email object."""
    return type('Email', (object,), {
        'Subject': 'Hot Deals',
        'Body': 'Check out our new deals at https://example.com and https://test.com'
    })

@pytest.fixture
def proof_handler(dummy_email):
    """Fixture to provide a ProofHandler instance."""
    return ProofHandler(dummy_email)

def test_get_subject(proof_handler):
    assert proof_handler.get_subject() == 'Hot Deals', "The subject should be 'Hot Deals'"

def test_get_body(proof_handler):
    assert proof_handler.get_body() == 'Check out our new deals at https://example.com and https://test.com', \
        "The body text did not match the expected value"

def test_get_links(proof_handler):
    links = proof_handler.get_links()
    assert len(links) == 2, "There should be two links in the email body"
    assert 'https://example.com' in links, "The link 'https://example.com' should be in the list of links"
    assert 'https://test.com' in links, "The link 'https://test.com' should be in the list of links"