import ctf_platforms
import config

buu = ctf_platforms.BUUCTF(config.BUUCTF_COOKIE)
bugku = ctf_platforms.BugKu()
print(buu.get_user_info("glzjin"))
print(bugku.get_user_info("112"))
