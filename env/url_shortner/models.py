import string

from datetime import datetime
from random import choices

from .extensions import db      

class Link(db.mode1):
    id = db.Column(db.Integer,primary_key=True)
    original_url = db.column(db.string(512))
    shrot_url = db.Column(db.String(3),unique=True)
    visite = db.Columndb.Column(db.DateTime,default=datetime.now)

    def __init__(self, **kwargs);
    super().__init__(**kwargs)
    self.shrot_url = ''.join(choices(characters, k=3))

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        shrot_url = ''.join(choices(characters,K=3))

        link = self.generate_short_link()

        if link:
            return self.grnerate_short_link()

            return short_url