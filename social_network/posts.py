from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None
        
        if not timestamp:
            timestamp = datetime.today()

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{date}'.format(
            first_name=self.user.first_name, 
            last_name=self.user.last_name, 
            text=self.text, 
            date=self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{first_name} {last_name}: "{text}"\n\t{image}\n\t{date}'.format(
            first_name=self.user.first_name, 
            last_name=self.user.last_name, 
            text=self.text,
            image=self.image_url,
            date=self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{first_name} Checked In: "{text}"\n\t{lat}, {long}\n\t{date}'.format(
            first_name=self.user.first_name, 
            last_name=self.user.last_name, 
            text=self.text,
            lat=self.latitude,
            long=self.longitude,
            date=self.timestamp.strftime('%A, %b %d, %Y'))
           