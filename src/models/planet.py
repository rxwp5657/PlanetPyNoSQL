from mongoengine import Document, StringField, FloatField, ValidationError

class Planet(Document):
    name = StringField(primary_key=True)
    orbital_speed = FloatField()
    circumference = FloatField()

    def clean(self):
        """ Ensuers that the Planet has a name before trying to insert it """
        if not self.name :
            raise ValidationError("Planet should have a name")