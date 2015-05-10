#!/usr/bin/env bash


set -u;
set -e;

VERSION="0.0.2";
BUNDLE_ROOT=$(cd "$(dirname "$0")"; pwd);
DIST_ROOT="$BUNDLE_ROOT/dist";


rm -rf $DIST_ROOT/*;


if [ ! -d "$DIST_ROOT" ]; then
	mkdir "$DIST_ROOT";
fi;



#
#
# 1. Create Ubuntu Package (.deb file)
#
#

cd $BUNDLE_ROOT;

if [ -d "$DIST_ROOT/ubuntu" ]; then
	rm -rf "$DIST_ROOT/ubuntu";
fi;

rsync -a ./package/ubuntu/ "$DIST_ROOT/ubuntu/";
mkdir -p "$DIST_ROOT/ubuntu/root/usr/bin/";
mkdir -p "$DIST_ROOT/ubuntu/root/usr/lib/";
rsync -a ./src/ "$DIST_ROOT/ubuntu/root/usr/";

mv $DIST_ROOT/ubuntu/root/usr/bin/howto.py $DIST_ROOT/ubuntu/root/usr/bin/howto;
mv $DIST_ROOT/ubuntu/root/usr/bin/ghow.py $DIST_ROOT/ubuntu/root/usr/bin/ghow;

find "$DIST_ROOT/ubuntu/" -type d -exec chmod 0755 {} \;
find "$DIST_ROOT/ubuntu/" -type f -exec chmod go-w {} \;
# find "$DIST_ROOT/ubuntu/root/usr/lib" -type f -exec chmod 0744 {} \;
chown -R root:root "$DIST_ROOT/ubuntu/";


cd $DIST_ROOT/ubuntu/root;
tar czf $DIST_ROOT/ubuntu/data.tar.gz *;


cd $DIST_ROOT/ubuntu/DEBIAN;
let SIZE=`du -s $DIST_ROOT/ubuntu/root | sed s'/\s\+.*//'`+8
sed s"/SIZE/${SIZE}/" -i ./control;
sed s"/VERSION/${VERSION}/" -i ./control;
tar czf "$DIST_ROOT/ubuntu/control.tar.gz" *;


cd $DIST_ROOT/ubuntu;
echo 2.0 > ./debian-binary;
find $DIST_ROOT/ubuntu/ -type d -exec chmod 0755 {} \;
find $DIST_ROOT/ubuntu/ -type f -exec chmod go-w {} \;
chown -R root:root $DIST_ROOT/ubuntu/;
ar r "$DIST_ROOT/howto-$VERSION.deb" debian-binary control.tar.gz data.tar.gz;



exit 0;

