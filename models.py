from app import db
from sqlalchemy_utils import ColorType


class Issue(db.Model):
	__abstract__ = True
	id = db.Column(db.INTEGER, primary_key=True)
	title = db.Column(db.String, unique=True)


class Chapter(Issue):
	parent = db.Column(db.INTEGER, db.ForeignKey("chapter.id"), nullable=True)
	children = db.relationship("Issue", backref='chapter', lazy=True)

	def __init__(self, title, parent=None):
		self.title = title
		if parent is not None:
			self.parent = parent

	def __repr__(self):
		return '<Chapter {}>'.format(self.id)

	def serialise(self):
		return {
			'id': self.id,
			'parent': self.parent,
			'title': self.title
			}


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                db.Column('paper_id', db.Integer, db.ForeignKey('paper.id'), primary_key=True)
                )


class Paper(Issue):
	parent = db.Column(db.INTEGER, db.ForeignKey("chapter.id"), nullable=False)
	content = db.Column(db.TEXT)
	tags = db.relationship('Tag', secondary=tags, lazy='subquery',
	                       backref=db.backref('papers', lazy=True))

	def __init__(self, title, parent, content):
		self.title = title
		self.parent = parent
		self.content = content

	def __repr__(self):
		return '<Paper {}>'.format(self.id)

	def serialise(self):
		return {
			'id': self.id,
			'parent': self.parent,
			'title': self.title,
			'content': self.content
			}


class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)
	color = db.Column(ColorType)

	def __init__(self, name, color):
		self.name = name
		self.color = color

	def __repr__(self):
		return '<Tag {}>'.format(self.id)

	def serialise(self):
		return {
			'id': self.id,
			'name': self.name,
			'color': self.color
			}
