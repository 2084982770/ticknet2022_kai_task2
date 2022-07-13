在cs_basic_0分支下添加文件夹和文件task1，编辑文档。<br>
git add task1将修改文件夹存入缓冲区<br>
git commit -a将缓冲区所有文件提交<br>
然后编辑提交信息按ctrl+X下一步，选择y提交。
之前提交为空文件，没有保存，再次编写提交。然后通过：<br>
git log --pretty=oneline查看两次提交。<br>
用：git reset --hard HEAD^  回退到前一次提交，然后用：git reset --hard "加上提交编号"回退到最后一次提交。继续编写并提交。