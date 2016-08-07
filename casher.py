# coding=utf-8
import pandas as pd
import random

discount_buy_2_get_1_free = {''}
discount95off = {''}


def generate_input(input_data):
    fake_input = []
    for i in range(1, 10):
        item_id = input_data['ItemId'][random.randint(0, 9)]
        num = str(random.randint(2, 5))
        fake_input.append(item_id if random.randint(0, 1) == 0 else item_id + '-' + num)
    return fake_input


def update_discount_info(input_data):
    for i in range(1, random.randint(2, 4)):
        discount95off.add(input_data['ItemId'][random.randint(0, 9)])
        discount_buy_2_get_1_free.add(input_data['ItemId'][random.randint(0, 9)])


def format_input(input_raw):
    format_dict = {}
    for one_row in input_raw:
        id_and_num = one_row.split('-')
        num = 1 if len(id_and_num) == 1 else int(id_and_num[1])
        if id_and_num[0] in format_dict:
            format_dict[id_and_num[0]] += num
        else:
            format_dict[id_and_num[0]] = num
    return format_dict


def print_check_out(input_raw):
    format_data = format_input(input_raw)
    total_price = 0
    total_saved = 0
    get_1_free_info = {}
    print "***<没钱赚商店>购物清单***"
    for one_format in format_data.iteritems():
        index = int(one_format[0][4:]) - 1
        price_per_unit = float(full_data['Price'][index])
        item_num = one_format[1]
        if one_format[0] in discount_buy_2_get_1_free:
            total_price += (item_num - item_num // 3) * price_per_unit
            total_saved += (item_num // 3) * price_per_unit
            if item_num // 3 > 0:
                get_1_free_info[full_data['Name'][index]] = str(item_num // 3) + full_data['Unit'][index]
            print "名称：" + full_data['Name'][index] + "，数量：" + str(one_format[1]) + full_data['Unit'][index] \
                  + "，单价：" + str(price_per_unit) + "(元)，小计：" + str((item_num - item_num // 3) * price_per_unit) + "(元)"
        elif one_format[0] in discount95off:
            total_price += price_per_unit * item_num * 0.95
            total_saved += price_per_unit * item_num * 0.05
            print "名称：" + full_data['Name'][index] + "，数量：" + str(one_format[1]) + full_data['Unit'][index] \
                  + "，单价：" + str(price_per_unit) + "(元)，小计：" + str(price_per_unit * item_num * 0.95) + "(元)，节省" \
                  + str(price_per_unit * item_num * 0.05) + "(元)"
        else:
            total_price += price_per_unit * item_num
            print "名称：" + full_data['Name'][index] + "，数量：" + str(one_format[1]) + full_data['Unit'][index] \
                  + "，单价：" + str(price_per_unit) + "(元)，小计：" + str(price_per_unit * item_num) + "(元)"
    if get_1_free_info:
        print "----------------------"
        for one_free in get_1_free_info.iteritems():
            print "名称：" + one_free[0] + "，数量：" + one_free[1]
    print "----------------------"
    print "总计：" + str(total_price) + "(元)"
    print "节省：" + str(total_saved) + "(元)"
    print "**********************"


if __name__ == '__main__':
    in_file = 'item_info.csv'
    full_data = pd.read_csv(in_file)
    update_discount_info(full_data)
    input_random = generate_input(full_data)
    print_check_out(input_random)
