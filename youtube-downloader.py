import os, curses, sys, subprocess
from curses import wrapper
from curses.textpad import Textbox, rectangle

menu = ['extract audio (mp3)', 'extract video (mp4)', 'exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def msg(stdscr):
    stdscr.clear()
    print_center(stdscr, message)
    stdscr.refresh()
    stdscr.getch()
    if message == "Invalid URL provided. Press enter to quit.":
        os.system("killall Terminal")
    else:
        os.system("open Downloads")
        os.system("killall Terminal")

def main(stdscr):

    global mediaFormat
    global url
    global message
    
    print_center(stdscr, "Enter a YouTube URL and press enter!")

    rectx = 5
    recty = 5

    editwin = curses.newwin(1, 44, 10, 19) #(1,30, 2,1)
    #rectangle(stdscr, 1, 5, 3, 51) #1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Enter is struck.
    box.edit()

    # Get resulting contents
    url = box.gather()

    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
            
        elif key == curses.KEY_ENTER or key in [10, 13]:
            #checks the current row and performs the selected action
            if current_row == 0:
                mediaFormat = "mp3"
                break
            if current_row == 1:
                mediaFormat = "mp4"
                break
            if current_row == 2:
                os.system("killall Terminal")
                break

            stdscr.getch()

        print_menu(stdscr, current_row)

#start main()
curses.wrapper(main)

#restore terminal
curses.endwin()

if mediaFormat == 0:
    os.system("killall Terminal")
if len(url) < 44 or "https://www.youtube.com/watch?v=" not in url:
    message = "Invalid URL provided. Press enter to quit."
    curses.wrapper(msg)
else:
    if mediaFormat == "mp3":
        message = "Downloading successful! Press enter to quit."
        os.system("youtube-dl --rm-cache-dir")
        os.system("[ytdl] Cache cleared successfully!")
	os.system("youtube-dl --extract-audio --audio-format mp3 "+ url)
        curses.wrapper(msg)
    if mediaFormat == "mp4":
        message = "Downloading successful! Press enter to quit."
        os.system("youtube-dl --rm-cache-dir")
	os.system("[ytdl] Cache cleared successfully!")
	os.system("youtube-dl -f mp4 "+ url)
        curses.wrapper(msg)

print("ALERT: IF YOU ARE SEEING THIS MESSAGE SOMETHING HAS BROKEN. CONTACT ETHAN FOR MORE INFO")

