<div align="center">

~假装有图片~

# 手机胶框检查系统

基于Python的图像识别和机器学习进行胶框识别的项目

</div>

## 开发者

- happy6vegetable
- GenshinMagic
- ScatteredWood
- WinterBlessing
- xyx6152

  

## 开发环境搭建步骤

使用了以下工具进行管理：

- poetry：管理Python虚拟环境
- pre-commit：管理代码格式规范和commit信息规范
- nonemoji：为commit提供有概括性的emoji

> 前往阅读 >>[配置开发环境](./guide/dev-config.md)<<

## commit注意事项

项目使用了 [nonemoji](https://github.com/nonebot/nonemoji) 对commit信息进行规范

### nonemoji 介绍以及使用

对于commit，在git commit时，应该所写的commit msg前附带一个emoji(前后使用`:`包裹起来的emoji名称，例如`:fire: ->`:fire:)，用来概括本次提交的意图，例如:

```commit
git commit -m ":bug: 修复了xxx错误"

// 这样commit之后的信息就会显示

🐛 修复了xxx错误

```

从而使得commit msg更容易理解

也可以直接在命令行里输入`nonemoji`命令，选择一个合适的nonemoji后填写commit msg并提交

所有可用的nonemoji参见下面的链接，或者使用`nonemoji list`命令查看

> 前往阅读 >>[使用nonemoji进行commit](./guide/nonemoji.md)<<
