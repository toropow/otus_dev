TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:password@localhost:5432/demo"},
    "apps": {
        "models": {
            "models": ["aerich.models", "models"],
            "default_connection": "default",
        },
    },
}