# DAR-SYS - The Dual-Axis Rating System 

# What is this?

Dar-sys ("Darcys") is intended to be a solution to the problem of communicating
the distinction between "good" and "enjoyable" media. The idea stems from a
conversation with a close friend (credit incoming) who wanted a way to
efficiently show that a show is enjoyable without having to specifiy that it
isn't a cinematic masterpiece. Obviously this can also go the other way, with
some shows being cinematic masterpieces that are subjectively, boring!

# Requirements

Store users in some manner
Allow querying for community opinion
Allow querying for personal opinion 
Be highly available 
Take advantage of some tech I want to work with:
    - PostgreSQL - DB
    - MiniKube - Orchestration
    - AWS - Hosting
    - OAuth - API Authentication 
    - FastAPI - Spinning up yonder API
    - SQLAlchemy - concurrency hard, sqlalchemy ez
