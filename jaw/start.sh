#!/bin/sh
service nginx restart
/usr/bin/supervisord -c /etc/supervisor/conf.d/jaw.conf