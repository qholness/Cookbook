from CookingCompendium.Techniques.Base import Base


class TestTechnique(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(technique_name="Test Technique", *args, **kwargs)
