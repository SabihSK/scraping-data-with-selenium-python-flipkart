# import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger_config import setup_logger

# Set up the logger
log = setup_logger("app_logs")


# Your main application code

# DataFrme
df = pd.DataFrame(
    columns=[
        "product image url",
        "product name",
        "product discription",
        "product price",
        "product discount price",
        "product per off",
    ]
)


def print_function(
    product_image_url,
    product_name,
    product_discription,
    product_price,
    product_discount_price,
    product_per_off,
):
    # ------------------- print product data -------------------#
    global df
    new_row = pd.DataFrame(
        [
            {
                "product image url": product_image_url,
                "product name": product_name,
                "product discription": product_discription,
                "product price": product_price,
                "product discount price": product_discount_price,
                "product per off": product_per_off,
            }
        ]
    )
    df = pd.concat([df, new_row], ignore_index=True)

    log.debug("///------------------------ Start ----------------------------///")
    log.info(
        f"Product image url= {product_image_url}",
    )
    log.info(
        f"Product name= {product_name}",
    )
    log.info(
        f"Product discription= {product_discription}",
    )
    log.info(
        f"Product price= {product_price}",
    )
    log.info(
        f"Product dicount Price= {product_discount_price}",
    )
    log.info(
        f"Product % off= {product_per_off}",
    )
    log.debug("///------------------------- End -----------------------------///")


def product_loop_functions(driver):
    for j in range(2, 12):
        for i in range(1, 5):
            # Product image url
            try:
                product_image_url = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/a/div[1]/div/div/img",
                ).text
            except NoSuchElementException:
                product_image_url = ""

            # Product name
            try:
                product_name = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/div/a[1]",
                ).text
            except NoSuchElementException:
                product_name = ""

            # Product discription
            try:
                product_discription = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/div/div[1]",
                ).text
            except NoSuchElementException:
                product_discription = ""

            # Product price
            try:
                product_price = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/div/a[2]/div/div[1]",
                ).text
            except NoSuchElementException:
                product_price = ""

            # Product discount price
            try:
                product_discount_price = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/div/a[2]/div/div[2]",
                ).text
            except NoSuchElementException:
                product_discount_price = ""

            # Product % off
            try:
                product_per_off = driver.find_element(
                    By.XPATH,
                    f"/html/body/div[1]/div/div[3]/div/div[2]/div[{j}]/div/div[{i}]/div/div/a[2]/div/div[3]/span",
                ).text
            except NoSuchElementException:
                product_per_off = ""

            print_function(
                product_image_url,
                product_name,
                product_discription,
                product_price,
                product_discount_price,
                product_per_off,
            )


def page_loop_function(driver):
    for i in range(1, 8):
        # Base URL
        driver.get(
            f"https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy%2Cbuh&marketplace=FLIPKART&p%5B%5D=facets.brand%255B%255D%3DNoise&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&param=464245&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTEsMDk5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiTm9pc2UgU21hcnR3YXRjaGVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiU01XR1JaUEtKRVdZRVdHVSIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D&page={i}"
        )
        product_loop_functions(driver)


def main():

    # Web Driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    driver.maximize_window()

    page_loop_function(driver)

    driver.close()

    log.debug("///------------------------- DataFrame -------------------------///")
    log.info(df)
    df.to_csv("flipkart_data.csv", encoding="utf-8", index=False)


if __name__ == "__main__":
    main()
