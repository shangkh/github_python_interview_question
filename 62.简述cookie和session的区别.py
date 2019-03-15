"""
1.session在服务器端，cookie在客户端（浏览器）
2.session的运行依赖session id，而session id 也会失效，
    存储session是，键与cookie中的session id相同，
    值是开发人员设置的键值对信息，进行base64编码，
    过期时间由开发人员设置
3.cookie安全性比session差
"""