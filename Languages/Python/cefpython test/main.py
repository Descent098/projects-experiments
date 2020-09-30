from cefpython3 import cefpython as cef
import platform
import sys
import os


def main():
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {"auto_zooming":"2.0"}
    cef.Initialize(settings)
    cef.CreateBrowserSync(url=f"file://{os.path.abspath(os.curdir)}\\UI\\index.html",
                            window_title="Hello World!")
    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()