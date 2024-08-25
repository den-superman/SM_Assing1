import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(ChromeDriverManager().install())

def hover_over_profile(browser, index):
    avatar = browser.find_element(By.XPATH, f"(//img[@alt='User Avatar'])[{index}]")
    
    actions = ActionChains(browser)
    actions.move_to_element(avatar).perform()
    browser.save_screenshot(f"profile_hover_{index}.png")
    profile_link = browser.find_element(By.XPATH, f"(//a[contains(text(),'View profile')])[{index}]")
    assert profile_link
    user_name = browser.find_element(By.XPATH, f"//h5[normalize-space()='name: user{index}']")
    assert user_name
        
    profile_link = browser.find_element(By.XPATH, f"(//a[contains(text(),'View profile')])[{index}]")
    user_name = browser.find_element(By.XPATH, f"//h5[normalize-space()='name: user{index}']")
    return [profile_link, user_name]
    
def move_away(browser):
    blank_area = browser.find_element(By.XPATH, "(//div[@id='flash-messages'])[1]")
    actions = ActionChains(browser)
    actions.move_to_element(blank_area).perform()

class HoverTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("https://the-internet.herokuapp.com/hovers")

    def test_correct_page_loaded(self):
        browser = self.browser
        browser.save_screenshot("test_screenshot.png")
        self.assertEqual("https://the-internet.herokuapp.com/hovers", browser.current_url)
        assert len(browser.find_elements(By.CSS_SELECTOR, ".figure")) == 3

    def test_hover_displays_information(self):
        browser = self.browser
        time.sleep(2)
        for i in range(1, 4):
            profile_elements = hover_over_profile(browser, i)
            self.assertIsNotNone(profile_elements[0])
            self.assertIsNotNone(profile_elements[1])

    def test_view_profile_link_navigation(self):
        browser = self.browser
        time.sleep(2)
        total_profiles = len(browser.find_elements(By.CSS_SELECTOR, ".figure"))
        for i in range(1, total_profiles):
            self.browser.get("https://the-internet.herokuapp.com/hovers")
            time.sleep(1)
            profile_elements = hover_over_profile(browser, i)
            profile_elements[0].click()
            time.sleep(1)
            browser.save_screenshot("profile_click_screenshot.png")
            self.assertNotEqual("https://the-internet.herokuapp.com/hovers", browser.current_url)
            self.assertEqual(f"https://the-internet.herokuapp.com/users/{i}", browser.current_url)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
