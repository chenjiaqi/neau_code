import curses


def main(stdscr):
    # 初始化curses
    curses.curs_set(0)  # 隐藏光标
    stdscr.clear()

    # 打印汉字

    stdscr.addstr(5, 40,  "<<Python 入门 !>>", curses.A_BOLD)
    stdscr.addstr(10, 42, "主讲人: 陈佳琦", curses.A_BOLD)
    stdscr.addstr(20, 41, "(嵌入式软件工程师)", curses.A_BOLD)

    # 刷新屏幕
    stdscr.refresh()

    # 等待用户按任意键退出
    stdscr.getch()


curses.wrapper(main)
