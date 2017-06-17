#########################################################################
# vim: ts=8 sw=8
#########################################################################
# Author:   tf135c (James Reynolds)
# Filename: Makefile
# Date:     2006-11-30 07:31:27
#########################################################################
# Note that we use '::' rules to allow multiple rule sets for the same
# target.  Read that as "modularity exemplarized".
#########################################################################

PREFIX	:=${DESTDIR}${HOME}/opt
BINDIR	=${PREFIX}/bin

TARGETS	=all clean distclean clobber check install uninstall tags
TARGET	=all

SUBDIRS	=

.PHONY:	${TARGETS} ${SUBDIRS}

all::	FIXME

${TARGETS}::

clean::
	${RM} a.out *.o core.* lint tags

distclean clobber:: clean

check::	FIXME
	./FIXME ${ARGS}

install:: FIXME
	install -d ${BINDIR}
	install -c FIXME ${BINDIR}/

uninstall::
	${RM} ${BINDIR}/FIXME

# ${TARGETS}::
# 	${MAKE} TARGET=$@ ${SUBDIRS}

# ${SUBDIRS}::
# 	${MAKE} -C $@ ${TARGET}
