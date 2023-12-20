import requests
def perform_search(query):
    """
    Perform a search using a GET request with a query string parameter.

    Parameters:
    - query (str): The search query.

    Returns:
    - requests.Response: The response object from the GET request.
    """
    url = "https://httpbin.org"
    params = {"q": query}  # Adding the query parameter to the URL

    # Making the GET request
    response = requests.get(url, params=params)

    return response

# Example search query
search_query = "html"

# Perform the search
response = perform_search(search_query)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Search successful!")
    print("Response content:")
    print(response.text)
else:
    print(f"Search failed with status code {response.status_code}")