# monitor_server_space_usage
监控服务器空间使用情况，当小于一定空间时，邮件发送出来。
====


# 1简述

执行sendmail.py 脚本，可以根据脚本里的限制阀值判断是否发送警告邮件。再通过crontab定时触发机制配合使用从而达到自动监控的目的。

# 2步骤
## 2.1 获取sendmail.py ,修改相关配置，放置脚本位置，添加可执行权限
获取到sendmail.py文件后需要修改脚本里的相关配置<br>
1.邮件服务器，自己的邮件账号和密码<br>
2.被告知者的邮件填写<br>
3.阀值设置<br>
<br>
可以把脚本放置在/usr/sbin/下，通过以下命令添加可执行权限：<br>

```Bash
sudo cp sendmail.py /usr/sbin/
sudo chmod +x /usr/sbin/sendmail.py
```

<br>
<br>
## 2.2.测试脚本是否可用
### 2.2.1.先查看当前服务器使用情况，根据情况修改sendmail.py脚本
```Bash
sudo df -h |grep " /$" |awk '{print $5}'
```
通过root用户，执行上述命令，查看当前使用的数值为多少，如果是50%，那么先修改sendmail.py的阀值为50以下

### 2.2.2.手动执行测试脚本，查看是否收到邮件,如果收到邮件说明正常，再把阀值修改为想要监控的数值
设置好阀值后，手动执行脚本，查看是否邮件收到
```Bash
sudo /usr/bin/python /usr/sbin/sendmail.py
```

## 2.3 配置crontab，添加sendmail.py
crontab具体是什么作用，就自己搜索吧。<br>
建议使用root权限下的crontab，如果之前未使用过crontab，以下是基本的一些命令：
```Bash
#crontab -l   查看当前脚本内容
#crontab -e   编辑内容，如果是第一次，会出现使用何种编辑器进行编辑，建议选择vim相关的，其他的比较复杂
```
vim的简单操作命令：
```Bash
#进入vim后，是还未进入编辑模式，输入a，进入编辑模式，按ESC调出编辑模式，在非编辑模式下，输入：wq 标示保存退出，其他不要乱输入，实在不行先查下vim的基本使用方法吧。
```

crontab的一些格式，看了就懂了：
```Bash
0 23-7/1 * * * /usr/local/apache/bin/apachectl restart
晚上11点到早上7点之间，每隔一小时重启apache

0 11 4 * mon-wed /usr/local/apache/bin/apachectl restart
每月的4号与每周一到周三的11点重启apache

0 4 1 jan * /usr/local/apache/bin/apachectl restart
一月一号的4点重启apache

0 */1 * * * /usr/local/apache/bin/apachectl restart
每一小时重启apache
```
