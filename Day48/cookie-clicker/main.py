from selenium import webdriver
import time

cookie_monster_is_chomping = True

chrome_driver_path = "/Users/charlesnolan/python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

target_url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(target_url)

big_cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 20
five_min = time.time() + 60*5

while cookie_monster_is_chomping:
    big_cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        cookie_count = int(driver.find_element_by_id("money").text.strip().replace(",",""))

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 20
        pass

    if time.time() > five_min:
        print("Game Over")
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        cookie_monster_is_chomping = False
        break

driver.quit()

