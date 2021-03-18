from models.base import Base


class Family(Base):
    def __init__(self, entries=None):
        if entries:
            Base.__init__(self, entries)
            return
        self.id = 0
        self.created_by = 0
        self.created_on = ''
        self.surname = ''
        self.name = ''
        self.area = ''
        self.tanghao = ''
        self.description = ''
        self.members = []
        self.admins = []
        self.relations = []