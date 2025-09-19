from pydantic import BaseModel


class BaseRetsept(BaseModel):
    name:str
    description:str
    masalliqlar:str


class CreateRetsept(BaseRetsept):
    pass

class UpdateRetsept(BaseRetsept):
    pass
class RetseptResponse(BaseRetsept):
    id:int
