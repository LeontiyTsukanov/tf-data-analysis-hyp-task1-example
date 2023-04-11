import pandas as pd
import numpy as np


chat_id = 407415686 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x = x_success/x_cnt
    y = y_success/y_cnt
    flag = False
    if x/y > 1.04:
        flag = True
    return flag # Ваш ответ, True или False
