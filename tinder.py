from selenium import webdriver
from time import sleep
import random
import pyautogui

#CHANGE 2
class tinder_bot:
    def __init__(self):
        path = r"C:\Users\Admin\Desktop\chromedriver.exe"
        self.driver = webdriver.Chrome(path)
    def login(self):
        self.driver.get("https://tinder.com/")
        print('getting to tinder...')
        sleep(2)

        log_in = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        log_in.click()
        print('pressing logging in...')
        sleep(1)

        by_facebook = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        print("pressing by facebook...")
        by_facebook.click()
        sleep(1)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        print('switching window...')

        email = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div/div[1]/div/input')
        email.send_keys('kuba1302@gmail.com')
        print('entering email...')
        sleep(1)

        password = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div/div[2]/div/input')
        password.send_keys('Kacperwujec2706')
        print('entering password')
        sleep(1)

        log_in_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div/div[3]/label[2]')
        log_in_btn.click()
        print('loggining in...')
        self.driver.switch_to_window(base_window)
        sleep(4)
        print('closing pop up')
        location_pop = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        location_pop.click()
        sleep(0.5)

        pop2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        pop2.click()

        pop3 = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        pop3.click()
        print('You are logged in.')

    def swipe_right(self):
        button_right = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button")
        button_right.click()
    def swipe_left(self):
        button_left = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        button_left.click()
    def new_tab(self):
        self.driver.execute_script("window.open('https://www.cleverbot.com');")
        sleep(2)
        self.driver.find_element_by_name('understood, and agreed').click()
    def swipe_left(self):
        button_left = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        button_left.click()

    def swiping(self):
        i = 1
        c = 0
        b = 0
        a = int(input("how many times should i swipe?"))
        while a > i :
            if random.randrange(1,6) == 1:
                try:
                    self.swipe_left()
                    c += 1
                    print(str(c) + "th left swipe")
                    sleep(random.uniform(1, 2))
                except:
                    try:
                        #ta o matchu
                        pop_up = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/button')
                        pop_up.click()
                        print('Match!')
                        sleep(1)
                    except:
                        try:
                            #ta o superlike
                            pop_up1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
                            pop_up1.click()
                            #ta o pulpicie
                            pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
                            pop_up2.click()
                        except:
                            try:
                                # ta o pulpicie
                                pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
                                pop_up2.click()
                            except:
                                pass
                sleep(0.5)
            else:
                try:
                    self.swipe_right()
                    sleep(random.uniform(1,2))
                    b += 1
                    print(str(b) + "th right swipe")
                except:
                    try:
                        pop_up = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/button')
                        pop_up.click()
                        print('Match!')
                        sleep(1)
                    except:
                        try:
                            #ta o superlike
                            pop_up1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[2]')
                            pop_up1.click()
                            pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
                            pop_up2.click()
                        except:
                            try:
                                # ta o pulpicie
                                pop_up2 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
                                pop_up2.click()
                            except:
                                pass
                sleep(0.5)
            i += 1



    def get_msg(self):
        msg = self.driver.find_elements_by_class_name("text")
        a = msg[0].text

    def menu(self):
        def options():
            print('What do you want to do?')
            print('Press 0 to swipe.')
            print('Press 1 to quit.')
            print('Press 2 to get_msg')
            global option
            option = input('Enter your choice:\n')
        while option != 0:
            if option == 1:
                bot.swiping()
                options()
            else:
                options()
                pass

if __name__ == "__main__":
    bot = tinder_bot()
    option = 1
    bot.login()
    bot.menu()
