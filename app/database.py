from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Configuracoes(BaseSettings):
    db_user: str = "root"
    db_password: str = ""
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "biblioteca_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


configuracoes = Configuracoes()

DATABASE_URL = (
    f"mysql+pymysql://{configuracoes.db_user}:{quote_plus(configuracoes.db_password)}"
    f"@{configuracoes.db_host}:{configuracoes.db_port}/{configuracoes.db_name}"
)

mecanismo_banco = create_engine(DATABASE_URL, pool_pre_ping=True)
criar_sessao = sessionmaker(bind=mecanismo_banco, autoflush=False, autocommit=False)


class BaseBanco(DeclarativeBase):
    pass