#ifndef {{ config['project_uname'] }}_GLOBAL_H
#define {{ config['project_uname'] }}_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined {{ config['project_uname'] }}_LIBRARY
#  define {{ config['project_uname'] }}SHARED_EXPORT Q_DECL_EXPORT
#else
#  define {{ config['project_uname'] }}SHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // {{ config['project_uname'] }}_GLOBAL_H
