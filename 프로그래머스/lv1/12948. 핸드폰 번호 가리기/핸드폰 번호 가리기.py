def solution(phone_number):
    last_four = phone_number[-4:]
    forward_num = phone_number[:-4]
    star_num = forward_num.replace(forward_num, len(forward_num) * '*')
    return star_num + last_four