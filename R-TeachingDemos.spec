#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-TeachingDemos
Version  : 2.12
Release  : 29
URL      : https://cran.r-project.org/src/contrib/TeachingDemos_2.12.tar.gz
Source0  : https://cran.r-project.org/src/contrib/TeachingDemos_2.12.tar.gz
Summary  : Demonstrations for Teaching and Learning
Group    : Development/Tools
License  : Artistic-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n TeachingDemos
cd %{_builddir}/TeachingDemos

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589519091

%install
export SOURCE_DATE_EPOCH=1589519091
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TeachingDemos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TeachingDemos
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library TeachingDemos
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc TeachingDemos || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/TeachingDemos/DESCRIPTION
/usr/lib64/R/library/TeachingDemos/INDEX
/usr/lib64/R/library/TeachingDemos/Meta/Rd.rds
/usr/lib64/R/library/TeachingDemos/Meta/data.rds
/usr/lib64/R/library/TeachingDemos/Meta/features.rds
/usr/lib64/R/library/TeachingDemos/Meta/hsearch.rds
/usr/lib64/R/library/TeachingDemos/Meta/links.rds
/usr/lib64/R/library/TeachingDemos/Meta/nsInfo.rds
/usr/lib64/R/library/TeachingDemos/Meta/package.rds
/usr/lib64/R/library/TeachingDemos/NAMESPACE
/usr/lib64/R/library/TeachingDemos/NEWS
/usr/lib64/R/library/TeachingDemos/R/TeachingDemos
/usr/lib64/R/library/TeachingDemos/R/TeachingDemos.rdb
/usr/lib64/R/library/TeachingDemos/R/TeachingDemos.rdx
/usr/lib64/R/library/TeachingDemos/data/Rdata.rdb
/usr/lib64/R/library/TeachingDemos/data/Rdata.rds
/usr/lib64/R/library/TeachingDemos/data/Rdata.rdx
/usr/lib64/R/library/TeachingDemos/help/AnIndex
/usr/lib64/R/library/TeachingDemos/help/TeachingDemos.rdb
/usr/lib64/R/library/TeachingDemos/help/TeachingDemos.rdx
/usr/lib64/R/library/TeachingDemos/help/aliases.rds
/usr/lib64/R/library/TeachingDemos/help/paths.rds
/usr/lib64/R/library/TeachingDemos/html/00Index.html
/usr/lib64/R/library/TeachingDemos/html/R.css
