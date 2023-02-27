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

# 게시글 목록
id_list = []
def list_post():
    """게시글 목록 함수"""
    print("\n\n[[ 게시글 목록 ]]")
    for post in post_list:
        print(f"No. : {post.get_id()}")
        print(f"제목 : {post.get_title()}")
        print(f"조회수 : {post.get_view_count()}")
        print("")
        id_list.append(post.get_id())
    
    while True:
        print(">>> 게시글 번호를 선택해주세요")
        try:
            id = int(input("글 번호 : "))
            if id in id_list:
                print(f"\n\n>>> {id}번 게시글")
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다!")
        except ValueError:
            print("숫자를 입력해주세요!")

# 게시글 상세보기
def detail_post(id):
    """게시글 상세보기 함수"""
    print("\n[[ 상세보기 ]]")
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print(f"No. : {post.get_id()}")
            print(f"제목 : {post.get_title()}")
            print(f"내용 : {post.get_content()}")
            print(f"조회수 : {post.get_view_count()}")
    
    while True:
        print("\n수정하려면 1, 삭제하려면 2를 눌러주세요")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                print("수정")
                break
            elif choice == 2:
                print("삭제되었습니다")
                break
            elif choice == -1:
                break
            else: 
                print("잘못 입력하셨습니다")
        except ValueError:
            print("숫자를 입력해주세요")

# 게시글 작성
def write_post():
    """게시글 작성 함수"""
    print("\n\n[[ 게시글 작성 ]]")
    title = input("제목 : ")
    content = input("내용 : ")
    # 글 번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content)
    post_list.append(post)
    print("\n 게시글 등록 완료")

# 메뉴 출력
while True:
    print("\n\n-- Jiwon's Blog --")
    print("메뉴를 선택해주세요")
    print("1. 게시글 작성")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해주세요")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("프로그램 종료")
            break