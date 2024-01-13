{
    "name": "Create Resume",
    "author": "Developer",
    "version": "16.0.1",
    "category": "Create Resume & Template",
    "license": "LGPL-3",
    "summary": "Create Resume",
    "depends": ['base','website'],
    "data": [
        'security/ir.model.access.csv',
        'controllers/create_resume.xml',
        'views/resume_views.xml',
        'views/portal_template.xml',
        'views/resume_details.xml',
    ],
    'demo': [],
    "applications":True,
    "auto_install": False,
    'installable': True,
    'assets':{
        'web.assets_frontend':[
            'resume/static/src/templates/*',
            'resume/static/src/js/*',
        ]
    }
}
