import json

POST_PATH = "/Users/macos/PycharmProjects/lesson12_project_source_v3/posts.json"


def load_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts
