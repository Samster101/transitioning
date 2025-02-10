import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from modular import *
from selenium.webdriver.common.action_chains import ActionChains
import time

Options=Options()
Options.set_capability('acceptInsecureCerts', True)

chromedriver_path = "/Users/abdussami/Desktop/chaya/chromedriver"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=Options)

store_names = ['PALM BERRIES','PALM BERRIES', 'PALM BERRIES BOONE','PALM BERRIES CONCORD',
               'PALM BERRIES CORNELIUS','PALM BERRIES HICKORY','PALM BERRIES LINCOLNTON',
               'PALM BERRIES MOORESVILLE', 'PALM BERRIES RALEIGH','PALM BERRIES ARLINGTON']

Sysco_css = {'css_sign-in':"a.sign-in-link[aria-label='Navigate to Sign In']" , 'email_css':"input[type='email']","next_button_login":"button[data-id='btn_next']",
             'login pass': "input[type='password']", "address_select":"div[data-id='topPanel-dropdown-button-globalCustomerSelection']",
             'click_shopping_in':"div[data-id='add_case_to_cart_button']",
             'input_shopping': "input[data-id='add_case_to_cart_input']", 'total_cart':"div.cart-total-label > span[data-id='span_cart_button_total_price']"
             }
#arbitrary N**
x_path_stores = {store_names[n] : f"//h5[text()='{store_names[n]}']" for n in range(len(store_names))}
errors_ = ["button.btn.marketing-modal-close-btn.btn-xxl.icon-only[aria-label='close icon']"]

website_url = "https://shop.sysco.com/auth/login"
     
driver.get(website_url)
ddv=driver
action = ActionChains(driver)

sysco_pass = "PaBe5432!"
sysco_email = "bowldberries@gmail.com"

method_css = By.CSS_SELECTOR
method_xp = By.XPATH
time_wait= [3,9,10,10]
def main():
    #general_css_click(ddv,Sysco_css,'css_sign-in',1,errors_)
    general_css_sk(method_css,ddv,Sysco_css,'email_css', sysco_email,time_wait[0],errors_)
    general_css_click(method_css,ddv,Sysco_css,'next_button_login',time_wait[1],errors_)
    general_css_sk(method_css,ddv,Sysco_css,'login pass', sysco_pass,time_wait[2],errors_)
    general_css_click(method_css,ddv,Sysco_css,'address_select',time_wait[3],errors_)

    ## select store ##
    trivial = False
    scrollable_element = driver.find_element(By.ID,"searched_accounts_container")
    ActionChains(driver).move_to_element(scrollable_element).perform()
    while trivial == False:
        try:
            general_css_click(method_xp,ddv,x_path_stores,store_names[6],1,errors_)
            trivial = True
        except:
            time.sleep(1)
            for n in range(3):
                scrollable_element.send_keys(Keys.ARROW_DOWN)
        
        
    input("Press Enter to close the browser...")
    driver.quit()

main()