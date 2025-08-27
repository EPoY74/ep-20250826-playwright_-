def test_example(page) -> None:
    
    page.goto("http://example.com")
    assert page.title() == "Example Domain"
