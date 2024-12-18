import requests
import json

headers = {
    'abp-culturename': 'c=null|uic=null',
    'abp-tenantid': '23',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://truckline.com.au',
    'priority': 'u=1, i',
    'referer': 'https://truckline.com.au/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

params = {
    'd': '1731233765886',
}
data_list = list()
response = requests.get('https://api-v3.partsb2.com.au/AbpUserConfiguration/GetAll', params=params, headers=headers)
data = json.loads(response.text)
data_to_fetch = data.get('result', {}).get('setting',{}).get('values',{}).get("App.EPCSettings.TopCategory.DisplayOrder",{})
if data_to_fetch:
    data_to_fetch = json.loads(data_to_fetch)
    for category in data_to_fetch[1:]:
        casetogy_id = category['CategoryId']
        category = category['CategoryName']
        payload = params = {
                'CategoryId': casetogy_id,
                'InStock': 'false',
                'IncludeRichContentDeltaInfo': 'false',
                'ExcludeStockAndPrice': 'true',
                'Sorting': "'Brand.Priority' : 1, 'Brand.BrandName' : 1",
                'MaxResultCount': '96',
                'SkipCount': '0',
            }
        headers = {
            'abp-customerid': '779386fc-2222-4c74-98f0-700d216414b2',
            'abp-tenantid': '23',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'b2v4apikey': 'truckline.IQhz6BfZZW3794H1Hgf3dKAP8hJfBZZFI2o6654NUv4=',
            'origin': 'https://truckline.com.au',
            'priority': 'u=1, i',
            'referer': 'https://truckline.com.au/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        response = requests.get('https://api-v3.partsb2.com.au/api/Product/GetProducts', params=params, headers=headers)
        data = json.loads(response.text)
        total_count = data.get('result', {}).get('products',{}).get('totalCount')
        data_dicts = data.get('result', {}).get('products',{}).get('items',[])


        counter = 0
        for i in range(0, total_count, 1000):
            payload['MaxResultCount'] = 1000
            payload['SkipCount'] = i
            response = requests.get('https://api-v3.partsb2.com.au/api/Product/GetProducts', params=params, headers=headers)
            data = json.loads(response.text)
            total_count = data.get('result', {}).get('products',{}).get('totalCount')
            data_dicts = data.get('result', {}).get('products',{}).get('items',[])
            for data_dict in data_dicts:
                part_no = data_dict.get('productNr')
                part_name = data_dict.get('ced',{}).get('companyEnhancedData',{}).get('companyProductTitle')
                data_list.append({
                    "category": category,
                    "part_no": part_no,
                    "part_name": part_name
                })            
                counter += 1
        print(counter)
import pandas as pd
df = pd.DataFrame(data_list)
print(df)
df.to_csv('output.csv', index=False)