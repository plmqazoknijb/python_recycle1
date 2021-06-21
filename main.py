from garbagebook import Garbagebook
def print_menu():
    category_list = ['\n★★[카테고리:','플라스틱,', '종이,', '종이팩,', '캔,', '비닐,', '페트,','유리,', '음식물,', '일반]★★']
    for i in range(len(category_list)):
        print(category_list[i], end=' ')

    print('\n1. 분리수거 검색')
    print('2. 음식물 쓰레기 검색')
    print('3. 분리수거 물품 추가')
    print('4. 음식물 쓰레기 추가')
    print('5. 분리수거 품목 모음')
    print('6. 음식물 쓰레기 품목 모음')
    print('7. 종료')
    menu = input('>>메뉴를 선택하세요:')
    return menu

def main():
    garbagebook_main = Garbagebook()
    while True:
        menu = print_menu()
        # 분리수거 검색
        if menu == '1':
            garbagebook_main.search_recycle()
        # 음식물 쓰레기 검색
        elif menu == '2':
            garbagebook_main.search_foodwast()
        #분리수거 물품 추가
        elif menu == '3':
            garbagebook_main.add_recycle()
        # 음식물 쓰레기 추가
        elif menu =='4':
            garbagebook_main.add_foodwast()
        #분리수거 물품 보여주기
        elif menu =='5':
            garbagebook_main.show_all_recycle()
        #음식물 쓰레기 보여주기
        elif menu =='6':
            garbagebook_main.show_all_foodwast()
        #종료
        elif menu == '7':
            break
        else:
            print('다시 입력하세요:')

if __name__ == '__main__':
    main()

