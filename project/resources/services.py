from flask_restful import Resource, reqparse
from sqlalchemy.orm import sessionmaker
from .auth_user import is_user_auth
from db.maindb import engine
from models.user_model import User
from models.poll_model import Poll
from models.variant_model import Variant

main_parser = reqparse.RequestParser()
session = sessionmaker(bind=engine)
salt = b'asdfkdlsfurithqwnadsjks4ad5f48as7d5f645a6sdf465asdf'

class RegisterUser(Resource):
    def post(self):
        main_parser.add_argument('name', type=str)
        main_parser.add_argument('password', type=str)
        args = main_parser.parse_args()

        with session() as ses:
            new_user = User(
                name=args.get('name'),
                password=User.create_password(args.get('password'), salt)
            )

            ses.add(new_user)
            ses.commit()
        
        return {"user": "created"}

class CreatePoll(Resource):
    def post(self):
        is_auth = False
        variants = []
        main_parser.add_argument('name', type=str)
        main_parser.add_argument('password', type=str)
        main_parser.add_argument('poll_name', type=str)
        main_parser.add_argument('question', type=str)
        main_parser.add_argument('variants', action='append')
        args = main_parser.parse_args()
        is_auth = is_user_auth(session, User, args.get('name'), args.get('password'), salt)
        
        if is_auth:
            with session() as ses:
                poll = Poll(name=args.get('poll_name'), question=args.get('question'))
                ses.add(poll)
                ses.flush()
                for variant in args.get('variants'):
                    variants.append(Variant(text=variant, poll_id=poll.id))
                ses.add_all(variants)
                ses.commit()

        return {"this is args": args}
