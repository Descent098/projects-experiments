import time
import requests
import psutil
from urllib.parse import urlparse
from scraping import Site
from concurrent.futures import ThreadPoolExecutor

def get_peak_cpu_usage(func, *args, **kwargs):
    cpu_usages = []
    memory = []
    start_time = time.time()
    
    # Start monitoring CPU usage in a loop
    while (time.time() - start_time) < 1:
      cpu_usages.append(psutil.cpu_percent(interval=0.1)) #Check CPU every 0.1 second
      memory.append(psutil.virtual_memory().percent)
      
    result = func(*args, **kwargs) # Execute the function
    
    # Continue monitoring CPU usage after function execution for 1 second
    start_time = time.time()
    while (time.time() - start_time) < 1:
      cpu_usages.append(psutil.cpu_percent(interval=0.1))
      memory.append(psutil.virtual_memory().percent)
    return max(cpu_usages), max(memory)

def get_data_from_url(url:str) -> Site:
    print(f"Parsing {url}")
    try:
        temp = urlparse(url)
        resp = requests.get(url, timeout=5)
    except Exception as e:
        print(f"Could not parse {url}")
        return
    return Site(
        url, 
        temp.hostname,
        resp.headers.get("server", ""),
        temp.scheme,
        resp.headers.get("Content-Type", "text/html"),
        resp.text,
        temp.port
    )

def pure_python_scraping(urls:list[str]) -> list[Site]:
    with ThreadPoolExecutor(max_workers = 10) as executor:
        temp = executor.map(get_data_from_url, urls)
        result = list(temp)
    return result

def simple_benchmarking(urls:list[str]):
    
    t1 = time.time()
    cpu_1, mem_1 = get_peak_cpu_usage(pure_python_scraping, urls)
    t2 = time.time()
    
    t3 = time.time()
    cpu_2, mem_2 = get_peak_cpu_usage(Site.from_urls, urls)
    t4 = time.time()
    
    time.sleep(30)
    print("compiling results")
    import logging
    logging.basicConfig(filename="res.log", filemode="w+", level=logging.INFO)
    
    q = logging.getLogger(__name__)
    print(f"pure_python_scraping took {t2-t1} seconds for {len(urls)} sites with:\n\tMax CPU usage of {cpu_1}\n\tMax RAM usage of: {mem_1} %")
    print(f"Site.from_urls took {t4-t3} seconds for {len(urls)} sites with:\n\tMax CPU usage of {cpu_2}\n\tMax RAM usage of: {mem_2} %")
    total_memory = psutil.virtual_memory().total
    q.info(f"pure_python_scraping took {t2-t1} seconds for {len(urls)} sites with:\n\tMax CPU usage of {cpu_1}\n\tMax RAM usage of: {mem_1} %")
    q.info(f"Site.from_urls took {t4-t3} seconds for {len(urls)} sites with:\n\tMax CPU usage of {cpu_2}\n\tMax RAM usage of: {mem_2} %")
    
    difference = max(mem_1, mem_2) - min(mem_1, mem_2)
    difference_multiplier = difference/100
    print(f"Memory difference is {difference}% of {total_memory}\n\t{difference_multiplier*total_memory}B\n\t{(difference_multiplier*total_memory)//1024}KB\n\t{((difference_multiplier*total_memory)//1024)//1024}MB")
    q.info(f"Memory difference is {difference}% of {total_memory}\n\t{difference_multiplier*total_memory}B\n\t{(difference_multiplier*total_memory)//1024}KB\n\t{((difference_multiplier*total_memory)//1024)//1024}MB")

if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com",
        "https://www.amazon.com",
        "https://www.netflix.com",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.dropbox.com",
        "https://www.spotify.com",
        "https://www.tumblr.com",
        "https://www.quora.com",
        "https://www.stackoverflow.com",
        "https://www.medium.com",
        "https://www.bing.com",
        "https://www.paypal.com",
        "https://www.ebay.com",
        "https://www.pinterest.com",
        "https://www.tiktok.com",
        "https://www.cnn.com",
        "https://www.bbc.com",
        "https://www.nytimes.com",
        "https://www.theguardian.com",
        "https://www.washingtonpost.com",
        "https://www.forbes.com",
        "https://www.bloomberg.com",
        "https://www.airbnb.com",
        "https://www.udemy.com",
        "https://www.coursera.org",
        "https://www.khanacademy.org",
        "https://www.github.com",
        "https://www.gitlab.com",
        "https://www.codepen.io",
        "https://www.heroku.com",
        "https://www.digitalocean.com",
        "https://www.slack.com",
        "https://www.zoom.us",
        "https://www.skype.com",
        "https://www.trello.com",
        "https://www.notion.so",
        "https://www.canva.com",
        "https://www.wix.com",
        "https://www.shopify.com",
        "https://www.mozilla.org",
        "https://www.icann.org",
        "https://www.cloudflare.com",
        "https://www.openai.com",
        "https://www.deepmind.com",
        "https://www.ibm.com",
        "https://www.oracle.com",
        "https://www.sap.com",
        "https://www.adobe.com",
        "https://www.salesforce.com",
        "https://www.zendesk.com",
        "https://www.asana.com",
        "https://www.bitbucket.org",
        "https://www.bitly.com",
        "https://www.hubspot.com",
        "https://www.mailchimp.com",
        "https://www.figma.com",
        "https://www.behance.net",
        "https://www.dribbble.com",
        "https://www.envato.com",
        "https://www.codeacademy.com",
        "https://www.pluralsight.com",
        "https://www.edx.org",
        "https://www.futurelearn.com",
        "https://www.teachable.com",
        "https://www.skillshare.com",
        "https://www.lynda.com",
        "https://www.x.com",  # Formerly Twitter/X
        "https://www.aliexpress.com",
        "https://www.flipkart.com",
        "https://www.target.com",
        "https://www.homedepot.com",
        "https://www.walmart.com",
        "https://www.bestbuy.com",
        "https://www.nike.com",
        "https://www.adidas.com",
        "https://www.samsung.com",
        "https://www.huawei.com",
        "https://www.sony.com",
        "https://www.lenovo.com",
        "https://www.dell.com",
        "https://www.hp.com",
        "https://www.intel.com",
        "https://www.amd.com",
        "https://www.nvidia.com",
        "https://www.tesla.com",
        "https://www.ford.com",
        "https://www.gm.com",
        "https://www.toyota.com",
        "https://www.honda.com",
        "https://www.bmw.com",
        "https://www.mercedes-benz.com"
    ]

    
    simple_benchmarking(urls)
    

