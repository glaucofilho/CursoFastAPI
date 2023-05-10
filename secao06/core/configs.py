from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    '''
    Configuracoes gerais usadas na aplicacao
    '''
    API_V1_STR: str = '/api/v1'
    
    DB_URL: str = 'postgresql+asyncpg://sa:1234@localhost:5432/banco'
    
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = '5GblT97MnsUvbQzREdqLIBv5n-q4CH7VB9YruL-sjt8'
    '''
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'
    
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()