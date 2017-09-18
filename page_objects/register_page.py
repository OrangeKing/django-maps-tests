'''
Module representing registration page.
All user input is validated on the app-side.
'''

from page_objects.locators.register_page_locators import RegisterPageLocators
from page_objects.base_page import BasePage
from page_objects.elements.elements import BasePageElement


class RegisterPage(BasePage):
    '''
    Class contining methods for actions within register page.
    All user signing up methods should go here.
    '''

    def __init__(self, driver):
        super(RegisterPage, self).__init__(driver)

    def fill_fields(self, username, password, email):
        '''
        Fills registration forms with given user credentials.

        :param username: string value of registered user username to be put into
                         login form.

        :param password: string value of registered user password to be put into
                         login form.

        :param email: string value of registered user password to be put into
                         login form.
        '''

        if username != " ":
            BasePageElement(self.driver).input_text(
                RegisterPageLocators.USER_NAME, username)
        if password != " ":
            BasePageElement(self.driver).input_text(
                RegisterPageLocators.PASSWORD, password)
        if email != " ":
            BasePageElement(self).input_text(RegisterPageLocators.EMAIL, email)

    def press_submit(self):
        '''
        Clicks at the "submit" button to confirm register process with given
        credentials and sign up.
        '''

        BasePageElement(self.driver).click_element_and_wait(
            RegisterPageLocators.SUBMIT_BUTTON)

    def stop_music(self):
        '''
        Stops the music video.
        '''

        BasePageElement(self.driver).click_element_and_wait(
            RegisterPageLocators.MUSIC_BUTTON)
        BasePageElement(self.driver).click_element_and_wait(
            RegisterPageLocators.STOP_MUSIC_BUTTON)
        BasePageElement(self.driver).click_element_and_wait(
            RegisterPageLocators.HIDE_MUSIC_POPUP)

    # delete after making home_page
    def open_register(self):
        BasePageElement(self.driver).click_element_and_wait(
            RegisterPageLocators.REGISTER)
    # TODO - prepare postgress queries
    """
    def verify_user_registration(self, username):
        '''
        Verify whether user was properly registered by looking up user database
        endpoint at its url address.

        :param username: string object used for assertion with list of registered
                         users.

        :return: boolean value.
        '''
        sleep(10)
        users = urllib.urlopen(RegisterPageLocators.USERS_PAGE).read()
        match = re.findall(RegisterPageLocators.USER_PATTERN, users)
        return username in match
    """

    """
    def check_usr_in_db(self, username):
        '''
        Verify whether user was properly registered by looking up user database
        endpoint with requests and bs parse.

        :param username: string object used for assertion with list of registered
                         users.

        :return: boolean value.
        '''

        try:
            get_db = requests.get(RegisterPageLocators.USERS_PAGE)
            if get_db.status_code == 200:
                soup = BeautifulSoup(get_db.text, "html.parser")
                # using " " as empty password
                if username == " ":
                    check_usr_name = soup.find(text=username)
                    if check_usr_name == "<br/>":
                        return True
                    else:
                        return False
                else:
                    check_usr_name = soup.find(text=username)
                    if check_usr_name:
                        return True
                    else:
                        return False
            else:
                self.check_usr_in_db(username)
        except requests.exceptions.RequestException as ex:
            print(ex)
            print("Could not get data from db. Aborting ...")
    """
