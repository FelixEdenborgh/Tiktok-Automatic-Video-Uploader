# Steg 1: Öppna cmd och skriv in cd C:\Program Files (x86)\Google\Chrome\Application
# Steg 2: skriv in detta: chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Selenium\Chrome_Test_Profile
# Steg 3: gå till tiktok.com och logga in


# Setup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)

print(driver.title)

time.sleep(3)
driver.get("https://www.tiktok.com/upload?lang=sv-SE")

def getFirstFile():
    # Set the path to the folder you want to get the first item from
    folder_path = "" # <-- your folder where the videos are in.

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Get the first file in the folder
    first_file = files[0]

    # Get the name of the first file
    first_file_name = os.path.basename(first_file)

    first_file_path = os.path.join(folder_path, first_file)

    print("First file in folder:", first_file)
    print("Name of first file:", first_file_name)
    return first_file_path


def deleteTheFile(nameOfFileAndPath):
    # delete the film from folder
    time.sleep(2)
    print("Deleting the movie from folder")
    os.remove(nameOfFileAndPath)


uploads = 0
while(True):
    time.sleep(20)
    uploads = uploads + 1
    video_path = getFirstFile()

    print("New upload started")
    driver.get("https://www.tiktok.com/upload?lang=sv-SE")

    while(True):
        try:
            # uploading video
            # Assuming you have already logged in to TikTok using Selenium and have navigated to the upload page
            time.sleep(5)

            # There is an iframe on the page...
            iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
            driver.switch_to.frame(iframe)

            # Wait until page loads...
            time.sleep(3)

            # Select the input file and send the filename...
            upload = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            upload.send_keys(video_path)
        except:
            print("Cant upload a new video")


        try:
            time.sleep(5)
            PictureText = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div')
            PictureText.clear()
            time.sleep(5)
            PictureText.send_keys("Motivational Speech, Check link in discription")
            time.sleep(5)
            PictureText.send_keys("#motivation" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#inspiration" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#mindset" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#selfimprovement" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#growthmindset" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#positivity" + Keys.ENTER)
            time.sleep(5)
            PictureText.send_keys("#determination" + Keys.ENTER)
        except:
            print("Cant change name on the video")


        try:
            time.sleep(5)
            PublishButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[7]/div[2]/button')
            PublishButton.click()

            time.sleep(15)
            deleteTheFile(video_path)
        except:
            print("Cant find PublishButton")
            break

        print(f"Their have been so far {uploads} uploads")
        time.sleep(15)

        try:
            time.sleep(5)
            UploadnewVideoButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div/div[2]/div[1]')
            UploadnewVideoButton.click()
            break
        except:
            print("Cant click on adding new video")
            break









