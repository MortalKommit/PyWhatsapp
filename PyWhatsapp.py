import schedule
import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from tkinter import filedialog
from tkinter import Tk

try:
    import autoit
except ModuleNotFoundError:
    pass
import time
import os

whatsapp_url = "https://web.whatsapp.com/"


class Message:
    def __init__(self, message=None, attachment_list=None, file_list=None):
        self.message = message
        self.attachment_list = attachment_list
        self.file_list = file_list


def is_numeric(literal):
    """Return whether a literal can be parsed as a numeric value, allows signage +/-"""
    castings = [int, float, complex,
                lambda s: int(s, 2),  # binary
                lambda s: int(s, 8),  # octal
                lambda s: int(s, 16)]  # hex
    for cast in castings:
        try:
            cast(literal)
            return True
        except ValueError:
            pass
    return False


def whatsapp_login(url):
    chrome_options = Options()
    chrome_options.add_argument('--user-data-dir=./User_Data')
    browser_instance = webdriver.Chrome(options=chrome_options)
    browser_instance.get(url)
    browser_instance.maximize_window()
    print("QR scanned")
    return browser_instance


def send_message(target, message_content, web_browser):
    wait = WebDriverWait(web_browser, 600)
    try:
        x_arg = '//span[contains(@title,' + target + ')]'
        ct = 0
        while ct != 10:
            try:
                group_title = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()
                break
            except:
                ct += 1
                time.sleep(3)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message_content.message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT). \
                    key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")
        time.sleep(1)
        if message_content.attachment_list:
            clip_button = web_browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
            clip_button.click()
            time.sleep(1)
            # To send Videos and Images.
            media_button = web_browser.find_element_by_xpath(
                '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
            media_button.click()
            time.sleep(3)

            autoit.control_focus("Open", "Edit1")
            attachments = " ".join(map(lambda x: '"' + x + '"', message_content.attachment_list))
            autoit.control_set_text("Open", "Edit1", attachments)
            autoit.control_click("Open", "Button1")
            time.sleep(3)
            whatsapp_send_button = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
            whatsapp_send_button.click()

    except NoSuchElementException:
        return


def send_unsaved_contact_message(message_content, web_browser, link):
    web_browser.get(link)
    time.sleep(1)
    web_browser.find_element_by_xpath('//*[@id="action-button"]').click()
    time.sleep(2)
    web_browser.find_element_by_xpath('//*[@id="content"]/div/div/div/a').click()
    time.sleep(4)

    try:
        time.sleep(7)
        input_box = web_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message_content.message:
            if ch == "\n":
                ActionChains(web_browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).\
                    key_up(Keys.SHIFT). key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfully")

    except NoSuchElementException:
        print("Failed to send message")
        return

    time.sleep(7)

# Function to send Documents(PDF, Word file, PPT, etc.)


def send_files(web_browser, file_list):
    # Attachment Drop Down Menu
    clip_button = web_browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
    clip_button.click()
    time.sleep(1)

    # To send a Document(PDF, Word file, PPT)
    doc_button = web_browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/'
                                                   'button')
    doc_button.click()
    time.sleep(1)

    doc_path = os.getcwd() + "\\Documents\\" + file_list

    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", doc_path)
    autoit.control_click("Open", "Button1")

    time.sleep(3)
    whatsapp_send_button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/'
                                                         'div/div[2]/span[2]/div/div/span')
    whatsapp_send_button.click()


def sender(contact_list, unsaved_contact_list, sender_message, web_browser):
    for i in contact_list:
        send_message(i, sender_message, web_browser)
        print("Sending message to... ", i)
    time.sleep(5)

    if len(unsaved_contact_list) > 0:
        for i in unsaved_contact_list:
            link = "https://wa.me/" + i
            print("Sending message to.... ", i)
            send_unsaved_contact_message(sender_message, web_browser, link)


# To schedule your msgs
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Append more contact_list as input to send messages
# input_contacts()

messageparser = argparse.ArgumentParser(description='Automated Whatsapp Messaging', epilog='''Usage :python 
                                                                            PyWhatsapp.py "Jay" --msg "Hey"''')
messageparser.add_argument('contacts', metavar='contacts', nargs='+',
                           help='''A list of contacts (names or numbers, max:10, country code required as +XX)
                                without the +''')
messageparser.add_argument('--msg', metavar='message', help='''The message to be sent to a list of 
                                                                       contacts or groups. Use \n for newline''',
                           required=True)
messageparser.add_argument('--schd', metavar='schedule', nargs='?', help='''Whether the message should be sent on a 
                            schedule or once, DEFAULT:once FORMAT:DD-MM-YYYYTHH:MM:SS''')
messageparser.add_argument('--attach', action='store_true', help='Whether to include attachments'
                                                                 '(image/video)')
messageparser.add_argument('--doc', action='store_true', help='Whether to include documents')

args = messageparser.parse_args()
contact = ['"{0}"'.format(element) for element in args.contacts if not is_numeric(element)]
unsaved_contacts = [element for element in args.contacts if is_numeric(element)]
args.msg = args.msg.replace("\\n", '\n')

Tk().withdraw()
if args.attach:
    names = filedialog.askopenfilenames(title='Send Whatsapp Attachment(s)', filetypes=[("All files", "*.*")],
                                        initialdir=os.path.expanduser('~'), multiple=True)
else:
    names = None
if args.doc:
    doc_names = filedialog.askopenfilenames(title='Send Whatsapp Document(s)', filetypes=[("All files", "*.*")],
                                            initialdir=os.path.expanduser('~'), multiple=True)
else:
    doc_names = None
names = [os.path.abspath(name) for name in names]
message_object = Message(args.msg, names, doc_names)
print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
browser = whatsapp_login(whatsapp_url)
sender(contact, unsaved_contacts, message_object, browser)
# First time message sending Task Complete
print("Task Completed")

#browser.quit()
