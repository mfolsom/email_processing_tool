import pytest
from email_handlers.link_verifier import LinkVerifier
from unittest.mock import patch

@pytest.fixture
def link_verifier():
    links = ["https://example.com", "https://invalid-link.com","https://www.starbucks.com/madeup"]
    return LinkVerifier(links)

def test_check_links_present(link_verifier):
    expected_links = ["https://example.com"]
    result = link_verifier.check_links_present(expected_links)
    assert result['status'] == 'pass', "Expected link should be found in the email"
    assert result['missing_links'] == [], "No links should be missing"

@patch('requests.head')
def test_verify_link_targets(mock_head, link_verifier):
    mock_head.return_value.status_code = 200
    link_status, final_urls, unreachable_links = link_verifier.verify_link_targets()
    assert link_status["https://example.com"] == 'valid', "Link should be marked as valid"

def test_verify_link_targets_invalid(link_verifier):
    link_status, final_urls, unreachable_links = link_verifier.verify_link_targets()
    print(f"LINKSTATUS***{link_status}")
    assert link_status["https://www.starbucks.com/madeup"] == 'invalid', "Link should be marked as invalid"

def test_verify_link_targets_unreachable(link_verifier):
    link_status, final_urls, unreachable_links = link_verifier.verify_link_targets()
    assert link_status["https://invalid-link.com"] == 'unreachable', "Link should be marked as unreachable"


