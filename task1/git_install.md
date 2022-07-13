1.ubuntu安装git：<br>
sudo apt-get install git<br>
2.添加账户:
git config --global user.name "账户名"<br>
git config --global user.email "邮箱"<br>
3.配置ssh密钥：<br>
生成密钥：ssh-keygen -t rsa -C "邮箱"<br>
然后按回车，输入两次密码。<br>
将私钥添加到ssh代理中：ssh-add ~/.ssh/id_rsa<br>并输入密码。将得到的私钥复制。<br>
用网页打开github进入个人账户添加刚刚生成的密钥。完成。