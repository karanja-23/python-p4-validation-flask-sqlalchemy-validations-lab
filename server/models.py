from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Name is required')
        
        for author in Author.query.all():
            if name == author.name:
                raise ValueError('Name must be unique')
        return name
    @validates('phone_number')
    def validates_phone_number(self, key, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError('Phone numbers should have 10 digits')
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def validates_content(self, key, content):
        if not isinstance(content,str) or len(content) > 250 :
            raise ValueError("Post content is at least 250 characters long")

    @validates('summary')
    def validates_summary(self, key, content):
        if not isinstance(content,str) or len(content) > 250 :
            raise ValueError("Post content is at least 250 characters long")   
    @validates('category')
    def validates_category(self, key, category):
        if category not in ['Fiction', 'Non-Fiction']:
            raise ValueError(' category is either Fiction or Non-Fiction')  
@validates('title')
def validates_title(self, key, title):
    keywords =  ["Won't Believe", "Secret", "Top", "Guess"]
    if not isinstance(title, str) or not any(keyword in title for keyword in keywords):
        raise ValueError('Title must contain one of the following: "Won\'t Believe", "Secret", "Top", "Guess"')
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
