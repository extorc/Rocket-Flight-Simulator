from rocket import *

def compute_pid(error,error_log):
    pgain = 1
    pid = error * pgain
    return pid
