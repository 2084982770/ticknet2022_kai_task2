# 第二章（计算机基础）

本章学习服务器基本操作和HTTP协议。最后要求使用套接字协议编写一个HTTP请求器。

## 任务一：自动安装python、node脚本

https://linuxtools-rst.readthedocs.io/zh_CN/latest/base/

编写一个shell脚本，自动**编译安装**python、nodejs

### 功能：

1. 选择是要（安装/卸载）（python/node）。
2. 自动结束所有（python/node）进程
3. 下载源码
4. （编译安装/删除）

附加题：实现python环境或者node环境的切换

## 任务二：使用TCP来实现HTTP下载器

- https://www.cnblogs.com/ranyonsue/p/5984001.html
- https://developer.mozilla.org/zh-CN/docs/Web/HTTP
- 抓包工具fiddler
- 抓包工具wireshark
- 浏览器调试工具（devtool network）

### 功能

1. 参考curl或者requests

附加题：
- 支持http代理
- 支持http1.1

## 编写文档

我们要求你编写文档来记录本次实现过程，可以是以博客的样式记录。把文档写入到 `submit.md` 中即可，该文件会在运行提交命令后自动上传。

## 如何提交到服务器

首先需要使用commit将你的代码交予git管理，这样在切换分支的时候修改不会丢失。

```shell
# 添加到暂存区
git add .
# 提交
git commit -m "<一些描述信息>"
```

然后运行将自己的key填入 `submit.yml` 的 `key` 键中。最后运行以下命令提交。

```shell
python submit.py
```
