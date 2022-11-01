from sqlalchemy import desc, select
from model import UsersModel, db


# Carregando a saida da URL https://jsonplaceholder.typicode.com/users
def insert(data):
    for user in data:
        address = user['address']
        geo = address['geo']
        company = user['company']
        new_user = UsersModel(id=int(user['id']), name=user["name"], username=user["username"], email=user["email"], 
                        address_street=address['street'], address_suite=address['suite'], address_city=address['city'], address_zipcode=address['zipcode'], 
                        address_geo_lat=geo['lat'], address_geo_lng=geo['lng'], 
                        phone=user['phone'], website=user['website'], 
                        company_name=company['name'], company_catchPhrase=company['catchPhrase'], company_bs=company['bs'])
        db.session.add(new_user)
        db.session.commit()
    return { "data" : " %s new users inserted" % len(data) }


# Os websites de todos os usuários
def getWebsites():
    users = UsersModel.query.all()
    websites = [
        {
            "website": user.website
        } for user in users ]
    return { "websites": websites }
    

# O Nome, email e a empresa em que trabalha (em ordem alfabética)
def getDetails():
    list = UsersModel.query.order_by(UsersModel.name.asc()).all()
    users = [
        {
            "name": user.name,
            "email": user.email,
            "company": user.company_name
        } for user in list ]
    return { "users": users }


# Mostrar todos os usuarios que contenham determinado texto no nome.
def search(name):
    list = UsersModel.query.filter(UsersModel.name.contains(name)).all()
    users = [
        {
            "id": user.id,
            "name": user.name
        } for user in list ]
    return { "users": users }