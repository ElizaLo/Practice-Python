import requests_with_caching
import json

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5

    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)



# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")


import requests_with_caching
import json

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5

    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(d):
    return [i['Name'] for i in d['Similar']['Results']]

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
#extract_movie_titles(get_movies_from_tastedive("Black Panther"))



import requests_with_caching
import json

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5

    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(d):
    return [i['Name'] for i in d['Similar']['Results']]

def get_related_titles(lst):
    l = []
    for title in lst:
        movies = get_movies_from_tastedive(title)
        titles = extract_movie_titles(movies)
        l1 = [l.append(movie) for movie in titles if movie not in l]
    return l

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
#extract_movie_titles(get_movies_from_tastedive("Black Panther"))


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])


import requests_with_caching
import json

def get_movie_data(movie_title):
    url = 'http://www.omdbapi.com/'
    param = {'t': movie_title, 'r': 'json'}
    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")


import requests_with_caching
import json

def get_movie_data(movie_title):
    url = 'http://www.omdbapi.com/'
    param = {'t': movie_title, 'r': 'json'}
    this_page_cache = requests_with_caching.get(url, params=param)
    #print(json.loads(this_page_cache.text))
    return json.loads(this_page_cache.text)

def get_movie_rating(d):
    movie_ratings = d['Ratings']
    for rate in movie_ratings:
        if rate['Source'] == 'Rotten Tomatoes':
            print(rate['Value'])
            return int(rate['Value'][:-1])
    return 0

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_movie_data("Black Panther")
#get_movie_data("Baby Mama")
#get_movie_data('Deadpool 2')



# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))





import requests_with_caching
import json

def get_movies_from_tastedive(title):
    url = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5

    this_page_cache = requests_with_caching.get(url, params=param)
    return json.loads(this_page_cache.text)

def extract_movie_titles(d):
    return [i['Name'] for i in d['Similar']['Results']]

def get_related_titles(lst):
    l = []
    for title in lst:
        movies = get_movies_from_tastedive(title)
        titles = extract_movie_titles(movies)
        l1 = [l.append(movie) for movie in titles if movie not in l]
    return l

def get_movie_data(movie_title):
    url = 'http://www.omdbapi.com/'
    param = {'t': movie_title, 'r': 'json'}
    this_page_cache = requests_with_caching.get(url, params=param)
    #print(json.loads(this_page_cache.text))
    return json.loads(this_page_cache.text)

def get_movie_rating(d):
    movie_ratings = d['Ratings']
    for rate in movie_ratings:
        if rate['Source'] == 'Rotten Tomatoes':
            print(rate['Value'])
            return int(rate['Value'][:-1])
    return 0

def get_sorted_recommendations(lst_movie_titles):

    new_lst = get_related_titles(lst_movie_titles)
    new_d = {}

    for title in new_lst:
        data = get_movie_data(title)
        rate = get_movie_rating(data)
        new_d[title] = rate
        #print(new_d)
    return [i[0] for i in sorted(new_d.items(), key=lambda item: (item[1], item[0]), reverse=True)]

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])


