# Real Estate Spreadsheet Cleaners
A set of command line scripts to clean spreadsheet outputs from [FlexMLS](https://www.flexmls.com/) and [Cole Realty Resource](https://www.colerealtyresource.com/). 

## Zillow Past Sales Spreadsheet Cleaner
Use this script to clean CSV outputs from FlexMLS sales data to Zillow's [required format](https://zillow.zendesk.com/hc/en-us/articles/227824027-How-can-I-add-Past-Sales-to-my-Zillow-profile-) of:
* Property address (including ZIP)
* Sold date
* Sale price
* Who you represented (Seller, buyer or both)

## Cole Realty Resource Cleaner
Use this script to avoid manually unselecting or deleting rows with incomplete data.  Writes four sheets of data in XLS format for prospects who have the following:
* Email, Cell and Home Phone Number
* Home Phone Number
* Cell Phone Number
* Email Address

### Python Libraries Required
* Pandas

### Author
Emily Nassi - [LinkedIn](https://www.linkedin.com/in/emily-nassi-aa6b4a20/)