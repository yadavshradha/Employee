from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session


DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/account")
def create_account(id: int, name: str, balance: float, db: Session = Depends(get_db)):
    account = Account(id=id, name=name, balance=balance)
    db.add(account)
    db.commit()
    return {
        "message": "Account Created Successfully",
        "account": {"id": id, "name": name, "balance": balance}
    }

@app.get("/account")
def get_accounts(db: Session = Depends(get_db)):
    return db.query(Account).all()

@app.get("/account/{id}")
def search_account(id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == id).first()
    if account:
        return account
    return {"message": "Account Not Found"}

@app.put("/account/{id}")
def update_account(id: int, name: str, balance: float, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == id).first()
    if account:
        account.name = name
        account.balance = balance
        db.commit()
        return {
            "message": "Account Updated Successfully",
            "account": {"id": id, "name": name, "balance": balance}
        }
    return {"message": "Account Not Found"}

@app.delete("/account/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == id).first()
    if account:
        db.delete(account)
        db.commit()
        return {"message": "Account Deleted Successfully"}
    return {"message": "Account Not Found"}
