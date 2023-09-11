from fastapi import APIRouter
from fastapi_sqlalchemy import db
# from models.models import Relations_en_ja_noun
# import logging
from sqlalchemy.sql import text
 
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

router = APIRouter()

@router.get("")
@router.get("/")
async def Test():
    # test = db.session.query(Corpus_en_ja).filter(Corpus_en_ja.id == 1).first()
    # return test
    return {"message": "Hello World"}


@router.get("/discord")
@router.get("/discord/")
async def discord():
    return "test"


@router.get("/keep_active")
@router.get("/keep_active/")
async def keep_active():
    return "test"