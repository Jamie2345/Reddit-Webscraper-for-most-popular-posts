import requests
# import json   (only needed to save the json to see how it is structured (not needed for the main part of the program)

# Imports to create interactive graph
from plotly import offline


class Reddit:
    def r_graph(self, time, subreddit='learnpython'):  # default subreddit is learnpython
        
        # set up headers not difficult just looks, If my instuctions are bad here's a video I found explaining how to do It https://www.youtube.com/watch?v=Mw-dsY8UKVs&t=129s
        
        headers = {
            # Step 1: go to https://www.reddit.com/.json  Step 2: press f12    Step 3: Click Network   Step 4: Refresh The Page  Step 5: Right Click .json then hover over copy and then copy as Curl cmd
            # Step 6: go to https://curl.trillworks.com/ and paste link on the left box  # Step 7: copy everyting from right box and paste under hear then remove everything apart from the text under headers
        }

        params = (
            ('t', time),
        )

        response = requests.get(f'https://www.reddit.com/r/{subreddit}/top/.json', headers=headers, params=params)
        
        response_dict = response.json()   # create a json file from the request
        posts = response_dict['data']['children']  # get all posts/children

        # lists of all info
        upvotes, hyperlinks_to_posts, hover_text = [], [], []

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
