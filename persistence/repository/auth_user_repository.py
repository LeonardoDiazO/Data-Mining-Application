import sqlalchemy as db
from persistence.modelos import Auth_User
from sqlalchemy.orm import Session

class AuthUserRepository():
    def __init__(self) -> None:
        self.engine= db.create_engine('mysql+pymysql://root:@localhost:3306/bd_energy_login', echo=False,future=False)
    
    #Validacion de usuario para verificar que este si esté contenido dentro de la base de datos    
    def getUserByUserName(self, user_name: str):
        user: Auth_User = None
        with Session(self.engine) as session:
            user = session.query(Auth_User).filter_by(
                username=user_name).first()
        return user
    
    #Insersion de usuario 
    def insertUser(self,user:Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()         