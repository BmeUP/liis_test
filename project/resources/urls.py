from .services import RegisterUser, CreatePoll

def urls(api):
    api.add_resource(RegisterUser, '/register-user')
    api.add_resource(CreatePoll, '/create-poll')