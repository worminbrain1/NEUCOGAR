# Makefile.in generated by automake 1.14.1 from Makefile.am.
# examples/sli/Makefile.  Generated from Makefile.in by configure.

# Copyright (C) 1994-2013 Free Software Foundation, Inc.

# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



VPATH = ../../../__NEST_SOURCE/examples/sli
am__is_gnu_make = test -n '$(MAKEFILE_LIST)' && test -n '$(MAKELEVEL)'
am__make_running_with_option = \
  case $${target_option-} in \
      ?) ;; \
      *) echo "am__make_running_with_option: internal error: invalid" \
              "target option '$${target_option-}' specified" >&2; \
         exit 1;; \
  esac; \
  has_opt=no; \
  sane_makeflags=$$MAKEFLAGS; \
  if $(am__is_gnu_make); then \
    sane_makeflags=$$MFLAGS; \
  else \
    case $$MAKEFLAGS in \
      *\\[\ \	]*) \
        bs=\\; \
        sane_makeflags=`printf '%s\n' "$$MAKEFLAGS" \
          | sed "s/$$bs$$bs[$$bs $$bs	]*//g"`;; \
    esac; \
  fi; \
  skip_next=no; \
  strip_trailopt () \
  { \
    flg=`printf '%s\n' "$$flg" | sed "s/$$1.*$$//"`; \
  }; \
  for flg in $$sane_makeflags; do \
    test $$skip_next = yes && { skip_next=no; continue; }; \
    case $$flg in \
      *=*|--*) continue;; \
        -*I) strip_trailopt 'I'; skip_next=yes;; \
      -*I?*) strip_trailopt 'I';; \
        -*O) strip_trailopt 'O'; skip_next=yes;; \
      -*O?*) strip_trailopt 'O';; \
        -*l) strip_trailopt 'l'; skip_next=yes;; \
      -*l?*) strip_trailopt 'l';; \
      -[dEDm]) skip_next=yes;; \
      -[JT]) skip_next=yes;; \
    esac; \
    case $$flg in \
      *$$target_option*) has_opt=yes; break;; \
    esac; \
  done; \
  test $$has_opt = yes
am__make_dryrun = (target_option=n; $(am__make_running_with_option))
am__make_keepgoing = (target_option=k; $(am__make_running_with_option))
pkgdatadir = $(datadir)/nest
pkgincludedir = $(includedir)/nest
pkglibdir = $(libdir)/nest
pkglibexecdir = $(libexecdir)/nest
am__cd = CDPATH="$${ZSH_VERSION+.}$(PATH_SEPARATOR)" && cd
install_sh_DATA = $(install_sh) -c -m 644
install_sh_PROGRAM = $(install_sh) -c
install_sh_SCRIPT = $(install_sh) -c
INSTALL_HEADER = $(INSTALL_DATA)
transform = $(program_transform_name)
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
build_triplet = x86_64-unknown-linux-gnu
host_triplet = x86_64-unknown-linux-gnu
subdir = examples/sli
DIST_COMMON = $(srcdir)/Makefile.in $(srcdir)/Makefile.am
ACLOCAL_M4 = $(top_srcdir)/aclocal.m4
am__aclocal_m4_deps = $(top_srcdir)/acinclude.m4 \
	$(top_srcdir)/configure.ac
am__configure_deps = $(am__aclocal_m4_deps) $(CONFIGURE_DEPENDENCIES) \
	$(ACLOCAL_M4)
mkinstalldirs = $(install_sh) -d
CONFIG_HEADER = $(top_builddir)/libnestutil/config.h
CONFIG_CLEAN_FILES =
CONFIG_CLEAN_VPATH_FILES =
AM_V_P = $(am__v_P_$(V))
am__v_P_ = $(am__v_P_$(AM_DEFAULT_VERBOSITY))
am__v_P_0 = false
am__v_P_1 = :
AM_V_GEN = $(am__v_GEN_$(V))
am__v_GEN_ = $(am__v_GEN_$(AM_DEFAULT_VERBOSITY))
am__v_GEN_0 = @echo "  GEN     " $@;
am__v_GEN_1 = 
AM_V_at = $(am__v_at_$(V))
am__v_at_ = $(am__v_at_$(AM_DEFAULT_VERBOSITY))
am__v_at_0 = @
am__v_at_1 = 
SOURCES =
DIST_SOURCES =
am__can_run_installinfo = \
  case $$AM_UPDATE_INFO_DIR in \
    n|no|NO) false;; \
    *) (install-info --version) >/dev/null 2>&1;; \
  esac
am__vpath_adj_setup = srcdirstrip=`echo "$(srcdir)" | sed 's|.|.|g'`;
am__vpath_adj = case $$p in \
    $(srcdir)/*) f=`echo "$$p" | sed "s|^$$srcdirstrip/||"`;; \
    *) f=$$p;; \
  esac;
am__strip_dir = f=`echo $$p | sed -e 's|^.*/||'`;
am__install_max = 40
am__nobase_strip_setup = \
  srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*|]/\\\\&/g'`
am__nobase_strip = \
  for p in $$list; do echo "$$p"; done | sed -e "s|$$srcdirstrip/||"
am__nobase_list = $(am__nobase_strip_setup); \
  for p in $$list; do echo "$$p $$p"; done | \
  sed "s| $$srcdirstrip/| |;"' / .*\//!s/ .*/ ./; s,\( .*\)/[^/]*$$,\1,' | \
  $(AWK) 'BEGIN { files["."] = "" } { files[$$2] = files[$$2] " " $$1; \
    if (++n[$$2] == $(am__install_max)) \
      { print $$2, files[$$2]; n[$$2] = 0; files[$$2] = "" } } \
    END { for (dir in files) print dir, files[dir] }'
am__base_list = \
  sed '$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;$$!N;s/\n/ /g' | \
  sed '$$!N;$$!N;$$!N;$$!N;s/\n/ /g'
am__uninstall_files_from_dir = { \
  test -z "$$files" \
    || { test ! -d "$$dir" && test ! -f "$$dir" && test ! -r "$$dir"; } \
    || { echo " ( cd '$$dir' && rm -f" $$files ")"; \
         $(am__cd) "$$dir" && rm -f $$files; }; \
  }
am__installdirs = "$(DESTDIR)$(datadir)"
DATA = $(nobase_data_DATA)
am__tagged_files = $(HEADERS) $(SOURCES) $(TAGS_FILES) $(LISP)
DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)
ACLOCAL = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/missing aclocal-1.14
AMTAR = $${TAR-tar}
AM_CFLAGS =   -W -Wall -pedantic -Wno-long-long  -O2 -g -O2 -fopenmp
AM_CXXFLAGS =   -W -Wall -pedantic -Wno-long-long  -O2  -fopenmp
AM_DEFAULT_VERBOSITY = 1
AR = ar
ARFLAGS = 
ARGZ_H = 
AS = 
AUTOCONF = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/missing autoconf
AUTOHEADER = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/missing autoheader
AUTOMAKE = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/missing automake-1.14
AWK = gawk
CC = gcc
CCDEPMODE = depmode=gcc3
CFLAGS = 
CPP = gcc -E
CPPFLAGS = 
CXX = g++
CXXCPP = g++ -E
CXXDEPMODE = depmode=gcc3
CXXFLAGS = 
CXX_AR = ar cru
CYGPATH_W = echo
DEFS = -DHAVE_CONFIG_H
DEPDIR = .deps
DLLTOOL = false
DOXYGEN = /usr/bin/doxygen
DSYMUTIL = 
DUMPBIN = 
ECHO_C = 
ECHO_N = -n
ECHO_T = 
EGREP = /bin/grep -E
EXEEXT = 
EXTRAS_SUBDIRS =  ConnPlotter
FGREP = /bin/grep -F
GREP = /bin/grep
GSL_CFLAGS = 
GSL_CONFIG = /usr/bin/gsl-config
GSL_LIBS = -L/usr/lib -lgsl -lgslcblas -lm
HAVE_CMATH_MAKROS_IGNORED = 
HAVE_DOT = yes
HAVE_ERRNO_IGNORED = 
HAVE_GSL = 
HAVE_INLINE = 
HAVE_ISTREAM = 
HAVE_LIBLTDL = 
HAVE_MPI = 
HAVE_MUSIC = 
HAVE_M_E = 
HAVE_M_PI = 
HAVE_OSTREAM = 
HAVE_PYTHON = 
HAVE_READLINE = 
HAVE_SIGUSR_IGNORED = 
HAVE_SSTREAM = 
HAVE_STL_VECTOR_CAPACITY_BASE_UNITY = 
HAVE_STL_VECTOR_CAPACITY_DOUBLING = 
HAVE_VAMPIR = 
HELPDIRS = /home/jochen/work/src/nest-simulator/__NEST_SOURCE/libnestutil:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/sli:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/librandom:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/lib:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/lib/sli:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/nestkernel:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/models:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/models/sli:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/precise:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/topology:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/topology/sli:/home/jochen/work/src/nest-simulator/__NEST_SOURCE/nest
HOST = 
INCLTDL = 
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_HELP_LOG = /home/jochen/work/src/nest-simulator/__NEST_BUILD/install-help.log
INSTALL_PROGRAM = ${INSTALL}
INSTALL_SCRIPT = ${INSTALL}
INSTALL_STRIP_PROGRAM = $(install_sh) -c -s
IS_BLUEGENE = 
IS_BLUEGENE_L = 
IS_BLUEGENE_P = 
IS_BLUEGENE_Q = 
IS_K = 
KERNEL = 
LD = /usr/bin/ld -m elf_x86_64
LDFLAGS = 
LIBADD_DL = -ldl 
LIBADD_DLD_LINK = 
LIBADD_DLOPEN = -ldl
LIBADD_SHL_LOAD = 
LIBLTDL = -lltdl
LIBNEUROSIM_INCLUDE = 
LIBNEUROSIM_LIBS = 
LIBNEUROSIM_PY_LIBS = 
LIBOBJS = 
LIBS = -ldl 
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LIPO = 
LN_S = ln -s
LTDLDEPS = 
LTDLINCL = 
LTDLOPEN = libltdl
LTLIBOBJS = 
LT_CONFIG_H = libnestutil/config.h
LT_DLLOADERS =  libltdl/dlopen.la
LT_DLPREOPEN = -dlpreopen libltdl/dlopen.la 
MAINT = #
MAKE = /usr/bin/make
MAKEINFO = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/missing makeinfo
MAKE_FLAGS = 
MANIFEST_TOOL = :
MKDIR_P = /bin/mkdir -p
MPI_INCLUDE = 
MPI_LIBS = 
MUSIC_INCLUDE = 
MUSIC_LIBS = 
NM = /usr/bin/nm -B
NMEDIT = 
OBJDUMP = objdump
OBJEXT = o
OPENMP_CXXFLAGS = -fopenmp
OTOOL = 
OTOOL64 = 
PACKAGE = nest
PACKAGE_BUGREPORT = nest_user@nest-initiative.org
PACKAGE_NAME = nest
PACKAGE_STRING = nest 2.10.0
PACKAGE_TARNAME = nest
PACKAGE_URL = 
PACKAGE_VERSION = 2.10.0
PATH_SEPARATOR = :
PKGBUILDDIR = /home/jochen/work/src/nest-simulator/__NEST_BUILD
PKGDATADIR = ${datarootdir}/nest
PKGDATADIR_AS_CONFIGURED = /home/jochen/opt/nest/share/nest
PKGDOCDIR = ${datarootdir}/doc/nest
PKGDOCDIR_AS_CONFIGURED = /home/jochen/opt/nest/share/doc/nest
PKGSRCDIR = /home/jochen/work/src/nest-simulator/__NEST_SOURCE
PYEXECDIR = ${exec_prefix}/lib/python2.7/site-packages
PYNEST_CPPFLAGS = -I/usr/include/python2.7
PYNEST_CXXFLAGS = -fno-strict-aliasing
PYNEST_SUBDIR = pynest
PYTHON = /usr/bin/python
PYTHON_EXEC_PREFIX = ${exec_prefix}
PYTHON_PLATFORM = linux2
PYTHON_PREFIX = ${prefix}
PYTHON_VERSION = 2.7
RANLIB = ranlib
SED = /bin/sed
SET_MAKE = 
SHELL = /bin/bash
SLI_CXXBACKEND = 
SLI_DIST_SUBDIRS = libnestutil sli librandom lib nestkernel models precise topology nest conngen pynest
SLI_EXITCODE_ABORT = 134
SLI_EXITCODE_SEGFAULT = 139
SLI_LIBS =   -lcurses -lreadline
SLI_MAJOR = 2
SLI_MINOR = 10
SLI_MODULES_LDADD =  /home/jochen/work/src/nest-simulator/__NEST_BUILD/models/libmodelsmodule.la /home/jochen/work/src/nest-simulator/__NEST_BUILD/precise/libprecisemodule.la /home/jochen/work/src/nest-simulator/__NEST_BUILD/topology/libtopologymodule.la
SLI_PATCHLEVEL = 0
SLI_PREFIX = /home/jochen/opt/nest
SLI_PRGNAME = nest-2.10.0
SLI_SUBDIRS = libnestutil sli librandom lib nestkernel models precise topology nest
SLI_THREAD_DEFS = 
SLI_USER_MODULES_LDADD = 
SLI_VERSION = 2.10.0
STRIP = strip
TESTSUITE_BASEDIR = /home/jochen/opt/nest/share/doc/nest
VAMPIR_CFLAGS = 
VAMPIR_LIBS = 
VERSION = 2.10.0
abs_builddir = /home/jochen/work/src/nest-simulator/__NEST_BUILD/examples/sli
abs_srcdir = /home/jochen/work/src/nest-simulator/__NEST_BUILD/../__NEST_SOURCE/examples/sli
abs_top_builddir = /home/jochen/work/src/nest-simulator/__NEST_BUILD
abs_top_srcdir = /home/jochen/work/src/nest-simulator/__NEST_BUILD/../__NEST_SOURCE
ac_ct_AR = ar
ac_ct_CC = gcc
ac_ct_CXX = g++
ac_ct_DUMPBIN = 
am__include = include
am__leading_dot = .
am__quote = 
am__tar = tar --format=ustar -chf - "$$tardir"
am__untar = tar -xf -
bindir = ${exec_prefix}/bin
build = x86_64-unknown-linux-gnu
build_alias = 
build_cpu = x86_64
build_os = linux-gnu
build_vendor = unknown
builddir = .
configure_bluegene = no
datadir = ${datarootdir}/doc/nest/examples
datarootdir = ${prefix}/share
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
host = x86_64-unknown-linux-gnu
host_alias = 
host_cpu = x86_64
host_os = linux-gnu
host_vendor = unknown
htmldir = ${docdir}
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = ${SHELL} /home/jochen/work/src/nest-simulator/__NEST_SOURCE/install-sh
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
ltdl_LIBOBJS =  lt__strl.o
ltdl_LTLIBOBJS =  lt__strl.lo
mandir = ${datarootdir}/man
mkdir_p = $(MKDIR_P)
oldincludedir = /usr/include
pdfdir = ${docdir}
pkgpyexecdir = ${pyexecdir}/nest
pkgpythondir = ${pythondir}/nest
prefix = /home/jochen/opt/nest
program_transform_name = s,x,x,
psdir = ${docdir}
pyexecdir = ${exec_prefix}/lib/python2.7/site-packages
pythondir = ${prefix}/lib/python2.7/site-packages
rp = 
sbindir = ${exec_prefix}/sbin
sharedstatedir = ${prefix}/com
srcdir = ../../../__NEST_SOURCE/examples/sli
subdirs =  libltdl
sys_symbol_underscore = no
sysconfdir = ${prefix}/etc
target_alias = 
top_build_prefix = ../../
top_builddir = ../..
top_srcdir = ../../../__NEST_SOURCE
nobase_data_DATA = \
	nestrc.sli

all: all-am

.SUFFIXES:
$(srcdir)/Makefile.in: # $(srcdir)/Makefile.am  $(am__configure_deps)
	@for dep in $?; do \
	  case '$(am__configure_deps)' in \
	    *$$dep*) \
	      ( cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh ) \
	        && { if test -f $@; then exit 0; else break; fi; }; \
	      exit 1;; \
	  esac; \
	done; \
	echo ' cd $(top_srcdir) && $(AUTOMAKE) --foreign examples/sli/Makefile'; \
	$(am__cd) $(top_srcdir) && \
	  $(AUTOMAKE) --foreign examples/sli/Makefile
.PRECIOUS: Makefile
Makefile: $(srcdir)/Makefile.in $(top_builddir)/config.status
	@case '$?' in \
	  *config.status*) \
	    cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh;; \
	  *) \
	    echo ' cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe)'; \
	    cd $(top_builddir) && $(SHELL) ./config.status $(subdir)/$@ $(am__depfiles_maybe);; \
	esac;

$(top_builddir)/config.status: $(top_srcdir)/configure $(CONFIG_STATUS_DEPENDENCIES)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh

$(top_srcdir)/configure: # $(am__configure_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(ACLOCAL_M4): # $(am__aclocal_m4_deps)
	cd $(top_builddir) && $(MAKE) $(AM_MAKEFLAGS) am--refresh
$(am__aclocal_m4_deps):

mostlyclean-libtool:
	-rm -f *.lo

clean-libtool:
	-rm -rf .libs _libs
install-nobase_dataDATA: $(nobase_data_DATA)
	@$(NORMAL_INSTALL)
	@list='$(nobase_data_DATA)'; test -n "$(datadir)" || list=; \
	if test -n "$$list"; then \
	  echo " $(MKDIR_P) '$(DESTDIR)$(datadir)'"; \
	  $(MKDIR_P) "$(DESTDIR)$(datadir)" || exit 1; \
	fi; \
	$(am__nobase_list) | while read dir files; do \
	  xfiles=; for file in $$files; do \
	    if test -f "$$file"; then xfiles="$$xfiles $$file"; \
	    else xfiles="$$xfiles $(srcdir)/$$file"; fi; done; \
	  test -z "$$xfiles" || { \
	    test "x$$dir" = x. || { \
	      echo " $(MKDIR_P) '$(DESTDIR)$(datadir)/$$dir'"; \
	      $(MKDIR_P) "$(DESTDIR)$(datadir)/$$dir"; }; \
	    echo " $(INSTALL_DATA) $$xfiles '$(DESTDIR)$(datadir)/$$dir'"; \
	    $(INSTALL_DATA) $$xfiles "$(DESTDIR)$(datadir)/$$dir" || exit $$?; }; \
	done

uninstall-nobase_dataDATA:
	@$(NORMAL_UNINSTALL)
	@list='$(nobase_data_DATA)'; test -n "$(datadir)" || list=; \
	$(am__nobase_strip_setup); files=`$(am__nobase_strip)`; \
	dir='$(DESTDIR)$(datadir)'; $(am__uninstall_files_from_dir)
tags TAGS:

ctags CTAGS:

cscope cscopelist:


distdir: $(DISTFILES)
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='$(DISTFILES)'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d "$(distdir)/$$file"; then \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -fpR $(srcdir)/$$file "$(distdir)$$dir" || exit 1; \
	      find "$(distdir)/$$file" -type d ! -perm -700 -exec chmod u+rwx {} \;; \
	    fi; \
	    cp -fpR $$d/$$file "$(distdir)$$dir" || exit 1; \
	  else \
	    test -f "$(distdir)/$$file" \
	    || cp -p $$d/$$file "$(distdir)/$$file" \
	    || exit 1; \
	  fi; \
	done
check-am: all-am
check: check-am
all-am: Makefile $(DATA)
installdirs:
	for dir in "$(DESTDIR)$(datadir)"; do \
	  test -z "$$dir" || $(MKDIR_P) "$$dir"; \
	done
install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	if test -z '$(STRIP)'; then \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	      install; \
	else \
	  $(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	    install_sh_PROGRAM="$(INSTALL_STRIP_PROGRAM)" INSTALL_STRIP_FLAG=-s \
	    "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'" install; \
	fi
mostlyclean-generic:

clean-generic:

distclean-generic:
	-test -z "$(CONFIG_CLEAN_FILES)" || rm -f $(CONFIG_CLEAN_FILES)
	-test . = "$(srcdir)" || test -z "$(CONFIG_CLEAN_VPATH_FILES)" || rm -f $(CONFIG_CLEAN_VPATH_FILES)

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
clean: clean-am

clean-am: clean-generic clean-libtool mostlyclean-am

distclean: distclean-am
	-rm -f Makefile
distclean-am: clean-am distclean-generic

dvi: dvi-am

dvi-am:

html: html-am

html-am:

info: info-am

info-am:

install-data-am: install-nobase_dataDATA

install-dvi: install-dvi-am

install-dvi-am:

install-exec-am:

install-html: install-html-am

install-html-am:

install-info: install-info-am

install-info-am:

install-man:

install-pdf: install-pdf-am

install-pdf-am:

install-ps: install-ps-am

install-ps-am:

installcheck-am:

maintainer-clean: maintainer-clean-am
	-rm -f Makefile
maintainer-clean-am: distclean-am maintainer-clean-generic

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-generic mostlyclean-libtool

pdf: pdf-am

pdf-am:

ps: ps-am

ps-am:

uninstall-am: uninstall-nobase_dataDATA

.MAKE: install-am install-strip

.PHONY: all all-am check check-am clean clean-generic clean-libtool \
	cscopelist-am ctags-am distclean distclean-generic \
	distclean-libtool distdir dvi dvi-am html html-am info info-am \
	install install-am install-data install-data-am install-dvi \
	install-dvi-am install-exec install-exec-am install-html \
	install-html-am install-info install-info-am install-man \
	install-nobase_dataDATA install-pdf install-pdf-am install-ps \
	install-ps-am install-strip installcheck installcheck-am \
	installdirs maintainer-clean maintainer-clean-generic \
	mostlyclean mostlyclean-generic mostlyclean-libtool pdf pdf-am \
	ps ps-am tags-am uninstall uninstall-am \
	uninstall-nobase_dataDATA


# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
