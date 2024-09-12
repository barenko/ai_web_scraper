import subprocess
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup


def scrape_website(url):
    print("Launching BrowserDriver...")

    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(url)
        print("Page loaded successfully.")
        html = driver.page_source
        return html
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        print("BrowserDriver closed.")


def extract_body_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if body:
        return str(body)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
