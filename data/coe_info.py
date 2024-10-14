from langchain_community.document_loaders import UnstructuredURLLoader

#fetch COE Info
urls = [
    "https://www.mot.gov.sg/news/Details/oral-reply-by-acting-minister-for-transport-chee-hong-tat-to-parliamentary-question-on-coe-demand-and-supply",
    "https://onemotoring.lta.gov.sg/content/onemotoring/home/buying/upfront-vehicle-costs/certificate-of-entitlement--coe-.html",
    "https://www.nlb.gov.sg/main/article-detail?cmsuuid=9fadc994-c8b2-45a9-9f35-372d05703ddc",
    "https://blog.seedly.sg/coe-bidding-and-price-history-trend-singapore/",
    #"https://onemotoring.lta.gov.sg/content/onemotoring/home/owning/coe-renewal.html",
]

loader = UnstructuredURLLoader(urls=urls)
COE_Info = loader.load()
#print(data[0])
