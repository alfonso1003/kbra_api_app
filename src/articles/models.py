from datetime import datetime, timezone
from src import db


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now(timezone.utc), nullable=False
    )

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Article {self.title} - {self.content[0:10]}>"
