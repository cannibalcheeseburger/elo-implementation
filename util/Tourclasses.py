from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class TournamentTeams(Base):
    __tablename__ = 'TournamentTeams'
    id = Column(Integer(),primary_key=True)
    discord = Column(String(80),nullable=False)
    name = Column(String(25),nullable=False)
    TeamName = Column(String(25))
    number = Column(Integer())
    rank = Column(String(25))
    Member1 = Column(String(40),nullable=False)
    Member2 = Column(String(40),nullable=False)
    Member3 = Column(String(40),nullable=False)
    Member4 = Column(String(40),nullable=False)
    Member5 = Column(String(40),nullable=False)
    Substitute1 = Column(String(40))
    Substitute2 = Column(String(40))

    def __repr__(self):
        return f"""<TournamentTeams username={self.discord} name={self.name}
        TeamName= {self.TeamName} number = {self.number} 
        rank = {self.rank} Member1={self.Member1} Member2={self.Member2}
        Member3={self.Member3} Member4={self.Member4} Member5={self.Member5}
        Substitute1={self.Member1} Substitute2={self.Substitute2}>     
        """


class Q1(Base):
    __tablename__ = 'Q1'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1score = Column(Integer,nullable=False)
    team2score = Column(Integer,nullable=False)

    def __repr__(self):
        return f"""<Q1 team1= {self.team1} team2= {self.team2} time = {self.time} 
        date = {self.date} team1score={self.team1score} team2score={self.team2score}>     
        """


class Q2(Base):
    __tablename__ = 'Q2'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1score = Column(Integer,nullable=False)
    team2score = Column(Integer,nullable=False)

    def __repr__(self):
        return f"""<Q2 team1= {self.team1} team2= {self.team2} time = {self.time} 
        date = {self.date} team1score={self.team1score} team2score={self.team2score}>     
        """


class Q3(Base):
    __tablename__ = 'Q3'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1score = Column(Integer,nullable=False)
    team2score = Column(Integer,nullable=False)

    def __repr__(self):
        return f"""<Q3 team1= {self.team1} team2= {self.team2} time = {self.time} 
        date = {self.date} team1score={self.team1score} team2score={self.team2score}>     
        """


class QuarterFinals(Base):
    __tablename__ = 'QuarterFinals'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1score = Column(Integer,nullable=False)
    team2score = Column(Integer,nullable=False)

    def __repr__(self):
        return f"""<QuarterFinals team1= {self.team1} team2= {self.team2} time = {self.time} 
        date = {self.date} team1score={self.team1score} team2score={self.team2score}>     
        """


class SemiFinals(Base):
    __tablename__ = 'SemiFinals'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1map1 = Column(Integer,nullable=False)
    team2map1 = Column(Integer,nullable=False)
    team1map2 = Column(Integer,nullable=False)
    team2map2 = Column(Integer,nullable=False)    
    team1map3 = Column(Integer,nullable=False)
    team2map3 = Column(Integer,nullable=False)
    def __repr__(self):
        return f"""<SemiFinals team1= {self.team1} team2= {self.team2} >
        """


class Finals(Base):
    __tablename__ = 'Finals'
    id = Column(Integer(),primary_key=True)
    team1 = Column(String(80),nullable=False)
    team2 = Column(String(80),nullable=False)
    team1map1 = Column(Integer,nullable=False)
    team2map1 = Column(Integer,nullable=False)
    team1map2 = Column(Integer,nullable=False)
    team2map2 = Column(Integer,nullable=False)    
    team1map3 = Column(Integer,nullable=False)
    team2map3 = Column(Integer,nullable=False)
    team1map4 = Column(Integer,nullable=False)
    team2map4 = Column(Integer,nullable=False)    
    team1map5 = Column(Integer,nullable=False)
    team2map5 = Column(Integer,nullable=False)
    def __repr__(self):
        return f"""<Finals team1= {self.team1} team2= {self.team2} >
        """
