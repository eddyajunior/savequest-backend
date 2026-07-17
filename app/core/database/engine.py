from sqlalchemy import Engine, create_engine
from sqlalchemy.pool import StaticPool

from app.core.config import Settings, get_settings


def create_database_engine(
    settings: Settings | None = None,
) -> Engine:
    current_settings = settings or get_settings()

    engine_options: dict[str, object] = {
        "echo": current_settings.database_echo,
        "pool_pre_ping": True,
    }

    if current_settings.database_url.startswith(
        "sqlite",
    ):
        engine_options.update(
            {
                "connect_args": {
                    "check_same_thread": False,
                },
                "poolclass": StaticPool,
            },
        )
    else:
        engine_options.update(
            {
                "pool_size": current_settings.database_pool_size,
                "max_overflow": (current_settings.database_max_overflow),
                "pool_timeout": (current_settings.database_pool_timeout),
                "pool_recycle": (current_settings.database_pool_recycle),
            },
        )

    return create_engine(
        current_settings.database_url,
        **engine_options,
    )


engine = create_database_engine()
