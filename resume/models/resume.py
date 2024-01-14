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
    lang =fields.Char(string="Language")

    edu_ids = fields.One2many('resume.edu','edu_id',string="Education",)
    exp_ids = fields.One2many('resume.exp','exp_id',string="Experience")

class ResumeEducation(models.Model):
    _name = 'resume.edu'
    _description =  'Resume Experience'

    edu_id = fields.Many2one('resume.model',string="Resume Model")
    yrs = fields.Char("From years - To years")
    degree = fields.Char("Degree")
    college = fields.Char("University/College")


class ResumeExperience(models.Model):
    _name = 'resume.exp'
    _description = 'Resume Experience'

    exp_id = fields.Many2one("resume.model",string="Resume Model")
    yrs = fields.Char("From years - To years")
    company = fields.Char("Company")
    position = fields.Char("Position")
    description = fields.Text("Description")

    # yrs1 = fields.Char("From years - To years")
    # company1 = fields.Char("Company")
    # position1 = fields.Char("Position")
    # description1 = fields.Text("Description")
    #
    # yrs2 = fields.Char("From years - To years")
    # company2 = fields.Char("Company")
    # position2 = fields.Char("Position")
    # description2 = fields.Text("Description")