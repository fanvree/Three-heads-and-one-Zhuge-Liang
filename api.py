学院平台助理(超级管理员)：

1.1、查询用户信息：
Method:GET
URL：/boss/user/list
QueryParam:
{
	'username': name(default ='')
	'page': 1
	'size': 20
}
Response:
{
	'total':101,
	'userlist':
	[
		{
			'userid': '101' //唯一id
			'username': 'fzr18',
			'identity': 'normal'/'renter'/'admin',
			'email': '12306@qq.com'
			'password': 'md5'
		},
	]
}

1.2、删除用户：
Method: POST
URL：/boss/user/delete
Request:
{
	'userid':'101'
}
Response:{}

1.3、设置用户类型：
Method:POST
URL：/boss/user/set
Request:
{
	'username': name,
	'identity': 'normal'/'renter'/'admin',
}
Response:{}

2.1 查看所有设备：
Method:GET
URL：/boss/device/list
QueryParam:
{
	'page': 1
	'size': 20
	'valid':0/已经上架 1/未审核 2/未上架 
	'deviceid': '101' //设备标识符
	'devicename': '设备名称' //可选
}
Response:
{
	'total':'101',
	'devicelist':[
	{
		'deviceid': '1' //设备唯一标识id
		'devicename': '自动机',
		'owner': 'fzr18',
		'phone': '188888888888'//owner's phone
		'user': 'yxr18',
		'rentout': 'True'/'False',
		'start': '2018年1月1日',  //借用开始时间
		'due': '2018年1月1日',  //借用结束时间
		'location': '东主楼',
		'addtion': '备注'
		'vaild'： 0/已经上架 1/未审核 2/未上架 
		'reason': '上架理由'
	}
	]
}

2.2 修改设备信息：
Method: POST
URL: /boss/device/change
Request:
{
	'deviceid': '1' //设备唯一标识id
	'devicename': '自动机',
	'owner': 'fzr18',
	'phone': '188888888888'
	'user': 'yxr18',
	'rentout': 'True'/'False',
	'start': '2018年1月1日',  //借用开始时间
	'due': '2018年1月1日',  //借用结束时间
	'location': '东主楼',
	'addtion': '备注',
	'vaild'： 0/已经上架 1/未审核 2/未上架 
	'reason': '上架理由'
}
Response:
{}


2.3 删除设备：
Method:POST
URL：/boss/device/delete
Request:
{
	'deviceid': '1' 
}
Response:{}

3.1 查看租借申请：
Method:GET
URL：/boss/order/list
QueryParam:
{
	'page': 1
	'size': 20
}
Response:
{
	'total':'101',
	'orderlist':[
	{
		'orderid': '1' //申请唯一标识id
		'devicename': '自动机',
		'owner': 'fzr18',
		'applicant': 'yxr18',
		'start':'2018年1月1日',
		'due': '2018年1月1日',  //借用结束时间
		'location': '东主楼',
		'addtion': '备注',
		'state': 0/审核通过 1/未审核 2/审核未通过 
	}
	]
}

3.2 租借审批申请:
Method:GET
URL：/boss/order/state
QueryParam:
{
	'orderid': '1',
	'state': 0/审核通过 1/未审核 2/审核未通过
}
Response:{}

3.3 删除租借申请：
Method:POST
URL：/boss/order/delete
Request:
{
	'orderid': '1',
}
Response:{}

4、用户注册：

5、用户申请成为设备提供者列表查看：
Method:POST
URL：/boss/offer
Request:
{
	'userid': '101',
	'labinfo': '',
	'reason': '',
}
Response:
{
	# offer:[
	# {
	# 	'userid': '101',
	# 	'reason': 'reason',
	# }
	# ]
}

6、上架设备审核
通过2筛选未上架和未审核设备，admin在其页面提交是否通过审核
Method:POST
URL: /boss/device/audit
Request:{
	'audit': True/False,
	'commit': ''# 具体回复
}
Response:{}
7、统计信息？再说吧
Method:GET
URL: /boss/device/filter
QueryParam:
{
	'available': True/False,	# 目前可用的 false表示filter不包含该选项
	'unavailable': True/False,	# 目前被占用的
	'devicename': '',
	'owner':'',
	'applicant':'',
}
Response:{}





学院师生：
1.1发送邮件：
Method:GET//后台存储email<->验证码关系
URL：/logon
QueryParam:{
	'email':'12306@qq.com'
}
Response:
{
	'state': 'email已经发送'/'email发送失败，请检查格式'
}

1.2提交注册内容：
Method:POST
URL：/logon
Request:{
	'username':'fzr18'
	'email':'12306@qq.com'
	'code':'yanzhengma'
	'password':'12306'
}
Response:
{
	'state': '注册成功'/'注册失败'
}

1.3登录：
Method:POST
URL：/login
Request:{
	'username':'fzr18'
	'password':'12306'
}
Response:
{
	'username':'fzr18'
	'identity': 'normal'/'renter'/'admin',
	'token': 'token'
}

2.1浏览上架设备信息：
Method:GET
URL：/user/device/list
QueryParam:
{
	'page': 1
	'size': 20
	'deviceid': '101' //设备标识符
	'devicename': '设备名称' //可选
}
Response:
{
	'total':'101',
	'devicelist':[
	{
		'deviceid': '1' //设备唯一标识id
		'devicename': '自动机',
		'owner': 'fzr18',
		'phone': '188888888888'//owner's phone
		'user': 'yxr18',
		'rentout': 'True'/'False',
		'start': '2018年1月1日',  //借用开始时间
		'due': '2018年1月1日',  //借用结束时间
		'location': '东主楼',
		'addtion': '备注'
	}
	]
}

3用户申请借设备
Method:GET
URL：/user/device/lend
QueryParam:
{
	'deviceid': '101' //设备标识符
}

4用户查看借设备记录
Method:GET
URL：/user/device/history
QueryParam:
{
	'page': 1
	'size': 20
}
Response:
{
	'total':'101',
	'devicelist':[
	{
		'orderid': '1' //申请唯一标识id
		'devicename': '自动机',
		'owner': 'fzr18',
		'applicant': 'yxr18',
		'start':'2018年1月1日',
		'due': '2018年1月1日',  //借用结束时间
		'location': '东主楼',
		'addtion': '备注',
		'state': 0/审核通过 1/未审核 2/审核未通过 
	}
	]
}

5看到已借设备
Method:GET
URL：/user/device/own
QueryParam:
{
	'page': 1
	'size': 20
}
Response:
{
	'total':'101',
	'devicelist':[
	{
		'orderid': '1' //申请唯一标识id
		'devicename': '自动机',
		'owner': 'fzr18',
		'applicant': 'yxr18',
		'start':'2018年1月1日',
		'due': '2018年1月1日',  //借用结束时间，前端对即将到期的设备给出提示
		'location': '东主楼',
		'addtion': '备注',
	}
	]
}


设备提供者：
1具有普通用户权限
2.1查询己方设备
2.2增加己方设备
2.3删除设备：
2.4上架设备：
2.5下架设备：
3需要平台支持审核普通用户的设备租借申请，普通用户在填写必要的登
记信息（例如用途、归还日期等，可自行设计，合理即可）之后，可以
对尚未借出的设备申请租借，而设备提供者可以查看所有对己方设备的
租借申请和申请方信息，并同意或拒绝申请，审核后对应的申请用户可
以收到审核结果；
4需要平台支持管理所有已借出设备历史信息，包括查看已借出的设备信
息、设备的归还情况等，同时对归还的设备进行确认归还操作等等。













