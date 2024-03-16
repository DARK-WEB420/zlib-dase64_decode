
import os


logo="""\033[38;5;46m      ╔╦╗╔═╗╦═╗╦╔═   \033[38;5;46m╦ ╦╔═╗╔╗ 
\033[38;5;46m       ║║╠═╣╠╦╝╠╩╗\x1b[38;5;196m───\033[38;5;46m║║║║╣ ╠╩╗
\033[38;5;46m      ═╩╝╩ ╩╩╚═╩ ╩   \033[38;5;46m╚╩╝╚═╝╚═╝
\033[38;5;46m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\033[38;5;46m┃\033[1;91m\033[1;41m\033[1;97m   WELCOME DARK-WEB TERMUX ZONE    \033[;0m\033[1;91m\033[1;92m\033[38;5;46m┃
\033[38;5;46m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;46m┃\033[33;1m DEVOLPER   \033[1;97m➢    \033[33;1mMD.ABDULLAH       \033[38;5;46m┃
\033[38;5;46m┃\033[38;5;46m FACEBOOK   \033[1;97m➢    \033[38;5;46mABDULLAH AL MAMUN \033[38;5;46m┃
\033[38;5;46m┃\x1b[38;5;208m GITHUB     \033[1;97m➢  \x1b[38;5;208m  DARKWEB-420       \033[38;5;46m┃
\033[38;5;46m┃\033[1;97m WATHSAPP   \033[1;97m➢  \033[1;97m  +8801725308028    \033[38;5;46m┃
\033[38;5;46m┃\x1b[38;5;196m TYPE       \033[1;97m➢    \x1b[38;5;196mDECOMPILE         \033[38;5;46m┃
\033[38;5;46m┃\x1b[1;96m FROM       \033[1;97m➢    \x1b[1;96mBANGLADESH        \033[38;5;46m┃
\033[38;5;46m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;37m"""

def main():
    os.system("clear")
    print(logo)
    print("\033[1;30m[\033[38;5;46mA\033[1;30m~\033[38;5;46m1\033[1;30m] \033[38;5;46mDecode Zlib \n\033[1;30m[\033[38;5;46mB\033[1;30m~\033[38;5;46m2\033[1;30m] \033[38;5;46mDecode Base64\n")
    choice=input("\033[1;30m[\033[38;5;46m✓\033[1;30m] \033[38;5;46mInput\033[1;97m ➢ \033[35;1m")
    dec()

def dec():
    os.system("clear")
    print(logo)
    print("\033[1;30m[\033[38;5;46m✓\033[1;30m] \033[38;5;46mExample file_enc.py")
    file=input("\033[1;30m[\033[38;5;46m✓\033[1;30m] \033[38;5;46mInput file\033[1;97m ➢ \033[35;1m ")
    ogge=str(open(file,"r").read())
    data=ogge.replace("exec","heron=")
    data2=f"""{data}\nopen(\"dec_done.py\",\"w").write(heron.decode(\'utf-8\')) """
    open(".dara.py","w").write(data2)
    os.system("python .dara.py")
    print(" \033[38;5;46mfile saved with \x1b[38;5;196mdec_done.py")
    print(" \033[38;5;46mDec done \033[1;30m[\033[38;5;46m✓\033[1;30m] ")
    

main()