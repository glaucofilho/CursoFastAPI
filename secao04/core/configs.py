from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    '''
    Configuracoes gerais usadas na aplicacao
    '''
    API_V1_STR: str = '/api/v1'
    
    DB_URL: str = 'postgresql+asyncpg://sa:1234@localhost:5432/banco'
    
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings = Settings()