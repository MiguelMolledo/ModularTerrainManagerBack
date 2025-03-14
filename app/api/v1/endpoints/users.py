from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut
from fastapi import status

router = APIRouter()


@router.get("/all")
async def read_users():
    return [{"name": "MiguelMolledo"}, {"name": "MiguelJunior"}]


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_create: UserCreate, db=None, user=None) -> UserOut:

    newUser = UserOut(name=user_create.name, email=user_create.email, id=1)

    return newUser


# @router.post(
#     "/",
# )
# def create_user(name: str, email: str) -> UserCreate:
#     return {"name": name, "email": email}
