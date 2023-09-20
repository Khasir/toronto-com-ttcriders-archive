from pathlib import Path
import os

import pdfkit
import scrapy


class TorontoComSpider(scrapy.Spider):
    name = "toronto.com"

    def __init__(self, input_file: str = None, *args, **kwargs):
        super(TorontoComSpider, self).__init__(*args, **kwargs)
        self.output_dir = f"output/{self.name}"

        self.input_file = input_file
        if self.input_file:
            self.input_file = os.path.expanduser(self.input_file)
            self.log(f"Input file: {self.input_file}")
        if not self.input_file:
            raise ValueError("Please specify the input file containing URLs.")
        elif not os.path.exists(self.input_file):
            raise FileNotFoundError(f"File does not exist: {self.input_file}")

    def start_requests(self):
        os.makedirs(self.output_dir, exist_ok=True)
        with open(self.input_file, 'r', encoding='utf-8') as file:
            for line in file:
                yield scrapy.Request(url=line.strip(), callback=self.parse)

    def parse(self, response):
        # Save HTML
        pagename: str = os.path.split(response.url)[1]
        filename = f"{self.output_dir}/{pagename}"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved HTML to: {filename}")

        # Save PDF
        period_index = pagename.find('.')
        pdf_name = pagename + ".pdf"
        if period_index >= 0:
            pdf_name = '.'.join(pagename.split('.')[:-1]) + ".pdf"
        filename = f"{self.output_dir}/{pdf_name}"
        # self.convert_html_to_pdf(response.body, filename)
        pdfkit.from_string(str(response.body, encoding='utf-8'), filename)
        self.log(f"Saved PDF to: {filename}")
