# Python 虚拟环境

## 什么是虚拟环境？

**虚拟环境**是一个隔离的空间，允许管理特定项目的依赖项，而不会干扰其他项目或系统上的全局 Python 环境。

## 为什么使用虚拟环境？
- **隔离**：避免不同项目中使用的包版本之间的冲突。
- **易于管理**：为每个项目使用特定的依赖项。
- **可移植性**：允许其他开发人员轻松复制您的项目环境，安装完全相同的包和版本。

![image venv](images/python-virtual-envs.png)

总之，虚拟环境允许您：
1. 在不同的项目中使用不同版本的包。
2. 通过仅在当前项目中安装依赖项来保持全局环境的整洁。

# 使用 `uv` 管理虚拟环境

`uv` 是一个现代且快速的工具，用于管理 Python 项目的虚拟环境和依赖项。
它用 Rust 编写，性能远优于传统工具，如 pip 和 pipenv。

`uv` 由 Astral 开发，即 ruff 背后的团队，您可以在 https://docs.astral.sh/uv/ 访问 uv 的文档

## 安装 `uv`
要安装 `uv`，请执行以下命令：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

或在 macOS 上使用 Homebrew：
```bash
brew install uv
```

对于 Windows：⚠️ 以管理员模式启动 powershell 或 VS code（推荐 VS code）
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
在本单元的其余部分，如果您使用 Windows，仅使用 powershell 或以管理员模式运行 VS code 进行安装

## 安装 Python 3.12

安装 `uv` 后，您需要为此项目安装 Python 3.12。`uv` 可以自动管理 Python 的安装：

```bash
uv python install 3.12
```

此命令将下载并安装 Python 3.12（如果您的系统中尚未安装）。`uv` 以隔离的方式管理 Python 版本，允许在您的计算机上拥有多个 Python 版本而不会产生冲突。

要验证 Python 3.12 已正确安装：

```bash
uv python list
```

此命令显示系统上所有可用的 Python 版本。

## 安装依赖项

在项目的根目录中，您可以看到有三个可用的文件：
- `.python-version`：指定要使用的 Python 版本（3.12）
- `pyproject.toml`：包含项目元数据和依赖项列表
- `uv.lock`：锁定文件，确保每个人使用的包版本完全相同

这些文件定义了我们项目的依赖项，因此定义了为了使其无缝运行需要安装的包。

如果打开 `pyproject.toml` 文件，您可以在 `dependencies` 部分中看到所有这些依赖项以及所需的版本。

要创建虚拟环境并使用 uv 安装依赖项，请在项目根目录运行以下命令：

```bash
uv sync
```

此命令将：
1. 通过 `.python-version` 文件检测所需的 Python 版本（3.12）
2. 在 `.venv/` 文件夹中自动创建虚拟环境
3. 安装 `pyproject.toml` 中列出的所有依赖项

由于此命令和虚拟环境，参加本课程的每个学生都拥有带有正确版本的必要包！

## 激活和停用虚拟环境

使用 `uv`，您可以以传统方式激活虚拟环境：

```bash
source .venv/bin/activate
```

或在 Windows 上：
首先启用脚本执行：
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
然后激活 venv
```bash
.venv\Scripts\activate
```

根据您的操作系统，您应该看到您的终端已更改，现在在一行的开头显示虚拟环境的名称
```bash
(.venv) user>
```

您也可以验证 python 可执行文件的路径确实是虚拟环境中的路径：
```bash
which python
```

要停用环境：
```bash
deactivate
```

或者，`uv` 允许直接在虚拟环境中执行命令而无需激活：
```bash
uv run python mon_script.py
```

## 在虚拟环境中安装包

在项目过程中，如果您需要在您的 env 中安装包，您只需执行：
```bash
uv add <nom_du_package>
```

此包将自动添加到 pyproject.toml 文件中并安装到您的环境中


在处理项目时，请注意激活虚拟环境以避免依赖项问题！

## 与 Jupyter Notebook 配合使用

⚠️ **重要**：在本课程中使用 Jupyter Notebooks 时，您必须：

1. **在启动 Jupyter 之前激活虚拟环境**（通常已通过前面的步骤完成）：

```bash
source .venv/bin/activate  # 在 macOS/Linux 上
# 或
.venv\Scripts\activate     # 在 Windows 上
```

或直接使用：

```bash
uv run jupyter notebook
```

在 Windows 上强烈建议在 VS code 中运行 notebook

如果从 powershell 启动 notebook 并在浏览器上出现错误，请将该命令给出的 localhost 链接复制粘贴到浏览器中

2. **在 notebook 中选择正确的内核**：
   - 打开 notebook 后，查看页面右上角
   - 您应该看到所使用的 Python 内核的名称（例如："Python 3.12"）
   - 单击它以验证或更改内核
   - 确保选择与您的虚拟环境 `.venv` 或 notebook 名称相对应的内核

如果在可用内核列表中看不到虚拟环境，可以使用以下命令添加它：

```bash
uv run python -m ipykernel install --user --name=dataengineer --display-name="Python (DataEngineer)"
```

此命令将创建一个名为"Python (DataEngineer)"的内核，您可以在您的 notebooks 中选择它。

## 下一步
当虚拟环境一切就绪后，您可以通过打开 notebook `Part2_Git.ipynb` 继续进行
````