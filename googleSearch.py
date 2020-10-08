import pprint
from vault.credentials import Credentials
from googleapiclient.discovery import build


def google_search(query):
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    # Handle if no search results found
    cred=Credentials()
    service = build("customsearch", "v1",
                    developerKey=cred.get_google_api_key())

    result = service.cse().list(
        q=query,
        cx=cred.get_google_cse_key(),
    ).execute()
    try:
        items = result["items"]
        top_five_links = []
        for i in items:
            if(len(top_five_links) < 5):
                top_five_links.append(i["link"])
        pprint.pprint(result["items"])
        return top_five_links
    except:
        return

