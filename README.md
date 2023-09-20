# toronto-com-ttcriders-archive
Archive TTCriders articles on Toronto.com.
The list of webpages was obtained from a google search: `site:toronto.com "ttcriders"`

# Steps to create repo
Follow [Scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html).

# Run guide
1. Install [pdfkit](https://pypi.org/project/pdfkit/).
2. Create python environment and install dependencies in `requirements.txt`.
3. `cd scraper` and `scrapy crawl -a input_file=input/ttcriders.txt toronto.com`
