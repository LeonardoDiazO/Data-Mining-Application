import sqlalchemy as db
from persistence.modelos import Auth_User
from sqlalchemy.orm import Session

class AuthUserRepository():
    def __init__(self) -> None:
        self.engine= db.create_engine('mysql+pymysql://root:@localhost:3306/bd_energy_login', echo=False,future=False)