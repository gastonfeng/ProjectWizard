
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets {% for model in config['qt_library'] %} {{ model['qt'] }}{% endfor %}

#应用程序类型
TEMPLATE = lib

release {
	TARGET = {{ config['project_name'] }}       #指定生成的应用程序名
	OBJECTS_DIR = ./tmp/release #指定目标文件(obj)的存放目录
	DESTDIR += {{config['framework_path']}}/bin/release			#生成文件目录
	#库依赖路径
	LIBS += -L{{config['framework_path']}}/lib/release {% for moudel in config['moudels'] %} -l{{ moudel['lib_name'] }}.lib{% endfor %}
}

debug {
	TARGET = {{config['project_name']}}d     #指定生成的应用程序名
	OBJECTS_DIR = ./tmp/debug #指定目标文件(obj)的存放目录
	DESTDIR += {{config['framework_path']}}/bin/debug			#生成文件目录
	#库依赖路径
	LIBS += -L{{config['framework_path']}}/lib/debug {% for moudel in config['moudels'] %} -l{{ moudel['lib_name'] }}d.lib{% endfor %}
}

#包含路径
INCLUDEPATH += {{config['framework_path']}}/include {% for moudel in config['moudels'] %} {{config['framework_path']}}/include/{{moudel['include_path']}}{% endfor %}

#预定义
DEFINES += QT_DLL {{config['project_uname']}}_LIBRARY

#包含的源文件
SOURCES += {{config['project_name']}}.cpp

#包含的头文件
HEADERS += {{config['project_name']}}.h\
        {{config['project_name']}}_global.h

unix {
    target.path = /usr/lib
    INSTALLS += target
}
