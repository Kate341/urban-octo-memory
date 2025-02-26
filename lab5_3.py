import re

txt = "i_really_like_my_mom"
txt1 = "Y_o_u_a_r_e_a_s_t_u_d_e_n_t"

x = re.findall("[a-z]_[a-z]", txt)
y = re.findall("[a-z]_[a-z]", txt1)

print(x)
print(y)

print(bool(x))
print(bool(y))

#Without input()

txt2 = str(input())

z = re.findall("[a-z]_[a-z]", txt2)

print(z)
print(bool(z))

#With input()