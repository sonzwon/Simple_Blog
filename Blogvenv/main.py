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


# 게시글 작성
def write_post():
    """게시글 작성 함수"""
    print("\n\n[[ 게시글 작성 ]]\n")
    title = input("제목 : ")
    content = input("내용 : ")
    # 글 번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content)
    post_list.append(post)
    save_post()
    print("\n## 작성이 완료되었습니다")



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
        print("\n원하시는 게시글 번호를 선택해주세요")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("\n없는 글 번호 입니다")
        except ValueError:
            print("\n숫자를 입력해주세요")


# 게시글 상세보기
def detail_post(id):
    """게시글 상세보기 함수"""
    print("\n\n[[ 게시글 상세 ]]")
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print(f"No. {post.get_id()}")
            print(f"제목 : {post.get_title()}")
            print(f"내용 : {post.get_content()}")
            print(f"조회수 : {post.get_view_count()}")
            target_post = post
    
    while True:
        print("\n------Press------")
        print("수정 : 1\n삭제 : 2\n뒤로가기 : -1")
        print("-----------------")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else: 
                print("잘못 입력하셨습니다")
        except ValueError:
            print("숫자를 입력해주세요")


# 게시글 수정
def update_post(target_post):
    """게시글 수정 함수"""
    print("\n\n[[ 게시글 수정 ]]")
    title = input("제목 : ")
    content = input("내용 : ")
    post = target_post.set_post(target_post.id, title, content, target_post.view_count)
    save_post()
    print("\n## 수정이 완료되었습니다")


# 게시글 삭제
def delete_post(target_post):
    """게시글 삭제 함수"""
    post_list.remove(target_post)
    print("\n## 삭제가 완료되었습니다")
    

# 게시글 저장
def save_post():
    """게시글 저장 함수"""
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("\n## 파일 저장 완료")

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