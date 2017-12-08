class Movie():

    """Movie class stores any pertinent information about movies"""

    # Constructor to be called when object is first being initialized
    def __init__(self, movie_title, movie_poster, movie_trailer):
        """Init that takes in 3 arguments
        -The movies title
        -Url of the movies poster
        -Url of the movies youtube trailer"""
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
