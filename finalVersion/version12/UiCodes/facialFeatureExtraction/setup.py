from distutils.core import setup

setup(
    name="CaptureFaces",
    version="1.0",
    description="人工智能-机器视觉实验套件系列",
    author="Louis Young",
    packages=[
        "capturefaces", 
        "font_zh", 
        "capturefaces.data",
        "font_zh.fonts"
    ],
    scripts=[
        "run.bat",
        "run.sh"
    ],
    package_data={
        "capturefaces.data": [
            "haarcascade_frontalface_alt2.xml", 
            "haarcascade_frontalface_alt.xml",
            "haarcascade_frontalface_default.xml",
        ],
        "font_zh.fonts": [
            "msyh.ttf",
        ],
    },

)


# python setup.py --help
# python setup.py --help-commands
# python setup.py build
# python setup.py install