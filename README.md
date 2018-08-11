# babel_battle_platform
Online Battle Platform for BableTime

## StartUp
1. pip install virtualenv
2. 在包含 requirements.txt 的文件夹
	* virtualenv venv
	* source venv/bin/activate
	* pip install -r requirements.txt
3. 在包含 manage.py 的文件夹
	* python manage.py makemigrations
	* python manage.py migrate
	* python manage.py runserver
4. 查看命令行对应的地址，打开浏览器，开始流程

## Code
1. 	babel\_battle_platform
	* settings.py 
		* 一些文件的基本设定，注意看:
		* STATIC_URL = '/static/'
		* MEDIA_ROOT = os.path.join(BASE\_DIR, 'battle\_platform', 'scripts') 	
	* urls.py
		* 总的 url 路径
2. babel\_platform
	* python 文件
		* models.py
			* 所有的类模型，包括上传记录等等
		* forms.py
			* ModelForm 
		* urls.py
			* 当前 app 的 url	 
		* views.py
			* 处理对应 url 的函数
		* admin.py
			* 后台查看数据库的配置
	* 文件夹
		* scripts
			* 存放上传的脚本的文件夹
		* templates
			* 存放 html 页面
		* static
			* 一些静态文件，作用在 html 页面上面，同时存放要播放的视频

## Logic
1. 用户通过浏览器输入一个 url
2. 查看 urls.py 来决定将 url 路由到哪一个处理函数（函数在view.py里面）
3. 在 views.py 中找到对应函数，经过一系列操作，包括数据库交互（可以没有）、文件系统交互（可以没有）等，最终返回一个 html 页面给用户，html 页面存放在 templates 里面，通过 static 的文件渲染
4. 用户通过点击按钮、直接访问 url 等操作和页面交互，继续触发下一个 url ，以完成下一个操作

## Function
1. 注册登录
2. 登录后上传脚本，脚本一定以 .lua 结尾
3. 脚本上传后将其保存在 scripts 里面，同时触发一个后端任务，以运行脚本
4. 用户回到首页后可以看到上传脚本的记录，点击上传脚本可以下载，同时如果脚本运行完可以点击播放视频
 