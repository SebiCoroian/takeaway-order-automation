# takeaway-order-automation
A Selenium bot that will order your regular lunch with every run

For security reasons, the bot runs in incognito mode, generating a disposable e-mail adress using <https://temp-mail.org/> API

#### HOW TO USE

Inside the code you'll find comments and variables with self explanatory names.

First, you need to change your desired restaurant's (in your range of delivery) URL. THis is done in 
This is done inside `restaurant_url`

Next, you need to fill in your personal data inside `USER CONFIG` section

To select the desired product, you need to navigate to `PRODUCT SELECTION` and fill in the header of the dish

In case you are ordering fron an appartment/office building, you need to navigate to `ADRESS` section
Here, you'll need to list the previous elements of the FIELDS array (FIELDS[7], FIELDS[6], FIELDS[5], etc.)
This is done according to the order they are listed on the view, FIELDS[0] being the first label.

Enjoy!
