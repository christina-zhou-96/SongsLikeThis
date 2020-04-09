from flask import Flask,redirect,request

# Create app instance.
app = Flask(__name__)

# Create homepage with form.
@app.route("/")
def home():
    return"""
    <html><body>
        <h2>Find yo songs</h2>
        <form action="/link">
            YouTube video link <input type='text' name='link'>
            <input type='submit' value='Go'>
        </form>
        
        <br>
        
        <form action="/about">
            <input type='submit' value='About'>
        </form>
    </body></html>
    """

# Create about page.
@app.route("/about")
def about():
    return"""
    <html><body>
        Just think about a song you really like, that you've been trying
        to find more songs like. 
        
        <br>
        <br>
        
        Find it on Youtube and paste its url here to find playlists made by others who enjoyed the song!
        
        <br>
        <br>
                
        I've used this to find playlists of similar taste without limiting
        myself to finding them by genre, which can provide rather stale mixes. 
        
        <br>
        <br>
                
        <a href="https://github.com/christina-zhou-96/FindYoSongs">Code</a>
    </body></html>
    """

# Backend logic to redirect user to the new Google page.

# TODO: I don't think this works with a video link already in a playlist, like
# v=42ijrf02oij$list=....
# Should change backend logic to only get the string between v= and &.

@app.route("/link")
def link():

    # Get the link from user.

    link = request.args['link']

    # Find the video ID.
    # Current business rule: video ID is between v= and &

    video_id = link.partition("v=")[2]

    # Relink to the Google search.
    # Current business rule: looks like site:youtube.com inurl(2jopgOD + list)

    google_search_base_url = "https://www.google.com/"
    google_search_param = "search?q="

    def youtube_search_builder(video_id):
        return f'site%3Ayoutube.com+inurl%3A({video_id}+list)'

    final_link = google_search_base_url + \
                 google_search_param + \
                 youtube_search_builder(video_id)

    return redirect(final_link)

# Run app.
if __name__ == "__main__":
    app.run()

