#  SPDX-License-Identifier: GPL-2.0-only
# 
#   Copyright (C) 2021  anandadwipra <anandabiru04@gmail.com> 

def bmi(weight, height):
    return  "Underweight" if (weight/height**2)<=18.5 else "Normal" if (weight/height**2)<=25.0 else "Overweight" if (weight/height**2)<=30.0 else "Obese"