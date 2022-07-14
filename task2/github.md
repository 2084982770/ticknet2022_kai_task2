搜索awesome html 进入链接[diegocard/awesome-html5](https://github.com/diegocard/awesome-html5)  git clone 拉取仓库 阅读README文件<br>
建立本地仓库：git init<br>
上传所有代码到本地仓库：git add .<br>
提交文件：git commit -m "ticknet2022"<br>
在github上新建一个仓库"ticknet2022_kai_task2"。
关联本地仓库上传代码：git remote add origin git@github.com:2084982770/ticknet2022_kai_task2.git (不过这一步搞错了，复制成了html 而不是ssh 导致上传代码没有权限，重新删除关联：1.git remote -v查看远程库信息:origin	https://github.com/2084982770/ticknet2022_kai_task2.git (fetch)<br>
origin	https://github.com/2084982770/ticknet2022_kai_task2.git (push)<br>
然后输入git remote rm origin解除关联)<br>
最后git push origin master上传。<br>
然后一不小心忘了git add .结果把电脑文件全上传上去了。