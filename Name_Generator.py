#import modules
from bs4 import BeautifulSoup
import requests

#create function
def get_data(url, file_name):

    # make a get request
    page = requests.get(url)
    # this line is not essential, but if we want to check 
    # the result, we can add it. It should be <Response 
    #[200]>. It means that the request succeeded.
    print(page)

    # check if an error occurs
    page.raise_for_status()

    # extract text - now we have all the text from the page
    soup = BeautifulSoup(page.text, "html.parser")

    print(soup)
# this line is also optional, only to see in command line
# how it works. If we use this command, we will have the 
# whole HTML document printed in the command line.


    # now find the table with data we want. In order to do 
    #it, we have to check the id of the table.
    tbody = soup.find_all(id="myTable")
    # if we want to see the output in command line
    print(tbody)

    # now it's time to store the data from the website.
    f = open(file_name, "w+") # it creates a file in which 
                              # it will write the data
    records = []

    # if we take a look at the output of print(tbody) we can
    # see that we have many <td> and <tr> tag elements. 
    # First we go through all the elements in tbody to find
    # ALL tr (table row) elements
    for elem in tbody:
        rows = elem.find_all("tr")

        # now we want to loop over rows. We can check how 
        # many rows are there and decide how many names we 
        # wish to store. I want to have many names, so I 
        # decided to loop over 300 rows.
        for row in rows[1:301]:

            # in each row we want to find table data with a 
            # name. Because in our rows, we have a few td 
            # elements, but only the first td element 
            # contains the name I'm using find("td") method
            column = row.find("td")
            # to extract only text we can use .text method,
            # but because the names in the table are written 
            #in UPPER CASE I'm .capitalize() method.
            column_text = column.text.capitalize()

            # store all the names in records list
            records.append(column_text)

    # the last step is to write the names into the file,
    # each name in the new line
    for record in records:
        f.write(record + "\n")

# I'm calling the function 3 times to have 3 files: one for 
# women's first names, one for men's first names, and one 
# for surnames

url = "https://namecensus.com/data/1000.html"
file_name = "last_names.txt"
get_data(url, file_name)

url = "https://namecensus.com/male_names.htm"
file_name = "male_first_names.txt"
get_data(url, file_name)

url = "https://namecensus.com/female_names.htm"
file_name = "female_first_names.txt"
get_data(url, file_
