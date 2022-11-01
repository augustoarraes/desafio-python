from init import db


class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String())
    email = db.Column(db.String())
    address_street = db.Column(db.String())
    address_suite = db.Column(db.String())
    address_city = db.Column(db.String())
    address_zipcode = db.Column(db.String())
    address_geo_lat = db.Column(db.String())
    address_geo_lng = db.Column(db.String())
    phone = db.Column(db.String())
    website = db.Column(db.String())
    company_name = db.Column(db.String())
    company_catchPhrase = db.Column(db.String())
    company_bs = db.Column(db.String())

    def __init__(self, id, name, username, email, address_street, address_suite, address_city, address_zipcode, address_geo_lat, address_geo_lng, phone, website, company_name, company_catchPhrase, company_bs):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address_street = address_street
        self.address_suite = address_suite
        self.address_city = address_city
        self.address_zipcode = address_zipcode
        self.address_geo_lat = address_geo_lat
        self.address_geo_lng = address_geo_lng
        self.phone = phone
        self.website = website
        self.company_name = company_name
        self.company_catchPhrase = company_catchPhrase
        self.company_bs = company_bs

    def __repr__(self):
        return f"<User {self.name}>"