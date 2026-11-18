from app.core import authorized,redact
def test_policy():
    assert authorized('reader','search') and not authorized('reader','health')
def test_redaction():
    assert '[REDACTED_EMAIL]' in redact('a@b.com')
