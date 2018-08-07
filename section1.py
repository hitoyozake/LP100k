# -* encoding: utf-8 *-

def problem_00():
    s = "stressed"
    reversed = ""
    for i in s[::-1]:
        reversed += i

    print("input:{0}, output: {1}".format(s, reversed))

    return reversed




if __name__ == '__main__':
    problem_00()