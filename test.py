#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
@File    : test.py
@Time    : 2021/1/28 10:01 下午
@Author  : Han0nly
@Github  : https://github.com/Han0nly
@Email   : zhangxh@stu.xidian.edu.cn
-------------------------------------------------
"""
import json
import shutil
import fire
import os


def obfuscated(profiles: str, apk_files: str, dest_dir: str) -> list:
    app_profiles = {}
    for root, dirs, files in os.walk(profiles):
        for name in files:
            # app_profiles.append(root + '/' + name)
            if 'json' == name.split('.')[-1]:
                with open(root + '/' + name, 'r') as f:
                    profile = json.load(f)
                    # print(profile.keys())
                    if ('lib_matches' in profile.keys()) and (len(profile['lib_matches']) > 0):
                        # print("Hello")
                        app_profiles[profile['appInfo']['fileName']] = []
                        used_lib = []
                        for lib in profile['lib_matches']:
                            used_lib.append({lib['libName']: lib['usedLibMethods']})
                        app_profiles[name[:-5]] = used_lib
    # print(app_profiles)
    matched_apps = []
    for root, dirs, files in os.walk(apk_files):
        for name in files:
            if name[:-4] in app_profiles.keys():
                matched_apps.append(root + '/' + name)
                shutil.move(root + '/' + name, dest_dir + '/' + name)
    return matched_apps

def unobfuscated(namelist: str, apk_files: str, dest_dir: str) -> list:
    app_profiles = {}
    with open('write_data_apk_name.txt','r') as f:
        for line in f:
            line = line.strip().split('\\')
            app_name = line[-1].split(' ')[0]
            print(app_name)
    # # print(app_profiles)
    # matched_apps = []
    # for root, dirs, files in os.walk(apk_files):
    #     for name in files:
    #         if name[:-4] in app_profiles.keys():
    #             matched_apps.append(root + '/' + name)
    #             shutil.move(root + '/' + name, dest_dir + '/' + name)
    # return matched_apps

if __name__ == '__main__':
    fire.Fire()
    # print(app_profiles)
