from selenium.webdriver.common.by import By


class AdminPageLocators:
    POSTS_BUTTON = (By.XPATH, "//*[@href='/admin/app/post/']")
    GROUPS_BUTTON = (By.XPATH, "//*[@href='/admin/auth/group/']")
    USERS_BUTTON = (By.XPATH, "//*[@href='/admin/auth/user/']")
    TEXT_ADD_GROUP_1 = (By.XPATH, "//*[@id='result_list']/tbody/tr/th/a")
    NAME_GROUP_FIELD = (By.XPATH, "//*[@id='id_name']")
    SAVE_BUTTON = (By.XPATH, "//*[@value='Save']")
