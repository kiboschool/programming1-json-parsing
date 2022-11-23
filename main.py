import json

FILENAME = "posts.json"

def count_posts(posts):
    return len(posts)

def count_posts_by_user(posts):
    user_counts = {}
    for post in posts:
        user_counts[post["userId"]] = user_counts.get(post["userId"], 0) + 1
    return user_counts

def longest_body(posts):
    max_len = 0
    for post in posts:
        if len(post["body"]) > max_len:
            max_len = len(post["body"])
    return max_len

def average_title_length(posts):
    total = 0
    for post in posts:
        total += len(post["title"])
    return total / len(posts)

def analyze(posts):
    return {
        "count": count_posts(posts),
        "by_user": count_posts_by_user(posts),
        "longest": longest_body(posts),
        "average_title": average_title_length(posts)
    }

def main():
    with open(FILENAME, "r") as post_file:
        posts = json.load(post_file)
        print(json.dumps(analyze(posts)))

if __name__ == "__main__":
    main()
