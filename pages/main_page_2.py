# pages/main_page.py
from playwright.sync_api import Page, Locator

class MainPage:
    def __init__(self, page: Page):
        self.page: Page = page
        # навигация в шапке
        self.about_link:    Locator = page.get_by_role("link", name="О нас")
        self.services_link: Locator = page.get_by_role("link", name="Услуги")
        self.cases_link:    Locator = page.get_by_role("link", name="Кейсы")
        self.reviews_link:  Locator = page.get_by_role("link", name="Отзывы")
        self.contacts_link: Locator = page.get_by_role("link", name="Контакты")

        # ориентиры в секциях (заголовки/якоря после скролла)
        self.about_header:    Locator = page.get_by_text("Наша цель")
        self.services_header: Locator = page.get_by_text("Разработка   мобильных приложений")
        self.reviews_header:  Locator = page.get_by_text("ОТЗЫВЫ КЛИЕНТОВ")
        self.contacts_footer: Locator = page.get_by_text("mailer@effective-mobile.ru")  # в подвале есть этот email

    def open(self) -> None:
        self.page.goto("https://effective-mobile.ru/")

    # действия
    def click_about(self) -> None:
        self.about_link.click()

    def go_to_services(self) -> None:
        self.services_link.click()

    def go_to_cases(self) -> None:
        self.cases_link.click()

    def go_to_reviews(self) -> None:
        self.reviews_link.click()

    def go_to_contacts(self) -> None:
        self.contacts_link.click()
