#!/bin/bash

make clean 2> /dev/null

tmp_files=( \
	".deps/" \
	"Makefile" \
	"config.h" \
	"config.log" \
	"config.status" \
	"include/Makefile" \
	"include/event2/event-config.h" \
	"libevent.pc" \
	"libevent_openssl.pc" \
	"libevent_pthreads.pc" \
	"libtool" \
	"sample/Makefile" \
	"stamp-h1" \
	"test/.deps/" \
	"test/Makefile" \
	"test/test-script.sh" \
)
for f in "${tmp_files[@]}"
do
	rm -rv $f 2> /dev/null
done
