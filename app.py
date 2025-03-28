import ctf_platforms

buu = ctf_platforms.BUUCTF("session=")

info = buu.get_user_info("glzjin")
print(info)
