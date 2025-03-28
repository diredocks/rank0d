import ctf_platforms

# buu = ctf_platforms.BUUCTF("session=")
# info = buu.get_user_info("glzjin")
bugku = ctf_platforms.BugKu("")
info = bugku.get_user_info("112")
print(info)
