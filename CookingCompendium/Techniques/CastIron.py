from CookingCompendium.Techniques.Base import Base


class CastIron(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(technique_name="Cast Iron", *args, **kwargs)
