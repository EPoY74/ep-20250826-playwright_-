from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        # Локаторы основных блоков/ссылок
        self.about_link    = page.get_by_text("О нас")
        self.services_link = page.get_by_text("Услуги")
        self.cases_link    = page.get_by_text("Кейсы")
        self.reviews_link  = page.get_by_text("Отзывы")
        self.contact_link  = page.get_by_text("Контакты")

    def open(self):
        # Открываем главную страницу
        self.page.goto("http://effective-mobile.ru/")
    
    def go_to_about(self):
        self.about_link.click()
    
    def go_to_services(self):
        self.services_link.click()
    
    def go_to_cases(self):
        self.cases_link.click()
    
    def go_to_reviews(self):
        self.reviews_link.click()
    
    def go_to_contacts(self):
        self.contact_link.click()
