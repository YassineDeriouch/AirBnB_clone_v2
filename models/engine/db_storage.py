from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

class DBStorage:
    """
    This class manages the database storage using SQLAlchemy.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a new instance of DBStorage.
        """
        """ Retrieve MySQL database connection information from environment variables """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        """ Create the SQLAlchemy engine with the provided information """
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True)

        """ Drop all tables if HBNB_ENV is 'test' """
        if os.getenv("HBNB_ENV") == "test":
            self.__engine.echo = True
            Base.metadata.drop_all(self.__engine)
            self.__engine.echo = False

        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)

        """ Create a session factory """
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """
        Query all objects from the current database session.

        Args:
            cls (class): The class of objects to query (default: None).

        Returns:
            dict: A dictionary containing all queried objects.
        """
        from models import classes

        result = {}
        if cls:
            query = self.__session.query(classes[cls])
            for obj in query.all():
                key = f"{cls}.{obj.id}"
                result[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls)
                for obj in query.all():
                    key = f"{cls.__name__}.{obj.id}"
                    result[key] = obj

        return result

    def new(self, obj):
        """
        Add the object to the current database session.

        Args:
            obj: The object to add.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete the object from the current database session.

        Args:
            obj: The object to delete (default: None).
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload the current database session.
        """
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

