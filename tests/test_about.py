from pages.main_page_2 import MainPage

def test_navigate_about(page) -> None:
    main = MainPage(page)
    main.open()
    page.wait_for_load_state("networkidle")
    assert main.about_link.is_visible()
    main.click_about()
    page.wait_for_load_state("networkidle")
    assert "about" in page.url  # или ожидаемый фрагмент URL


