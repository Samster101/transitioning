import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver (replace with your actual path)
chromedriver_path = "/Users/abdussami/Desktop/chaya/chromedriver"
# Set up the WebDriver service
service = Service(chromedriver_path)
# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

store_names = ['PALM BERRIES','PALM BERRIES', 'PALM BERRIES BOONE','PALM BERRIES CONCORD',
               'PALM BERRIES CORNELIUS','PALM BERRIES HICKORY','PALM BERRIES LINCOLNTON',
               'PALM BERRIES MOORESVILLE', 'PALM BERRIES RALEIGH','PALM BERRIES ARLINGTON']

Sysco_css = {'css_sign-in':"a.sign-in-link[aria-label='Navigate to Sign In']" , 'email_css':"input[type='email']","next_button_login":"button[data-id='btn_next']",
             'login pass': "input[type='password']", "address_select":"div[data-id='topPanel-dropdown-button-globalCustomerSelection']",
             "x_path_stores" : f"//h5[text()='{store_names}']", 'click_shopping_in':"div[data-id='add_case_to_cart_button']",
             'input_shopping': "input[data-id='add_case_to_cart_input']", 'total_cart':"div.cart-total-label > span[data-id='span_cart_button_total_price']",
               }
errors_css = {'intial_login_error':"button.btn.marketing-modal-close-btn.btn-xxl.icon-only[aria-label='close icon']",
              }
try:
    driver.get("https://www.sysco.com")


    sign_in_element = driver.find_element(By.CSS_SELECTOR, "a.sign-in-link[aria-label='Navigate to Sign In']")
    sign_in_element.click()

    print("Clicked on the 'Sign In' button!")

    # Wait for the sign-in page to load
    driver.implicitly_wait(10)

    # Locate the email input field and enter the email address
    email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_input.send_keys("bowldberries@gmail.com")
    print("Entered the email address!")

    # Pause for 1 second before clicking the "Next" button
    time.sleep(1)

    # Locate the "Next" button and click it
    next_button = driver.find_element(By.CSS_SELECTOR, "button[data-id='btn_next']")
    next_button.click()

    # Wait for the next page to load
    driver.implicitly_wait(10)

    # Locate the password input field and enter the password
    password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_input.send_keys("PaBe5432!")
    print("Entered the password!")

    # Submit the form
    password_input.send_keys(Keys.RETURN)
    print("Submitted the form!")

    # Pause for 3 seconds to allow for popup to potentially appear
    time.sleep(3)

    # Check for the popup's close button and click it if it exists
    try:
        popup_close_button = driver.find_element(By.CSS_SELECTOR, "button.btn.marketing-modal-close-btn.btn-xxl.icon-only[aria-label='close icon']")
        popup_close_button.click()
        print("Popup detected and closed.")
    except selenium.common.exceptions.NoSuchElementException:
        print("No popup appeared.")

    # Click the customer selection flyout element
    customer_selection_element = driver.find_element(
        By.CSS_SELECTOR, 
        "div[data-id='topPanel-dropdown-button-globalCustomerSelection']"
    )
    customer_selection_element.click()
    print("Clicked on the customer selection element!")

    # Pause briefly to ensure the flyout is fully loaded
    time.sleep(2)

    # Click the specific address element "2931 S GLEBE RD"
    address = "112 S NC 16 BUSINESS HWY"
    customer_address_element= driver.find_element(By.XPATH, "//h5[text()='PALM BERRIES CONCORD']")
    customer_address_element.click()
    print("Clicked on the address: 2931 S GLEBE RD")

    # Wait for 2 seconds after clicking the last button
    time.sleep(2)

    # Try to close the popup if it appears
    try:
        popup_close_button = driver.find_element(By.CSS_SELECTOR, "button.btn.marketing-modal-close-btn.btn-xxl.icon-only[aria-label='close icon']")
        popup_close_button.click()
        print("Popup detected and closed after address selection.")
    except selenium.common.exceptions.NoSuchElementException:
        print("No popup appeared after address selection.")

    # Open the specific product URL
    driver.get("https://shop.sysco.com/app/product-details/opco/012/product/7078370?seller_id=USBL")
    print("Navigated to the product details page.")

    # Wait for the product details page to load
    driver.implicitly_wait(2)

    # Locate the "Add to Cart" button
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "div[data-id='add_case_to_cart_button']")
    add_to_cart_button.click()


    # Wait for the quantity input field to become active
    time.sleep(1)

    # Locate the quantity input field and enter a number
    quantity_input = driver.find_element(By.CSS_SELECTOR, "input[data-id='add_case_to_cart_input']")
    quantity_input.clear()  # Clear any pre-filled value
    #driver.implicitly_wait(1)
    quantity_input.send_keys('3')
    
# Send the ENTER key after entering the quantity
    quantity_input.send_keys(Keys.RETURN)
    print("Sent ENTER key to confirm the quantity.")

# Wait for the cart total element to become visible
    time.sleep(2)

# Locate and click the cart total element
    cart_total_element = driver.find_element(By.CSS_SELECTOR, "div.cart-total-label > span[data-id='span_cart_button_total_price']")
    cart_total_element.click()
    print("Clicked on the cart total element.")
    time.sleep(1)
    cart_total_element = driver.find_element(By.CSS_SELECTOR, "div.cart-total-label > span[data-id='span_cart_button_total_price']")
    cart_total_element.click()
    print("Clicked on the cart total element.")
    

    

    #quantity_input.send_keys()
   # print("Entered quantity into the input field.")

finally:
    # Close the browser after use
    input("Press Enter to close the browser...")
    driver.quit()
