from odoo import  fields,models,api

class  ResumeModel(models.Model):
    _name = 'resume.model'
    _description = 'Resume Model'

    name = fields.Char(string="Name")
    resume_name = fields.Char(string="Resume Name")
    category = fields.Char(string="Category")
    email = fields.Char(string="Email")
    photo = fields.Binary(string="Photo")
    father_name= fields.Char(string="Father's Name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Datetime(string="Date of Birth")
    template = fields.Selection([('one','one'),('two','two'),('three','three')])
    creator=fields.Char(string="Resume Creator")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")