"Social Media Platform"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []

    def post(self,content):
        self.posts.append(content)
        print(f"{self.username} posted: {content}")
    def comment(self,content):
        print(f"{self.username} commented: {content}")
class Admin(User):
    def delete_post(self, user, post):
        if post in user.posts:
            user.posts.remove(post)
            print(f"Admin {self.username} deleted post: {post}")
        else:
            print("Post not found.")


def main():
    user = User("john_doe", "john@example.com")
    admin = Admin("admin01", "admin@example.com")

    user.post("Hello, world!")
    user.comment("Nice to meet you all!")

    admin.delete_post(user, "Hello, world!")
    admin.delete_post(user, "Non-existent post")


if __name__ == "__main__":
    main()

