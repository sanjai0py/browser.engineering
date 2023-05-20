# Sockets API

There are 2 types of **sockets**

1. Network socket
2. Unix Domain sockets (used to let programes running on a computer communicate)

## socket.socket()

this function creates an endpoint for communication it accepts **3** arguments **Domain, Type, Protocol**

The socket family - Domain
Determines whether you want a socket that works over the Internet or a local one. More specifically, you can have IPv4-based sockets, IPv6-based sockets or UNIX sockets.

A socket configured as IPv4 or IPv6 can exchange data with remote hosts. The former works with IP addresses version 4, the latter works with IP addresses version 6. A socket configured as UNIX is used to exchange data between programs on the same machine. Windows, a non-UNIX operating system, recently added support for the UNIX socket type.

The socket type - Type
Determines the type of communication you want to establish. Here the choice boils down to three types: stream sockets for connection-oriented protocols such as the Transmission Control Protocol (TCP); datagram sockets for connectionless protocols such as the User Datagram Protocol; raw sockets for low-level communication protocols such as the Internet Protocol.

With stream or datagram sockets you are using popular protocols already implemented for you by the operating system. Raw sockets instead allow to do whatever you want: you can implement your own protocols, generate custom IP packets, intercept network traffic or just mess around by sending invalid data to other computers.

Raw sockets are powerful and might cause harm if used for malicious purposes. This is probably the reason why raw sockets on Windows are in read-only mode: you can't send data with them.

The protocol - Protocol
This piece of information is often optional, as sockets can automatically determine how to behave given the family and the type described above. For example a stream, IPv6-based socket is automatically prepared for a TCP-over-IPv6 transmission. Even better, the Berkeley sockets API includes some utility functions to determine the right parameters for the socket configuration given the address you want to connect to.

## Flow chart

[url](https://raw.githubusercontent.com/monocasual/internalpointers-files/master/2021/09/network6/client-server-calls.png)

## HTTP response formate
[url](http://www.tcpipguide.com/free/diagrams/httpresponse.png)

