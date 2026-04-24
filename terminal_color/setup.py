from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="terminal_color_tool",
    version="0.1.2",                
    author="NoName ^_^",
    author_email="77pl77@inbox.ru",
    description="Change colors in your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/platonzhuman/FOSSDEV",
    package_dir={"": "src"},
    py_modules=["command", "colors"],  
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "terminal-color=command:main",
        ],
    },
)