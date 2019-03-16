"""
###　解释来自百度百科 ###
UDP：UDP 是User Datagram Protocol的简称， 中文名是用户数据报协议，是OSI（Open System Interconnection，开放式系统互联） 
    参考模型中一种无连接的传输层协议，提供面向事务的简单不可靠信息传送服务，IETF RFC 768是UDP的正式规范。
    UDP在IP报文的协议号是17。
    UDP协议全称是用户数据报协议，在网络中它与TCP协议一样用于处理数据包，是一种无连接的协议。
    在OSI模型中，在第四层——传输层，处于IP协议的上一层。UDP有不提供数据包分组、组装和不能对数据包进行排序的缺点，
    也就是说，当报文发送之后，是无法得知其是否安全完整到达的。UDP用来支持那些需要在计算机之间传输数据的网络应用。
    包括网络视频会议系统在内的众多的客户/服务器模式的网络应用都需要使用UDP协议。
    UDP协议从问世至今已经被使用了很多年，虽然其最初的光彩已经被一些类似协议所掩盖，
    但是即使是在今天UDP仍然不失为一项非常实用和可行的网络传输层协议。
TCP：TCP（Transmission Control Protocol 传输控制协议）
    是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC 793定义。
FTP：文件传输协议（英文：File Transfer Protocol，缩写：FTP）是用于在网络上进行文件传输的一套标准协议，
    使用客户/服务器模式。它属于网络传输协议的应用层。
    文件传送（file transfer）和文件访问（file access）之间的区别在于：前者由FTP提供，
    后者由如NFS等应用系统提供。
HTTP：超文本传输协议（HTTP，HyperText Transfer Protocol)是互联网上应用最为广泛的一种网络协议。
    所有的WWW文件都必须遵守这个标准。
HTTPS：HTTPS（全称：Hyper Text Transfer Protocol over Secure Socket Layer 
    或 Hypertext Transfer Protocol Secure，超文本传输安全协议），
    是以安全为目标的HTTP通道，简单讲是HTTP的安全版。
SMTP：简单邮件传输协议 (Simple Mail Transfer Protocol, SMTP) 是在Internet传输email的事实标准。
"""