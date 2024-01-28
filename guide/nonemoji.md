# Nonemoji

## 什么是 nonemoji ?

nonemoji 可以认为是 [gitmoji](https://gitmoji.dev/) 的简化版。

gitmoji是一个标准化和解释在GitHub提交消息上使用emoji的倡议。 gitmoji 是一个开源项目，专门规定了在 github 提交代码时应当遵循的 emoji 规范

在git commit上使用emoji提供了一种简单的方法，仅通过查看所使用的表情符号来确定提交的目的或意图。

## 为什么要使用 nonemoji？

在执行 git commit 指令时使用 emoji 图标为本次提交添加一个特别的图标， 这个本次提交的记录很容易突出重点，或者说光看图标就知道本次提交的目的。这样就方便在日后查看历史提交日子记录中快速的查找到对于的提交版本。
这里主要列出 nonemoji项目中规定的emoji规范的表情符号列表：

## 怎么使用 nonemoji？

> !注意：使用一下命令时请确保已经处于本项目的虚拟环境之中

可以直接在commit msg开头加入`:xxx:`(xxx为emoji名称)的标识，在commit成功后会自动转换为对应的emoji

### 快速提交

使用命令`nonemoji commit`可以快速选择一个emoji并填写commit msg进行commit

### 交互式使用

不使用`git commit`提交commit，而是使用`nonemoji`命令：

```powershell
in>
(pydevops-py3.10) PS X:\xxx\xxx> nonemoji

out<
[?] What do you want to do? (Use ↑ and ↓ to choose, Enter to submit)
❯ Start to commit changes
List all available emojis
Search for an emoji

//选择 Start to commit changes

out<
[?] Choose a gitmoji: (Use ↑ and ↓ to choose, Enter to submit)
❯ ✨  - Introduce new features.
  🐛  - Fix a bug.
  📝  - Add or update documentation.
  📄  - Add or update license.
  🎨  - Improve structure / format of the code.
  ♻️   - Refactor code.
  ✅  - Add, update, or pass tests.
  🚀  - Deploy stuff.
  .....

// 选择 ✨  - Introduce new features.

out<
[?] Choose a gitmoji: ✨  - Introduce new features.
[?] Enter the commit title: is a test

//...开始执行 git commit 命令
//...开始进行其他检查
```

> 参考教程：[Git Commit emoji Guide 提交表情使用指北](https://hooj0.github.io/git-emoji-guide/)

## nonemoji 表情库

| emoji 表情                               | emoji 代码                    | commit 说明               |
| :--------------------------------------- | :---------------------------- | :------------------------ |
| :sparkles: (火花)                        | `:sparkles:`                  | 引入新功能                |
| :bug: (bug)                              | `:bug:`                       | 修复 bug                  |
| :memo: (备忘录)                          | `:memo:`                      | 添加或者更新文档          |
| :page_facing_up: (文档)                  | `:page_facing_up:`            | 添加或更新许可证。        |
| :art: (调色板)                           | `:art:`                       | 改进代码结构/代码格式     |
| :recycle: (循环箭头)                     | `:recycle:`                   | 重构代码                  |
| :white_check_mark: (白色复选框)          | `:white_check_mark:`          | 增加或者更新测试          |
| :rocket: (火箭)                          | `:rocket:`                    | 部署功能                  |
| :lipstick: (口红)                        | `:lipstick:`                  | 更新 UI 和样式文件        |
| :bookmark: (书签)                        | `:bookmark:`                  | 发行/版本标签             |
| :label: (标签)                           | `:label:`                     | 增加或者更新类型          |
| :rotating_light: (警车灯)                | `:rotating_light:`            | 移除 compiler/linter 警告 |
| :heavy_plus_sign: (加号)                 | `:heavy_plus_sign:`           | 添加一个依赖              |
| :heavy_minus_sign: (减号)                | `:heavy_minus_sign:`          | 移除一个依赖              |
| :arrow_down: (下降箭头)                  | `:arrow_down:`                | 降级依赖                  |
| :arrow_up: (上升箭头)                    | `:arrow_up:`                  | 升级依赖                  |
| :pushpin: (图钉)                         | `:pushpin:`                   | 将依赖关系固定到特定版本  |
| :green_heart: (绿心)                     | `:green_heart:`               | 修复 CI 构建问题          |
| :construction_worker: (工人)             | `:construction_worker:`       | 添加 CI 构建系统          |
| :chart_with_upwards_trend: (上升趋势图)  | `:chart_with_upwards_trend:`  | 添加分析或跟踪代码        |
| :wrench: (扳手)                          | `:wrench:`                    | 修改配置文件              |
| :hammer: (锤子)                          | `:hammer:`                    | 添加或者更新开发脚本      |
| :globe_with_meridians: (地球)            | `:globe_with_meridians:`      | 国际化与本地化            |
| :pencil2: (铅笔)                         | `:pencil2:`                   | 修复 typo                 |
| :tada: (庆祝)                            | `:tada:`                      | 开始项目                  |
| :construction: (施工)                    | `:construction:`              | 工作进行中                |
| :rewind: (双左箭头)                      | `:rewind:`                    | 恢复更改                  |
| :twisted_rightwards_arrows: (双合并箭头) | `:twisted_rightwards_arrows:` | 合并分支                  |
| :package: (箱子)                         | `:package:`                   | 更新编译的文件或包        |
| :alien: (面具)                           | `:alien:`                     | 由于外部API更改而更新代码 |
| :truck: (面包车)                         | `:truck:`                     | 移动或重命名文件          |
| :boom: (爆炸)                            | `:boom:`                      | 介绍突破性变化            |
| :wheelchair: (轮椅)                      | `:wheelchair:`                | 提高可访问性              |
| :bulb: (灯泡)                            | `:bulb:`                      | 更新源代码注释            |
| :beers: (干杯)                           | `:beers:`                     | 醉生梦死的写代码          |
| :loud_sound: (有声喇叭)                  | `:loud_sound:`                | 添加日志                  |
| :mute: (静音喇叭)                        | `:mute:`                      | 删除日志                  |
| :children_crossing: (小盆友)             | `:children_crossing:`         | 改善用户体验/可用性       |
| :building_construction: (建筑施工)       | `:building_construction:`     | 进行架构改变              |
| :see_no_evil: (蒙眼猴子)                 | `:see_no_evil:`               | 添加或更新.gitignore文件  |
| :triangular_flag_on_post: (旗子)         | `:triangular_flag_on_post:`   | 更改特性flags             |
| :goal_net: (球门)                        | `:goal_net:`                  | 捕获异常                  |
| :wastebasket: (垃圾桶)                   | `:wastebasket:`               | 清理需要弃用的代码        |
| :coffin: (棺材)                          | `:coffin:`                    | 清理从未使用的死代码      |
| :technologist: (码农)                    | `:technologist:`              | 提高开发者体验            |
| :zap: (闪电)                             | `:zap:`                       | 提升性能                  |
| :fire: (火焰)                            | `:fire:`                      | 移除代码或文件            |
| :bento: (便当)                           | `:bento:`                     | 更改asset                 |

# 举个例子

```
git commit -m ":tada:init commit"
git commit -m ":bug: debug a mistake"

```
