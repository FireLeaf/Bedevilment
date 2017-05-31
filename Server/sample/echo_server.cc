#include <stdlib.h>
#include <string.h>

#include <arpa/inet.h>
#include <sys/socket.h>

#include <iostream>

#include <event2/event.h>
#include <event2/listener.h>

void accept_conn_cb(struct evconnlistener *listener, evutil_socket_t fd,
	struct sockaddr *addr, int len, void *ptr)
{
	struct event_base *base = evconnlistener_get_base(listener);
	std::cout << "accept a link" << std::endl;
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

	event_base_dispatch(base);
	return 0;
}

