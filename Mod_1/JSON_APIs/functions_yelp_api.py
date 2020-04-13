def yelp_call_businesses(url_params, api_key):
    headers = {'Authorization': f'Bearer {api_key}', }
    url =  'https://api.yelp.com/v3/businesses/search'
    response = requests.get(url, headers=headers, params=url_params)
    return response.json()

def parse_data(list_of_data):
    parsed_data = []
    for business in list_of_data['businesses']:
        biz_list = [business['name'],
                    business['id'],
                    business['review_count'], 
                    business['price'],
                    business['rating']]
        parsed_data.append(biz_list)
    
    columns = ['name', 'id', 'review_count', 'price', 'rating']
    df = pd.DataFrame(parsed_data)
    df.columns = columns
    
    return df

def data_save(data, csv_filename):
    existing = pd.read_csv(csv_filename, index_col=0)
    new = pd.concat([existing,data], axis=0, ignore_index=True)
    new.to_csv(csv_filename)


# columns = ['name', 'id', 'review_count', 'price', 'rating']
# new_df = pd.DataFrame(columns=columns)
# new_df.to_csv('yelp_api_lab.csv')
# pd.read_csv('yelp_api_lab.csv', index_col=0)

# cur = 0
# while cur < 1000:
#     url_params['offset'] = cur
#     results = yelp_call_businesses(url_params, api_key)
#     data = parse_data(results)
#     data_save(data, 'yelp_api_lab.csv')
#     cur += 50


def yelp_call_review(biz_id, api_key):
    headers = {'Authorization': f'Bearer {api_key}', }
    url_params = {}
    url = f'https://api.yelp.com/v3/businesses/{biz_id}/reviews'
    response = requests.get(url, headers=headers, params=url_params)
    return response.json()

def parse_data_reviews(business_id, reviews_container):
    parsed_data = []    
    for i in range(len(business_id)):
        try:
            for element in reviews_container[i]['reviews']:
#                 print(i)
                review_list = [business_id[i],
                                   element['rating'], 
                                   element['text'],
                                   element['time_created']]
                parsed_data.append(review_list)
        except KeyError:
            continue
            
    columns = ['id', 'rating', 'text', 'time_created']
    df = pd.DataFrame(parsed_data)
    df.columns = columns
    
    return df

# re-using data_save function
# def data_save(data, csv_filename):
#     existing = pd.read_csv(csv_filename, index_col=0)
#     new = pd.concat([existing,data], axis=0, ignore_index=True)
#     new.to_csv(csv_filename)


# cur = 0
# while cur < 1000:
#     url_params['offset'] = cur
#     results = yelp_call_review(business_id[cur], api_key)
#     cur += 1

# data = parse_data_reviews(business_id, results)
# data_save(data, 'yelp_reviews.csv')