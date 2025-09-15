'''
Author: wangxin
Date: 2021-05-25 10:29:58
LastEditTime: 2021-07-01 14:12:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
'''
from cnocr import CnOcr

from detection_choice_question import get_answer_card_cnts, get_sub_answer_card_cnts, detection_choice_question
from detection_exam_num import detection_exam_num
from settings import TITLE_NUM
from utils import get_init_process_img, capture_img, ocr_single_line_img
import os

if not os.path.exists('out'):
    os.makedirs('out')

def demo(origin_image_path):
    # 获取答题卡左右区域
    image = get_init_process_img(origin_image_path)
    answer_cnts = get_answer_card_cnts(image)
    answer_card_images_path = []
    if len(answer_cnts) > 0:
        len_answer_cnts = 0
        for c in answer_cnts:
            len_answer_cnts = len_answer_cnts + 1
            answer_card_image_path = 'out/answer_card_' + str(len_answer_cnts) + '.jpg'
            answer_card_images_path.append(answer_card_image_path)
            capture_img(origin_image_path, answer_card_image_path, c)
    print('答题卡左右区域切分结果：', answer_card_images_path)

    # 将答题卡切分为一道道试题
    sub_answer_card_images_path = []
    sub_answer_cnt_szie = 0
    for answer_card_image in answer_card_images_path:
        sub_answer_cnts = get_sub_answer_card_cnts(answer_card_image)
        if len(sub_answer_cnts) > 1:
            sub_answer_cnts = sub_answer_cnts[1:len(sub_answer_cnts)]

        if len(sub_answer_cnts) > 0:
            for c in sub_answer_cnts:
                sub_answer_card_image_path = 'out/sub_answer_card_' + str(sub_answer_cnt_szie) + '.jpg'
                sub_answer_card_images_path.append(sub_answer_card_image_path)
                capture_img(answer_card_image, sub_answer_card_image_path, c)
                sub_answer_cnt_szie = sub_answer_cnt_szie + 1
    print('试题切分结果：', sub_answer_card_images_path)


if __name__ == '__main__':
    demo('pic/1.png')
