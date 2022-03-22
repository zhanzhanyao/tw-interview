# training plan
- Command Line
- Java
- Database
- HTML & CSS
- JavaScript
- Extreme Programming
- Spring Boot
- React

## Step 1: CLI Basics
### Git basics
#### Learning Target
- 了解版本管理/版本控制概念
- 了解Git基本概念
- 掌握部分常用的Git命令
- 使用Git完成个人独立开发时需要处理的版本控制场景

### CLI basics
#### Learning Target
- 了解操作系统
- 了解Linux操作系统基本概念
    - 文件及目录管理
    - 用户及权限管理
- 了解CLI, Terminal, Console等基本概念
- 掌握部分Linux系统下的常见CLI命令
- 能够编写Bash Script解决基本问题

#### Prerequisites
Terminal
Console
Shell
GUI: Graphical User Interface
CLI: Command-Line Interface

shell 类型
bash/zsh/fish

#### 一些命令
- echo
- source #新改了命令让其生效
- export PATH="$PWD:$PATH"
- which scriptname # 看scriptname在哪里
- whereis scriptname # 看scriptname在哪里
- type *** # 看***是什么
- man/help/tldr  # 帮助 
- grep 
- cut
- |  # 管道
- /> >> 2>  <  # 重定向
- history
- hello world 函数/脚本


      #！/bin/bash
      TS=$(date "+%Y-%m-%d %H:%M:%S") #获取其他命令输出
      NAME=$*
      echo [$TS] hello $NAME

      function(){
        N=$1;
        echo hello $N
      }

#### 命令的四个来源
- shell builtin/shell 自带
- 系统提供
- 自定义的function
- 自己提供的可执行脚本或程序

#### 命令的使用方式
command [options] parameters

#### 常用简单命令
cat
chmod
chown
cut
echo
find
history
ifconfig
less
ping
ps
sort
top
touch
tr
uniq
which

#### 常用高级命令
awk
expect
sed
xargs
vim




