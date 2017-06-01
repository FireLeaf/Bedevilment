#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <assert.h>

#include <arpa/inet.h>
#include <sys/socket.h>

#include <iostream>

#include <event2/event.h>
#include <event2/listener.h>
#include <event2/buffer.h>
#include <event2/bufferevent.h>

void echo_read_cb(struct bufferevent *bev, void *ctx)
{
	// 获取bufferevent中的读和写的指针
	struct evbuffer *input  = bufferevent_get_input(bev);
	struct evbuffer *output = bufferevent_get_output(bev);
	// 把读到的数据复制到写内存
	evbuffer_add_buffer(output, input);
}
void echo_event_cb(struct bufferevent *bev, short events, void *ctx)
{
	if (events & BEV_EVENT_ERROR)
		perror("Error from bufferevent");
	if (events & (BEV_EVENT_EOF | BEV_EVENT_ERROR))
		bufferevent_free(bev);
}
void accept_conn_cb(struct evconnlistener *listener, evutil_socket_t fd,
	struct sockaddr *address, int socklen, void *ctx)
{
	// 初始化一个bufferevent用于数据的写入和读取
	// 首先需要从listener中获取event_base
	struct event_base *base = evconnlistener_get_base(listener);
	struct bufferevent *bev = bufferevent_socket_new(base, fd, BEV_OPT_CLOSE_ON_FREE);
	// 设置bufferevent的回调函数
	bufferevent_setcb(bev, echo_read_cb, nullptr, echo_event_cb, nullptr);
	// 启用bufferevent的读和写
	bufferevent_enable(bev, EV_READ | EV_WRITE);
}
void accept_error_cb(struct evconnlistener *listener, void *ctx)
{
	struct event_base *base = evconnlistener_get_base(listener);
	int err = EVUTIL_SOCKET_ERROR();
	assert(false);
	event_base_loopexit(base, nullptr);
}

int main(int argc, char **argv)
{
	struct event_base *base = event_base_new();
	struct sockaddr_in sin;
	memset(&sin, 0, sizeof(sin));
	sin.sin_family      = AF_INET;
	sin.sin_addr.s_addr = htonl(0);
	sin.sin_port        = htons(7513);

	struct evconnlistener *listener = evconnlistener_new_bind(
		base, accept_conn_cb, nullptr, 
		LEV_OPT_CLOSE_ON_FREE | LEV_OPT_REUSEABLE,
		-1, (struct sockaddr *)&sin, sizeof(sin));

	evconnlistener_set_error_cb(listener, accept_error_cb);

	event_base_dispatch(base);
	return 0;
}

