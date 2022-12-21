from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, test_name):

    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # context.driver = webdriver.Chrome\
    #     (executable_path='C:/Users/Vitaliy/careerist/internship/CureSkin-Automation-project/chromedriver.exe')
    # context.driver = webdriver.Firefox\
    #     (executable_path='C:\\Users\\Vitaliy\\careerist\\internship\\CureSkin-Automation-project\\geckodriver.exe')
    # context.driver = webdriver.Edge\
    #     (executable_path='C:/Users/Vitaliy/careerist/internship/CureSkin-Automation-project/msedgedriver.exe')
    # # context.driver = webdriver.Safari()

    ## HEADLESS MODE CHROME ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     executable_path='C:/Users/Vitaliy/careerist/internship/CureSkin-Automation-project/chromedriver.exe')

    ## HEADLESS MODE FIREFOX ##
    # options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    # context.driver = webdriver.Firefox(
    #     firefox_options=options,
    #     executable_path='C:\Users\Vitaliy\careerist\internship\CureSkin-Automation-project\geckodriver.exe')


    ### EventFiringWebDriver - log file ##
    ## for drivers ##
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(executable_path=
    #                      'C:/Users/Vitaliy/careerist/internship/CureSkin-Automation-project/chromedriver.exe')
    #     MyListener())

    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack ###
    desired_cap = {
        'browser': 'Chrome',
        'os_version': '11',
        'os': 'Windows',
        'name': test_name
    }
    bs_user = 'vitaliystyranko_obQCqn'
    bs_key = 'Ta5ZAXTCQR4PBxAFAHy7'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
