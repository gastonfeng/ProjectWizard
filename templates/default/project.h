#ifndef {{ config['project_uname'] }}_H
#define {{ config['project_uname'] }}_H

#include "{{ config['project_lname'] }}_global.h"

class {{ config['project_uname'] }}SHARED_EXPORT {{ config['project_name'] }}
{

public:
    {{ config['project_name'] }}();
};

#endif // {{ project_uname }}_H
