import scrapy


class TestJobSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
                'https://careers-redhat.icims.com/jobs/search?ss=1&searchKeyword=RHEL&searchPostedDate=01%2F12%2F2017+00%3A00%3A00.000&searchLocation=17992--Remote',
                'https://ldd.tbe.taleo.net/ldd03/ats/careers/searchResults.jsp;jsessionid=8CC857486642F1ECF31964129504CE69?org=CANONICAL&cws=1',
                'https://www.covermymeds.com/main/careers/all-positions/',
                'https://www.jobsatosu.com/postings/search?utf8=%E2%9C%93&query=&query_v0_posted_at_date=month&591=&577=&578=&579=&580=4&581=&commit=Search',
                'https://oclc.wd1.myworkdayjobs.com/OCLC_Careers',
                'https://www.verizon.com/about/work/jobs/search?cf[jobfamily][]=IT&radius=33.8703%2C-117.9253%2C80.467&v_dist=50#qref',
                'https://www.amazon.jobs/en/search?base_query=&loc_query=&job_count=10&result_limit=10&sort=relevant&business_category%5B%5D=amazon-web-services&location%5B%5D=columbus-metropolitan-area&cache',
                'http://rackspace.jobs/jobs/?location=Remote%2C+TX',
                'https://about.gitlab.com/jobs/',
                'https://jobs.github.com/positions?description=&location=remote',
                'https://www.digitalocean.com/company/careers/',
                'https://www.dice.com/jobs/sort-date-q-linux_unix_python_go_bsd-jtype-Full+Time-dtco-true-limit-30-jobs.html?searchid=4637262371475',
                'https://www.dice.com/jobs?q=linux&l=Columbus%2C+OH&searchid=6860418675686'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "jobs-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('saved files %s' %filename)


