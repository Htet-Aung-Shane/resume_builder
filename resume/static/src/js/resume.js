/* @odoo-module */
import publicWidget from '@web/legacy/js/public/public_widget'


publicWidget.registry.resumeTemplate = publicWidget.Widget.extend({
    selector:'#resume_cat',
//    template:'resume.TemplateOne',

   init: function () {
      this._super(...arguments);
   },
    start:function(){
        $( "#click_cat" ).on( "click", function() {
          $('#resume_information').removeClass('d-none')
          $('#resume_cat').addClass("d-none")
        } );

        $( "#click_resume_info" ).on( "click", function() {
          $('#resume_temp').removeClass('d-none')
          $('#resume_information').addClass("d-none")
          $('#resume_cat').addClass("d-none")
        } );
//       this.renderElement();
    }

})
https://www.odoo.com/sl_SI/forum/pomoc-1/how-to-print-download-report-from-website-121485