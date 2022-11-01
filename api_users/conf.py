POSTGRES = {
    'user': 'postgres',
    'pw': 'sua_senha',
    'db': 'fcamara_nilo_health',
    'host': 'host.docker.internal', # Docker: host.docker.internal
    'port': '5432',
}


DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


# Header (Authorization) Key: 'Api-Token'
KEY_VALUE = 'd33cdf514b426b'