from selenium import webdriver
import time
from random import randrange
from random import randint
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

    

i=0



zip = open("./zip.txt", "r")
z = zip.read()
z= list(z.split("\n"))
print(len(z))
text_file = open("./names.txt", "r")
states_file = open("./states.txt", "r")
states = states_file .read()
st= list(states.split("\n"))
cities = open("./cities.txt", "r")
ct = cities.read()
ct = list(ct.split("\n"))
streettypes= ["Lane","Road","ave","Avenue","Crossing","Parkway","way","abbey","park","street","st","ln","road","rd"]
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
email=["buffalo.edu","rit.edu","buffstate.edu","albany.edu","gmail.com","gmail.net","gmail.gov","aol.net","aol.com","outlook.com","hotmail.com","yahoo.com","mail.com"]

#18240
#read whole file to a string
data = text_file.read()
li= list(data.split("\n"))
while True:
    i=i+1
    browser = webdriver.Chrome()

    browser.get('https://form.jotform.com/212213034024536')

    browser.find_element_by_xpath('//*[@id="form-pagebreak-next_23"]').click()
    browser.find_element_by_xpath('//*[@id="first_11"]').send_keys(li[randrange(18211)])
    browser.find_element_by_xpath('//*[@id="middle_11"]').send_keys(li[randrange(18211)])
    browser.find_element_by_xpath('//*[@id="last_11"]').send_keys(li[randrange(18211)])
    browser.find_element_by_xpath('//*[@id="input_16_addr_line1"]').send_keys(li[randrange(18211)]+" "+streettypes[randrange(14)])
    browser.find_element_by_xpath('//*[@id="input_16_city"]').send_keys(ct[randrange(25)])
    browser.find_element_by_xpath('//*[@id="input_16_postal"]').send_keys(z[randrange(8328)])
    browser.find_element_by_xpath('//*[@id="input_16_state"]').send_keys(st[randrange(48)])

    browser.find_element_by_xpath('//*[@id="input_18_month"]').send_keys(months[randrange(11)])
    browser.find_element_by_xpath('//*[@id="input_18_day"]').send_keys(random_with_N_digits(1))
    browser.find_element_by_xpath('//*[@id="input_18_year"]').send_keys('19'+ str(random_with_N_digits(2)))
    #SSN
    browser.find_element_by_xpath('//*[@id="input_19"]').send_keys(random_with_N_digits(9))
    browser.find_element_by_xpath('//*[@id="input_13_full"]').send_keys(random_with_N_digits(10))
    browser.find_element_by_xpath('//*[@id="input_14"]').send_keys('YES')
    browser.find_element_by_xpath('//*[@id="input_12"]').send_keys(li[randrange(18211)] + li[randrange(18211)] + li[randrange(18211)] + "@" +email[randrange(12)])

    browser.find_element_by_xpath('//*[@id="input_17"]').send_keys('/home/anthony/Downloads/elf.png')
    browser.find_element_by_xpath('//*[@id="input_24"]').send_keys('/home/anthony/Downloads/elf.png')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="input_9"]').click()
    browser.close()
    print(i)

