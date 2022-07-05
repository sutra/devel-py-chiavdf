PORTNAME=	chiavdf
PORTVERSION=	1.0.6
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	zhoushuqun@gmail.com
COMMENT=	Chia VDF utilities

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools_scm>=3.5.0:devel/py-setuptools_scm@${PY_FLAVOR} \
	${PYTHON_SITELIBDIR}/pybind11:devel/py-pybind11@${PY_FLAVOR}
TEST_DEPENDS=	mypy:devel/py-mypy@${PY_FLAVOR} \
	flake8:devel/py-flake8@${PY_FLAVOR} \
	py.test:devel/py-pytest@${PY_FLAVOR}

USES=	python
USE_PYTHON=	autoplist concurrent distutils

#PYDISTUTILS_INSTALLARGS+=       --skip-build

USE_GITHUB=	yes
GH_ACCOUNT=	Chia-Network

post-extract:
# Remove extraneous unused files to prevent confusion
	@${RM} ${WRKSRC}/pyproject.toml

.include <bsd.port.mk>
