#!/usr/bin/python3
def delete_at(fresh_list=[], idx=0):
    if 0 <= idx < len(fresh_list):
        del fresh_list[idx]
    return fresh_list
