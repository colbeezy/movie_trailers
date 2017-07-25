import webbrowser

"""This class provides a way to store information related to movies"""
class Movie():

    """This constructor takes movie title, poster, youtube trailer link and
    outputs custom variables"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """This function opens a web browser at the YouTube URL of the trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
