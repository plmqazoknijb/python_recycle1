#분리수거 물품을 추가하는 클래스
class Recycle:
    def __init__(self,name):
        #이름
        self.name = name
        #카테고리
        self.category = ''
        #설명
        self.info = ''
        #영상
        self.link = ''
        #카테고리
        self.r_category_list = ['플라스틱', '종이', '종이팩', '캔', '비닐', '페트','유리', '일반쓰레기']

    def set_category(self):
        category = input('>> 카테고리를 입력해주세요: ')
        if category in self.r_category_list:
            self.category=category
        else:
            print('카테고리가 존재하지 않습니다.')

    def set_info(self):
        info = input('>> 분리수거 방법을 입력해주세요: ')
        self.info = info

    def set_link(self):
        link = input('>> 레시피 영상 주소를 입력하세요(링크)')
        self.link='입력된 주소가 없습니다.' if link == ''else link


    def set_recycle(self):
        self.set_category()
        self.set_info()
        self.set_link()

    def __str__(self):
        return f'품목 : {self.name}\n카테고리 : {self.category}\n방법 : {self.info}\n영상 : {self.link}'