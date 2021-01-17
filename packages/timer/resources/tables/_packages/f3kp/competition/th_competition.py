
from gnr.web.gnrbaseclasses import BaseComponent
class View(BaseComponent):

    # def th_struct(self,struct):
    #     r = struct.view().rows()
    #     r.fieldcell('name_competition',width='15em')
    #     r.fieldcell('contest_director_id',width='10em')
    #     r.fieldcell('name')
    #     r.fieldcell('venue')
    #     r.fieldcell('date')
    #     r.fieldcell('state_code')

    def th_options(self):
        return dict(partitioned=True)

class Form(BaseComponent):
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='15%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb = top.formbuilder(margin_left='20px',margin_right='30px'
                            ,cols=4,cols_width='auto',fld_width='90%')
        fb.field('name')
        fb.field('venue')
        fb.field('date')
        fb.field('state_code')
        fb.field('short_note',colspan=3)
        fb.field('preparation_time') #,validate_notnull=True lo fa solo in questa form o in quelle ereditate?
        fb.field('audio_path')
        self.registration(center_tb)
        self.competition_task(center_tb)
        self.combination(center_tb)
        self.ranking(center_tb)
        self.managment(center_tb)
        self.play_list(center_tb)
        self.competition_informations(center_tb)
    
    def play_list(self,tc):
        pane=tc.contentPane(title='!![en]Play List').ckeditor(value='^#FORM.record.play_list')