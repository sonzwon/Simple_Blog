import os
import csv
from post import Post

# 파일 경로
file_path = "./Simple_Blog/Blogvenv/data.csv"

post_list = []
# data.csv 파일이 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("loading...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # data.csv파일 없으면 파일 생성
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

# 게시물 작성
def write_post():
    """
    게시글 작성 함수
    """