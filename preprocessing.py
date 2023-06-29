#-*- coding:utf-8 -*-
import json
import os
import shutil
from importlib import reload
from pathlib import Path
dir_path = os.getcwd() + "/dataset/라벨링데이터"
save_path = os.getcwd() +'/result'
# print(dir_path)
# print(os.path.isdir(dir_path))
region_list = ['seoul','daejeon','gyeonggi','daegu','busan','ulsan','gwangju','incheon']
dataset_category_list = ['train','valid','test']
test_target = ['20221025','20221026','20221027','20221028','20221029','20221030','20221031','202211']
def preprocessing():
    if not os.path.isdir(dir_path):
        print('프로젝트 경로 ' + os.getcwd() + '/dataset/ 에서' + '"라벨링데이터" 폴더를 찾을 수 없습니다.')
    else:
        print('프로젝트 경로 ' + os.getcwd() + '/dataset/ 에서' + '"라벨링데이터" 폴더를 찾았습니다.')
        for folder in os.listdir(save_path + '/'):

            if os.path.isfile(save_path + '/' + folder):
                print('프로젝트 경로 ' + save_path + '/' + '에 존재하는 파일"' + folder + '"를 삭제합니다.')
                os.remove(save_path + '/' + folder)
                print('프로젝트 경로 ' + save_path + '/' + '에 존재하는 파일"' + folder + '"를 삭제하였습니다.')
            if os.path.isdir(save_path + '/' + folder):
                print('프로젝트 경로 ' + save_path + '/' + '에 존재하는 폴더"' + folder + '"를 삭제합니다.')
                shutil.rmtree(save_path + '/' + folder)
                print('프로젝트 경로 ' + save_path + '/' + '에 존재하는 폴더"' + folder + '"를 삭제하였습니다.')
        for region in region_list:
            print('프로젝트 경로 ' + save_path + '/' + '에 "' + region + '"지역 폴더를 생성합니다.')
            os.makedirs(save_path + '/total/' + region + '/07')
            os.makedirs(save_path + '/total/' + region + '/08')
            os.makedirs(save_path + '/total/' + region + '/09')
            os.makedirs(save_path + '/total/' + region + '/10')
            os.makedirs(save_path + '/total/' + region + '/11')
            os.makedirs(save_path + '/test/' + region + '/10')
            os.makedirs(save_path + '/test/' + region + '/11')
            print('프로젝트 경로 ' + save_path + '/' + '에 "' + region + '"지역 폴더를 생성하였습니다.')
        for month in os.listdir(dir_path + '/'):
            print(month + '월 데이터를 탐색합니다.')
            file_list = os.listdir(dir_path + '/' + month)
            for file in file_list:
                with open(dir_path + '/' + month + '/' + file, 'rt', encoding='UTF8') as st_json:
                    print('원본 데이터 위치 : ', dir_path + '/' + month + '/' + file)
                    origin_data = json.load(st_json)
                    print('원본 데이터 내용 : ', origin_data)
                if '서울' in file:
                    with open(save_path + '/total/' + 'seoul/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'seoul/' + month+ '/' + file)
                elif '대전' in file:
                    with open(save_path + '/total/' + 'daejeon/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'daejeon/' + month+ '/' + file)
                elif '경기' in file:
                    with open(save_path + '/total/' + 'gyeonggi/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'gyeonggi/' + month+ '/' + file)
                elif '대구' in file:
                    with open(save_path + '/total/' + 'daegu/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'daegu/' + month+ '/' + file)
                elif '부산' in file:
                    with open(save_path + '/total/' + 'busan/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'busan/' + month+ '/' + file)
                elif '울산' in file:
                    with open(save_path + '/total/' + 'ulsan/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'ulsan/' + month+ '/' + file)
                elif '광주' in file:
                    with open(save_path + '/total/' + 'gwangju/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'gwangju/' + month+ '/' + file)
                elif '인천' in file:
                    with open(save_path + '/total/' + 'incheon/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                        json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                        print('저장 대상 경로 : ', save_path + '/total/' + 'incheon/' + month+ '/' + file)
                else:
                    print('파일명 ' + dir_path + '/' + month + '/' + file + '은 8개 도시에 포함되지 않습니다.')

            if month == '10' or month == '11':
                for file in file_list:
                    split_file_name = file.split('_')
                    data = split_file_name[1]
                    for tg in test_target:
                        if data.startswith(tg):
                            with open(dir_path + '/' + month + '/' + file, 'rt', encoding='UTF8') as st_json:
                                print('원본 테스트 데이터 위치 : ', dir_path + '/' + month + '/' + file)
                                origin_data = json.load(st_json)
                                print('원본 테스트 데이터 내용 : ', origin_data)
                            if '서울' in file:
                                with open(save_path + '/test/' + 'seoul/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'seoul/' + month+ '/' + file)
                            elif '대전' in file:
                                with open(save_path + '/test/' + 'daejeon/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'daejeon/' + month+ '/' + file)
                            elif '경기' in file:
                                with open(save_path + '/test/' + 'gyeonggi/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'gyeonggi/' + month+ '/' + file)
                            elif '대구' in file:
                                with open(save_path + '/test/' + 'daegu/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'daegu/' + month+ '/' + file)
                            elif '부산' in file:
                                with open(save_path + '/test/' + 'busan/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'busan/' + month+ '/' + file)
                            elif '울산' in file:
                                with open(save_path + '/test/' + 'ulsan/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'ulsan/' + month+ '/' + file)
                            elif '광주' in file:
                                with open(save_path + '/test/' + 'gwangju/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'gwangju/' + month+ '/' + file)
                            elif '인천' in file:
                                with open(save_path + '/test/' + 'incheon/' + month+ '/' + file, 'w', encoding='UTF8') as make_file:
                                    json.dump(origin_data, make_file, indent=4, ensure_ascii=False)
                                    print('테스트 데이터 저장 대상 경로 : ', save_path + '/test/' + 'incheon/' + month+ '/' + file)
                            else:
                                print('테스트 데이터 파일명 ' + dir_path + '/' + month + '/' + file + '은 8개 도시에 포함되지 않습니다.')


