import requests  # used to request data from reddit
# import json   (only needed to save the json to see how it is structured (not needed for the main part of the program)

# Imports to create interactive graph

from plotly import offline


class Reddit:
    def r_graph(self, time, subreddit='learnpython'):  # default subreddit is learnpython

        # requesting the information

        headers = {
            'authority': 'www.reddit.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': 'csv=1; edgebucket=bRkItS6Vr3cKCZOUF4; __gads=ID=55c2de4f466a9104:T=1609350521:S=ALNI_MZYAXE1q8H2aW2gpqAR9ePrPn36jw; eu_cookie_v2=3; G_ENABLED_IDPS=google; pc=de; _rdt_uuid=1614720656004.86c45b48-7360-4c17-8acf-19f79c0dd73a; show_announcements=no; USER=eyJwcmVmcyI6eyJsYXlvdXQiOiJjYXJkIiwiZ2xvYmFsVGhlbWUiOiJSRURESVQifX0=; g_state=^{^\\^i_l^\\^:0,^\\^i_t^\\^:1615052854329^}; reddit_session=750220390183^%^2C2021-03-05T17^%^3A50^%^3A57^%^2C8f11e615f62fae7c45b4d5f175cc78fd013c5364; loid=00000000009kn9uluv.2.1609350518000.Z0FBQUFBQmdRbS1CblZKWC0tejgtZ0tMdnV0VjdiWG1ZTjJqc2liaGY0djR1Z1lnMWFQaTBVM3d5VUx2U09KeGg3LVRPUnpNSEhPWXhpY3o3QmN0ZWdmbUVSY3ZqMlQ3OFRRellrVnVhTEZmWjZfcVc4Y2UteVowUnl0cVF4N0RSM1RjNW9EbG5VWnE; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTUwMzIwMjEsInN1YiI6Ijc1MDIyMDM5MDE4My10aWR0eXBNTzBOTG11cFdKYXZFWFFWSkgtY0kiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCJdfQ.QU91XOs-rim7vYOzUWSXP6_H8n80iG_lYhwf3i6uyVE; __aaxsc=2; aasd=9^%^7C1615028526940; session=0433194fe02afab6cab8bbdd07b9b7ffd27d80c3gASVSQAAAAAAAABKP2JDYEdB2BDYUBhdj32UjAdfY3NyZnRflIwoMjk5OWUxYjNjYWVhNzEzYjJlNzMwZDcxNjE5MWRlN2Y4ZTc4ODA0ZZRzh5Qu; session_tracker=fdqlgoepdnbpamelib.0.1615028880336.Z0FBQUFBQmdRMktRQ3A4RDNhclMteVNVakM1cXppWVJMNGcwX2YyN2JVcW5HaVd3c1JDS3ptYU0xajBwWXZ3OVd2YlNZVVJWMVJBMEhiUkRZeXBOWWdQY0J3cEtqZ0FubTFxNUlyUEx3bGwzTTJDcHoxOHA0U2pIODEwUm1yUDlwbTd1T1h6Z1pTV04',
        }

        params = (
            ('t', time),
        )

        response = requests.get(f'https://www.reddit.com/r/{subreddit}/top/.json', headers=headers, params=params)

        response_dict = response.json()   # create a json file from the request

        # Saving the json file to find the keys (''' out because it isn't part of the program just showing how I know all of the keys to information)

        '''
        readable_file = r'area you want to save it to\something.JSON'
        with open(readable_file, 'w') as e:
            json.dump(response_dict, e, indent=4)
        # then you would just go into that file and open, it would look like this https://imgur.com/a/O54qNdF
        '''

        # getting all information about all posts from the json file

        posts = response_dict['data']['children']  # get all posts/children

        # lists of all info

        upvotes, hyperlinks_to_posts, hover_text = [], [], []

        # for loop to get each individual posts information

        for post in posts[:20]:  # get first 20 posts

            Ups = post['data']['ups']
            author = post['data']['author']
            title = post['data']['title']

            upvotes.append(Ups)  # add the current posts upvotes to the list of upvotes

            # Creating HoverText (<br /> is how you enter using plotly)
            text = f"Author: {author}<br />Upvotes: {Ups}<br />Title: {title}"
            hover_text.append(text)

            # creating hyperlink
            post_link = post['data']['url']
            hyperlinks_to_posts.append(f"<a href='{post_link}'>{author}</a>")

        # Plotting the graph

        # Setting the data in graph

        data = [{
            'type': 'bar',
            'x': hyperlinks_to_posts,
            'y': upvotes,
            'hoverinfo': 'text',
            'hovertext': hover_text,   # hover text is text that appears when you hover mouse over the bar
            'marker': {
                'color': 'rgb(57, 106, 177)',   # set bar colour
                'line': {'width': 1.5, 'color': 'rgb(57, 106, 250)'}  # small line around bar for a better appearance
            },
            'opacity': 0.6   # set opacity of the bar  (make it see through)
        }]

        # Setting the layout of the graph
        link_to_subreddit = f"<a href='https://www.reddit.com/r/{subreddit}/'>r/{subreddit}</a>"

        my_layout = {
            'title': f'Top 20 Most Popular Reddit Posts On {link_to_subreddit}',
            'titlefont': {'size': 28},
            'xaxis': {
                'title': 'Hyperlinks To Posts',
                'titlefont': {'size': 20},
                'tickfont': {'size': 14},
            },
            'yaxis': {
                'title': 'Upvotes',
                'titlefont': {'size': 20},
                'tickfont': {'size': 14},
            },
        }

        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='Subreddit_Top_Posts.html')


c = Reddit()
c.r_graph(time='year', subreddit='learnpython')  # times are: now, today, month, year and all
