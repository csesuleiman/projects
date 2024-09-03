from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "post 1 title", 
        "content": "This content is for post 1", 
        "id": 1
    }, 
    {
        "title": "post 2 title",
        "content": "This content belongs to post 2",
        "id": 2
    }
]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
    

@app.get("/")
def home():
    return {"meesage": "Welcome once again to python fastapi course"}


# @app.post("/createpost")
# def create_posts(payload: dict = Body(...)):
#     # print (payload)
#     return {"New post":f"title {payload['title']} content {payload['content']}"}

@app.get("/posts")
def posts():
    # return {"post": "This is what you posted"}
    return {"data": my_posts}


# @app.post("/posts")
# def create_post(post: Post):
#     # print (post)
#     # print (post.model_dump())
#     return {"data": post}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(3, 1000000)
    my_posts.append(post_dict)
    return (post_dict)


@app.get("/posts/{id}")
def get_one_post(id: int):
    post = find_post(id)
    return {"post detail": post}
