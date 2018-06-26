# Automatically deletes Hushmail's User-defined emails from the Inbox

import unittest
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
usr = ''
pss = ''


## true_login_page_until_the_credentials_are_filled
driver = webdriver.Chrome("C:/Users/home/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options) # open_chrome_driver_with_options
driver.get("https://www.hushmail.com/") # the_url
time.sleep(5)
driver.find_element_by_xpath("//*[@id='navbar']/ul[2]/li[4]/a").click(); # clicks_sign_in
time.sleep(5)
assert_string = driver.find_element_by_xpath("//*[@id='username-container']/div[2]/em"); # assert_string_var_defined_to_find_particular_text_and_verify_it_later
assert assert_string.text == 'jane@hushmail.com'; # verifies_that_we_are_on_the_correct_page
time.sleep(1)


## put_credentials_and_log_in
# put_user
driver.find_element_by_xpath("//*[@id='hush_username']").click();
driver.find_element_by_xpath("//*[@id='hush_username']").send_keys(usr);
time.sleep(0.2)


# put_pass
driver.find_element_by_xpath("//*[@id='hush_passphrase']").click();
driver.find_element_by_xpath("//*[@id='hush_passphrase']").send_keys(pss);
time.sleep(0.2)


# click_login__sign_in_button
driver.find_element_by_xpath("//*[@id='submit-container']/input").click();
time.sleep(10)


# find_username_on_the_inbox_page_to_assert_we_are_on_the_correct_page
# assert assert_string2.text == ''; --> put_your_username_here
assert_string2 = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div[1]/span[1]/span"); # assert_string2_var_defined
assert assert_string2.text == ''; # hence_verified_that_we_are_on_the_correct_page
time.sleep(2)

# hiding_the_warning_that_aks_to_get_premium_hushmail_(if_its_there)
hide = driver.find_element_by_class_name("event_hide-status")
if hide:
	hide.click();
else:
	pass
time.sleep(2)


# spam_defined
# keep_defining_spam_senders_here_after_comma_and_between_double_quotes
# remember_these_are_casesensitive_and_considers_whitespaces_and_other_characters
# better_to_copy__paste_as_they_are_in_this_field
spam = ["ACBNews", "BBC-World"];


## def_a_function
def try_spam():
	for i in spam[0:]: # range_in_spam_starting_from_0_everytime_until_there_are_no_more_to_look_upon_in_the_list
	    checkboxes = driver.find_elements_by_xpath("//a[contains(text(), '{}')]/parent::td//preceding-sibling::td//input[@type='checkbox']".format(i)) # checkbox_selection_by_finding_the_parent_and_preceding_sibling_of_i_in_spam
	    for checkbox in checkboxes: # for_a_single_checkbox_from_checkboxes
	    	if not checkbox.is_selected(): # if_i_from_spam_is_not_selected
	    		checkbox.click(); # select_the_i_from_spam


try_spam() # to_start_the_function_we_just_created
time.sleep(2)
print("CHECKED AND SELECTED ALL THE SPAMS\n")
time.sleep(2)



## pushes_the_selected_spam_to_the_trash_bin_(doesnt_confirm_from_the_user)
driver.find_element_by_xpath("//*[@id='element_message-list-toolbar']/div/div[5]/input[1]").click(); # clicks_the_delete_button
time.sleep(0.5) # waits
driver.find_element_by_xpath("//*[@id='element_delete-message-dialog-template']/div/div[3]/div[3]/form/div[2]/input").click(); # clicks_the_confirmation_delete_button



#usr_inpt()
def usr_inp():
	usr_inpt = input("Would you want me to delete the spam(s) from trash? Type only yes or no: ") # asks_for_yes__no
	if usr_inpt == 'yes':
	    print("Deleting spam(s) permanently from your trash. WIN users --> Ctrl+C to interrupt if gave a yes command by mistake.") # warning
	    time.sleep(10)
	    driver.get("https://secure.hushmail.com/preview/hushmail/#folder/Trash") # opens_trash_in_hushmail
	    time.sleep(10)
	    driver.find_element_by_xpath("//*[@id='element_message-list-toolbar']/div/div[6]/input").click(); # clicks_delete_all_permanently
	    time.sleep(1)
	    driver.find_element_by_xpath("//*[@id='element_delete-message-dialog-template']/div/div[3]/div[3]/form/div[2]/input").click(); # clicks_the_final_delete_all
	    time.sleep(3)
	    driver.get("https://secure.hushmail.com/1.1.5/preview/hushmail/{}/folder/Inbox".format(usr)); # goes_back_to_the_inbox
	elif usr_inpt == 'no':
		print("Thank you for using my service.")
	else:
		print("Type only yes or no.\n")
		usr_inp()
		time.sleep(5)


usr_inp() # to_start_the_function
