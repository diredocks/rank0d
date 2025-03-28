import ctf_platforms
import config

clients = {
    "BUUCTF": ctf_platforms.BUUCTF(config.BUUCTF_COOKIE),
    "BugKu": ctf_platforms.BugKu(),
}

for user in config.USERS:
    for p, u in user["platforms"].items():
        info = clients[p].get_user_info(u)
        print(info)
