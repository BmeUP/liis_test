from db.maindb import engine
from models.base import Base
from models.user_model import User 
from models.poll_model import Poll
from models.variant_model import Variant

Base.metadata.create_all(engine)