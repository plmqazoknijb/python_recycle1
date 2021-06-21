from recycle import Recycle
from foodwaste import Foodwast
class Garbagebook:
    def __init__(self):
        self.recycle_list = []
        self.foodwast_list = []
        self.recycle_court()
        self.foodwast_court()

    def add_recycle(self):
        # 추가할 쓰레기 입력
        recycle_name = input('>> 추가할 물품명을 입력하세요: ')
        # 중복을 체크
        for recycle in self.recycle_list:
        # 중복되는 물품이 있으면
            if recycle_name == recycle.name:
            #있다고 알려주기
                print('이미 존재하는 물품입니다.')
                return
        # 중복되는 물품이 없으면
        #물품을 새롭게 만들자
        new_recycle = Recycle(recycle_name)
        new_recycle.set_recycle()
        #추가한 물품 보여주기
        print(new_recycle)
        choice = input('위 정보로 추가 하시겠습니까? (1:예 0:아니오): ')
        if choice == '1':
            #리스트에 추가
            self.recycle_list.append(new_recycle)
        # 추가 안 한다고 하면
        else:
            # 끝
            return

    def add_foodwast(self):
        # 추가할 쓰레기 입력
        foodwast_name = input('>> 추가할 물품명을 입력하세요: ')
        # 중복을 체크
        for foodwast in self.foodwast_list:
        # 중복되는 물품이 있으면
            if foodwast_name == foodwast.name:
            #있다고 알려주기
                print('이미 존재하는 쓰레기입니다.')
                return
        # 중복되는 물품이 없으면
        #물품을 새롭게 만들자
        new_foodwast = Foodwast(foodwast_name)
        new_foodwast.set_foodwast()
        print(new_foodwast)
        choice = input('위 정보로 추가 하시겠습니까? (1:예 0:아니오): ')
        if choice == '1':
            # 리스트에 추가
            self.foodwast_list.append(new_foodwast)
        # 추가 안 한다고 하면
        else:
            # 끝
            return

    def show_all_recycle(self):
        for index,recycle in enumerate(self.recycle_list):
            print(f'\n{index+1}번.')
            print(recycle)

    def show_all_foodwast(self):
        for index,foodwast in enumerate(self.foodwast_list):
            print(f'\n{index+1}번.')
            print(foodwast)

    def search_recycle(self):
        # 찾을 물품명을 입력받기
        recycle_name = input('>> 검색할 물품명을 입력하세요: ')
        searched_recycle = []
        for recycle in self.recycle_list:
            #찾는 물품이 리스트에 있을 때
            if recycle_name in recycle.name:
                #물품을 보여주자
                print(recycle)
                searched_recycle.append(recycle)
        # 찾는 물품이 리스트에 없다면
        if len(searched_recycle) == 0:   # 못찾음
            # 추가할건지 물어보자
            choice = input('>> 찾으시는 물품이 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오)')
            # 추가한다고 하면
            if choice == '1':
                # 물품 추가
                self.add_recycle()
            # 추가 안 한다고 하면
            else:
                # 끝
                return

    def search_foodwast(self):
        # 찾을 물품명을 입력받기
        foodwast_name = input('>> 검색할 물품명을 입력하세요: ')
        searched_foodwast = []
        for foodwast in self.foodwast_list:
            #찾는 물품이 리스트에 있을 때
            if foodwast_name in foodwast.name:
                #물품을 보여주자
                print(foodwast)
                searched_foodwast.append(foodwast)
        # 찾는 물품이 리스트에 없다면
        if len(searched_foodwast) == 0:   # 못찾음
            # 추가할건지 물어보자
            choice = input('>> 찾으시는 물품이 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오)')
            # 추가한다고 하면
            if choice == '1':
                # 물품 추가
                self.add_foodwast()
            # 추가 안 한다고 하면
            else:
                # 끝
                return

    def recycle_court(self):
        페트병 = Recycle('페트병')
        페트병.category = '페트'
        페트병.info = '뚜껑은 플라스틱, 라벨은 비닐, 몸통은 페트로 분리해서 버린다. (세척 후 건조필수)'
        페트병.link = 'https://youtu.be/rJYUyfyV52I'
        self.recycle_list.append(페트병)

        우유팩 = Recycle('우유팩')
        우유팩.category = '종이팩'
        우유팩.info = '종이가 아닌 종이팩으로 따로 분리 (세척 후 건조필수)'
        우유팩.link ='https://youtu.be/xrHWHCjYumQ'+' (2:05 부터 보시면 바로 보실 수 있습니다.)'
        self.recycle_list.append(우유팩)

        과자봉지 = Recycle('과장봉지')
        과자봉지.category = '비닐'
        과자봉지.info = '과자봉지는 묻어있는 내용물과 기름을 모두 휴지로 닦은후에 잘접어서 비닐로 분리해서 버린다.(딱지접기 X)'
        과자봉지.link = 'https://youtu.be/FafK0E9ByVs'+'(1:45 부터 보시면 바로 보실 수 있습니다.)'
        self.recycle_list.append(과자봉지)

        깨진유리 = Recycle('깨진유리')
        깨진유리.category = '일반쓰레기'
        깨진유리.info = '깨진유리는 분리수거 불가능 하여 종량제 봉투에 넣어 일반쓰레기로 분리해서 버린다.'
        깨진유리.link = 'https://youtu.be/T1WV89Tk7L4' + '(0:15 부터 보시면 바로 보실 수 있습니다.)'
        self.recycle_list.append(깨진유리)

        스팸통= Recycle('스팸통 ')
        스팸통.category = '캔'
        스팸통.info = '스팸 통은 캔에 분리배출하고 뚜껑이 플라스틱은 플라스틱에 분비해서 버린다.'
        스팸통.link = 'https://youtu.be/E70KV-H1hWw' + '(1:33 부터 보시면 바로 보실 수 있습니다.)'
        self.recycle_list.append(스팸통)

    def foodwast_court(self):
        #일반쓰레기 (달걀, 양파, 마늘, 옥수수, 고추)
        달걀 = Foodwast('달걀 껍질')
        달걀.category = '일반쓰레기'
        달걀.info = '삶은달걀과 날달걀 상관없이 껍질은 일반쓰레기로 버린다.'
        달걀.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:52 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(달걀)

        양파 = Foodwast('양파 껍질')
        양파.category = '일반쓰레기'
        양파.info = '양파의 내용물은 음식물쓰레기로 분리되지만 껍질은 일반쓰레기로 분리된다.'
        양파.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:42 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(양파)

        마늘 = Foodwast('마늘 껍질')
        마늘.category = '일반쓰레기'
        마늘.info = '마늘의 내용물은 음식물쓰레기로 분리되지만 껍질은 일반쓰레기로 분리된다.'
        마늘.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:42 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(마늘)

        옥수수 = Foodwast('옥수수대와껍질')
        옥수수.category = '일반쓰레기'
        옥수수.info = '옥수수는 알맹이를 제외하고는 모두 일반쓰레기로 분리된다.'
        옥수수.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:42 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(옥수수)

        고추 = Foodwast('고추꼭지와씨')
        고추.category = '일반쓰레기'
        고추.info = '고추는 꼭지와 씨만 일반쓰레기로 분리된다.'
        고추.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:42 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(고추)

        #음식물 쓰레기( 귤, 바나나, 수박, 멜론, 고구마 )
        귤 = Foodwast('귤껍질')
        귤.category = '음식물 쓰레기'
        귤.info = '수분이 있고 부드러운 과일의 껍질은 음식물 쓰레기로 분류된다.'
        귤.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:16 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(귤)

        바나나 = Foodwast('바나나껍질')
        바나나.category ='음식물 쓰레기'
        바나나.info = '수분이 있고 부드러운 과일의 껍질은 음식물 쓰레기로 분류된다.'
        바나나.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:34 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(바나나)

        수박 = Foodwast('수박껍질')
        수박.category = '음식물 쓰레기'
        수박.info = '수분이 있고 부드러운 과일의 껍질은 음식물 쓰레기로 분류된다.'
        수박.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:34 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(수박)

        멜론 = Foodwast('멜론껍질')
        멜론.category = '음식물 쓰레기'
        멜론.info = '수분이 있고 부드러운 과일의 껍질은 음식물 쓰레기로 분류된다.'
        멜론.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:34 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(멜론)

        고구마 = Foodwast('고구마껍질')
        고구마.category = '음식물 쓰레기'
        고구마.info = '수분이 있고 부드러운 과일의 껍질은 음식물 쓰레기로 분류된다.'
        고구마.link = 'https://youtu.be/ChdRCscKGZ8'+'(0:35 부터 보시면 바로 보실 수 있습니다.)'
        self.foodwast_list.append(고구마)


    def __str__(self):
        pass
