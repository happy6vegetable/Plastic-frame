# PyDevOps 开发环境搭建

## 什么是Poetry？

[Poetry](https://python-poetry.org/) 是一个 Python 虚拟环境和依赖管理工具，另外它还提供了包管理功能，比如打包和发布。Poetry 可以同时管理 Python 库和 Python 程序。

## 安装Poetry

如果你是 Linux / MacOS / WSL用户, 执行以下命令:  
`curl -sSL https://install.python-poetry.org | python3 -`
如果你是 Windows 用户，请使用 **Powershell** 执行以下命令  
`(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

> 如果报错无法找到`py`命令，请尝试将`py`替换为`python`
> 参见 [Poetry-Installation](https://python-poetry.org/docs/#installation)

安装结束后，命令行中输入(Powershell请打开一个新的窗口)命令: `poetry --version`，如果出现类似以下内容，则为安装成功：

```powershell
in> poetry --version
out< Poetry (version 1.3.2)
```

## 配置Poetry

打开系统的命令行界面(Powershell / sh / bash或者其他)，输入命令：  
`poetry config virtualenvs.in-project true`  
该命令会让poetry在本项目所在目录下创建虚拟环境，而非其他奇怪的地方  
输入命令`poetry config --list`进行验证，应观察到存在输出:

```powershell
...
virtualenvs.in-project = true
...
```

证明配置成功

## 使用Poetry管理虚拟环境

上述步骤完成后，**切换到项目目录(切记!)**,执行命令`poetry install`，Poetry会根据项目目录下的`pyproject.toml`文件安装虚拟环境。
安装完毕后，可在项目目录下使用`poetry shell`命令进入该虚拟环境中。

如果你使用VsCode，可以在VsCode终端内运行命令`&.venv/Scripts/Activate.ps1`激活虚拟环境。

---

**!注意**：如无特殊说明，下述内容均应在poetry的虚拟环境中进行，并且鉴于一些原因，安装过程可能需要一些魔法。

---

## 什么是pre-commit?

[pre-commit](https://pre-commit.com/#introduction)是Git自带有的hook，它可以在我们commit之前先对提交的内容进行遍历、检测亦或是其他操作。它可以确保提交到仓库内的代码风格一致。

## 安装pre-commit

正常情况下，pre-commit会在之前的`poetry install`命令中被安装，如果执行命令`pre-commit --version`显示未找到该命令，可以使用`pip install pre-commit`命令进行安装。

## 配置pre-commit

安装pre-commit无误后，执行命令`pre-commit install`，将会安装一系列预先设置好的git hook，用以规范仓库代码和提交信息风格。  
接下来，只要你进行`git commit`相关的命令，pre-commit都将会自动运行，对你修改过的代码进行规范。

## 配置VsCode

如果你使用VsCode进行项目的开发，建议安装以下插件：

- EditorConfig for VS Code
- Pylance
- Python
