# defollowing people on twitter using selenium
from selenium import webdriver
import time, math, logging
from config import username, password

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "application.log",
							level = logging.INFO,
								format = LOG_FORMAT)
logger = logging.getLogger()


def wait(implicit_wait, program_wait):
	""" designed to implement appropriate waiting behaviour """
	driver.implicitly_wait(implicit_wait)
	time.sleep(program_wait)

def log(msg):
	logger.info(msg)


def login_twitter(username, password):
	""" log into twitter account by opening to login page,
	filling in fields and clicking submit button """
	driver = webdriver.Firefox()
	global driver
	driver.get("https://twitter.com/login")

	username_field = driver.find_element_by_class_name("js-username-field")
	password_field = driver.find_element_by_class_name("js-password-field")
	
	username_field.send_keys(username)
	wait(2,2)
	password_field.send_keys(password)
	wait(2,2)

	driver.find_element_by_class_name("EdgeButtom--medium").click()
	wait(2,4)


def compute_no_of_batches(target_amount):
	""" compute no of times programme needs to reload the 
	following page and do defollowing (batch) """
	no_of_batches = float(target_amount) / 18
	no_of_batches = math.ceil(no_of_batches)
	no_of_batches = int(no_of_batches)
	return no_of_batches


def defollow(target_amount):
	""" defollow a target amount of people by going to page of followers
	and repeatedly clicking de-follow buttons """
	no_of_batches = compute_no_of_batches(target_amount)

	driver.get("https://twitter.com/following")
	wait(2,4)

	for each in range(no_of_batches):
		defollow_buttons = driver.find_elements_by_class_name("following-text")
		wait(10,4)

		for defollow_button in defollow_buttons:
			try:
				defollow_button.click()
				wait(4,2)
			except:
				print "unable to defollow."

		log("3. Defollowed 1 round of followers")
		driver.refresh()
		wait(10,4)


if __name__ == "__main__":
	log("1. Programme started")
	login_twitter(username, password)
	log("2. Logged into Twitter")
	defollow(40)
	wait(2,4)
	driver.quit()
	log("4. Programme finished \n")

