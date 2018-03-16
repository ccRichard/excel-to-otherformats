# GMtoWiki使用说明文档

### 工具说明

因为直接在redmine上编辑wiki的表格较为复杂，为方便管理，还是将项目中常用GM指令用excel表格整理，然后再将其转换为wiki表的格式，最后自动提交到redmine的wiki页面上。

- exceltoformats.py：该脚本的功能是将excel表格转换为wiki表格。
- uptoredmine.py：该脚本的功能是编辑和修改redmine上的wiki页面，redmine的访问配置也在该脚本中。
- gm.xlsx：GM指令存放的excel表格。

----
### 使用说明

因为脚本可以自动转换格式并提交wiki，所以日常维护GM指令只需要打开excel表格进行编辑即可，编辑完成后，Jenkins上配置有个自动运行的任务，会监控gm.xlsx的修改，一旦发现有修改，就会运行脚本，将修改的内容同步到wiki上。

----
### 运行环境

- 支持系统：windows、linux
- 脚本语言：python3
- 依赖库：python-redmine
- 维护人：CC

----
### Jenkins配置

因为代码是托管在svn上的，所以需要配置以下几项内容：
1. 源码管理：选中Subversion，Repository URL里填写上svn地址，Credentials里添加或选择一个有访问该svn的账号密码用户。其他默认即可。
2. 构建触发器：勾选“Poll SCM”，然后日程表里填写“* * * * *”表示1分钟检查一次。
3. 构建：写上要执行的脚本名称，建议先cd到脚本所在目录，再执行脚本，否则跨目录执行脚本可能会有读写文件找不到的报错，当然也可以在脚本里自己处理读写文件的路径，但较为麻烦。

