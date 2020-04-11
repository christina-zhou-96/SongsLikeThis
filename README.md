Find more songs like the one you like! <br>

Try it out at <b> https://findyosongs.herokuapp.com/ </b> <br>

<b>
Notes
</b>

<br>

You're likely to only get a hit if these are relatively well known songs. 
This is because this only works if the playlists were indexed elsewhere on the web.
That means, if someone posted it as in their own blog or Facebook.
Sometimes, you'll click on the video and there is no playlist, I think the playlist went private in that case.

<br>

<b>
Resources
</b>

<br>

Local app <br>
1. Make a Flask app <br>
https://runestone.academy/runestone/books/published/thinkcspy/WebApps/07-InputForAFlaskWebApplication.html <br>

2. The idea <br>
This is a tip from user Ruben on stack overflow <br>
https://webapps.stackexchange.com/questions/44215/how-can-i-view-what-playlist-if-any-a-youtube-video-is-in <br>

Deployment <br>
1. Overview to deploy with Heroku <br>
which sounds cuter and easier than Amazon or Google <br>
https://pythonhow.com/deploying-your-web-application-to-the-cloud/ <br>

2. Generating a requirements file <br>
https://stackoverflow.com/questions/40192651/django-pip-freeze-results-in-empty-file <br>

3. The official Windows help <br>
Notice the special Windows procfile... <br>
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app <br>

4. Make a Procfile with Waitress <br>
https://books.google.com/books?id=cVlPDwAAQBAJ&pg=PT282&lpg=PT282&dq=%22waitress%22+procfile&source=bl&ots=xNJYeoYq9_&sig=ACfU3U1aUYxH6Zjxy5pi-jXDJdf4CZF_2w&hl=en&sa=X&ved=2ahUKEwioxOPcitzoAhWCl3IEHSGsAwoQ6AEwBnoECAkQKQ#v=onepage&q=%22waitress%22%20procfile&f=false
<br> If you're on Windows, you can't use gunicorn, which is what the tutorial
wants you to use. (The tutorial does have an example Windows procfile, but
that's only applicable for local use.) <br>

Connect to Youtube <br>
1. Overview of steps to use Youtube API <br>
https://developers.google.com/youtube/v3/getting-started <br>

2. python Youtube connection <br>
https://github.com/youtube/api-samples/tree/master/python <br>

3. The data structure of a video <br>
https://developers.google.com/youtube/v3/docs/videos#resource<br>

4. Read text in python <br>
https://cmdlinetips.com/2018/01/how-to-read-entire-text-file-in-python/<br>

<b>Contributions</b> <br>

Mixes: Recently Youtube added "mixes", which are not playlists.
Mixes, in case you don't know, are autogenerated Youtube slosh.
Only you can view your own mixes, so if you land on a "mix"
page, it just looks like there was no new content at all.
For now, I tell users to ignore any search results with the 
word "mix" but it would be nice to programmatically ignore them.

