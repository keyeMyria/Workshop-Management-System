# -*- coding:utf-8 -*-
import datetime

from fabric.api import env, run, prompt, local
from fabric.state import output

SERVER_HOST = ['118.126.64.162']
SERVER_USER = 'ubuntu'

env.environment = ""
env.full = False
output["running"] = False
output["stdout"] = False


def prd():
    """	生产环境 """
    env.environment = "prd"
    env.hosts = SERVER_HOST
    env.user = SERVER_USER
    env.tag_prefix = "REG"
    print("PRODUCTION\n")


def deploy():
    """	根据选择环境部署 """
    if not env.environment:
        while env.environment not in ("dev", "prd"):
            env.environment = prompt('请选择部署环境 ("dev" or "prd"): ')
            print()

    # 删除redis key, 每次都重新生成定时job, 跳过slave机器
    if env.host_string in (SERVER_HOST[0],):
        _del_redis_keys()

    # 获取当前分支
    dev_branch = local('git rev-parse --abbrev-ref HEAD', capture=True)

    print("当前分支dev_branch：%s" % dev_branch)

    # 生成tag号
    tag_str = _tag("REG", dev_branch)
    globals()["_update_%s" % env.environment](tag_str)

    # 切换到发布之前的branch
    if local('git rev-parse --abbrev-ref HEAD', capture=True) != dev_branch:
        local("git checkout %s" % dev_branch)


def _del_redis_keys():
    run("redis-cli del :1:schedule_once")


def _tag(server_type, current_branch=None):
    if server_type == "REG":
        local("git checkout master")
        # 合并分支到 master
        local("git merge %s" % current_branch)

    tag_str = '_'.join((server_type, datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
    # print(green(" * tagging: %s\n" % tag_str))
    local("git tag %s" % tag_str)
    # print(green(" * pushing tag: %s\n" % tag_str))
    local("git push --tags")
    return tag_str


# 更新生产服务器
def _update_prd(tag_str):
    # 更新 code
    _update_code()

    # checkout 分支
    _checkout(tag_str)

    # 重启服务 circus
    _restart_circus()


def _update_code():
    # print(green(" * updating code ...\n"))
    run("cd ~/Workshop-Management-System/WMS/ && git fetch --tags")


def _checkout(tag_str=None):
    # print(green(" * checking out %s\n" % tag_str))
    if tag_str:
        run("cd ~/Workshop-Management-System/WMS/ && git checkout %s" % tag_str)
    else:
        run("cd ~/Workshop-Management-System/WMS/ $(git describe --tags)")


def _restart_circus():
    # print(green(" * restarting circus ...\n"))
    run("circusctl restart")
