from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification
import time

def get_covid_data(state):
    url = "https://www.mohfw.gov.in/"
    driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe')  # Use the appropriate WebDriver for your browser

    driver.get(url)
    time.sleep(5)  # Give the page some time to load

    # Find the table row for the given state
    total_cases = active_cases = recovered = deaths = "Data not available"
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        
        if len(columns) > 1 and state.lower() in columns[1].text.lower():
            total_cases = columns[2].text
            # print(total_cases)
            active_cases = columns[3].text
            recovered = columns[4].text
            deaths = columns[5].text
            break

    driver.quit()
    return total_cases, active_cases, recovered, deaths

def send_notification(state, total_cases, active_cases, recovered, deaths):
    title = f"COVID-19 Stats for {state}"
    message = (
        f"Total cases: {total_cases}\n"
        f"Active cases: {active_cases}\n"
        f"Recovered: {recovered}\n"
        f"Deaths: {deaths}"
    )
    notification.notify(
        title=title,
        message=message,
        app_icon = r"C:\Users\rinku\Desktop\My_code\projects\Realtime-Covid-19-noti-system\favicon.ico",
        timeout=10  # Notification timeout in seconds
    )

if __name__ == "__main__":
    state_name = "Rajasthan"  # Replace with the state you're interested in
    total, active, recovered, deaths = get_covid_data(state_name)
    send_notification(state_name, total, active, recovered, deaths)
