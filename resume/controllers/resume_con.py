from odoo import http
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal
import base64

class Resume(CustomerPortal):
    @http.route(['/resume'], type="http", auth="user", website="True")
    def generate_resume(self):
        return request.render("resume.resume_create")

    # @route(['/'])
    @http.route(['/create/resume'], methods=['POST'], type="http", auth="user", )
    def create_resume(self, **post):
        image = post.get('image')
        data = {
            'photo':base64.b64encode(image.read()),
            'name':  post['name'],
            'category':  post['category'],
            'email': post.get('mail'),
            'resume_name': post['resume_name'],
            'father_name': post['fname'],
            'date_of_birth': post['date_of_birth'],
            'template': post['template'],
            'creator': post['login'],
            'phone': post['phone'],
            'address': post['address'],
        }
        result = request.env['resume.model'].sudo().create(data)
        if result:
            return request.redirect("/resume")

    @route(['/detail-resume/<int:id>'], type='http', auth="user", website=True)
    def showResume(self,id,**kw):
        data = request.env['resume.model'].sudo().search([('id','=',id)])
        return  request.render('resume.ResumeDetail',{'data':data})
    #
    @route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        resume = request.env['resume.model'].sudo().search([('creator','=',request.env.user.login)])
        # values = self._prepare_portal_layout_values()
        data = {
            'resume': resume,
        }
        return request.render("portal.portal_my_home", data)
