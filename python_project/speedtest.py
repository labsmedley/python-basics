import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Open the browser (Chrome)
driver = webdriver.Chrome()

try:
    # 2. Navigate to Fast.com (The test starts running AUTOMATICALLY immediately)
    print("Opening fast.com...")
    driver.get("https://fast.com/")

    print("Speed test started automatically. Waiting for results...")
    
    # 3. Wait until the test finishes and the final results counter appears
    # Fast.com displays the class "succeeded" once the final speed calculation is locked in.
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#speed-value.succeeded"))
    )
    
    # Extract the final speed text from the page
    final_speed = driver.find_element(By.ID, "speed-value").text
    speed_unit = driver.find_element(By.ID, "speed-units").text
    
    print(f"\n⚡ Speed Test Complete: {final_speed} {speed_unit} ⚡\n")
    
    # Hold the screen open for a few extra seconds so you can see it
    time.sleep(5)

finally:
    # 4. Close the browser completely
    print("Closing browser.")
    driver.quit()