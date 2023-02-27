class Post:
    """
    -- 게시물 클래스 --
    param id : 글 번호
    param title : 글 제목
    param content : 글 내용
    param view_count : 조회수
    """

    def __init__(self, id, title, content, view_count=0):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    # 게시글 수정 함수
    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    # 조회수 증가 함수
    def add_view_count(self):
        self.view_count += 1

    # 글 번호 추출
    def get_id(self):
        return self.id

    # 글 제목 추출
    def get_title(self):
        return self.title
    
    # 글 내용 추출
    def get_content(self):
        return self.content
    
    # 조회수 추출
    def get_view_count(self):
        return self.view_count
    

# TEST
if __name__ == "__main__":
    post = Post(1, "test1", "테스트입니다")
    post.add_view_count()
    print(f"글 번호 : {post.get_id()}\n글 제목 : {post.get_title()}\n글 내용 : {post.get_content()}\n조회수 : {post.get_view_count()}")