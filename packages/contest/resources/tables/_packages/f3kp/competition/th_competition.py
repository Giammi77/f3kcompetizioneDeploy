
from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name_competition',width='15em')
        r.fieldcell('contest_director_id',width='10em')
        r.fieldcell('name')
        r.fieldcell('venue')
        r.fieldcell('date')
        r.fieldcell('state_code')

    def th_options(self):
        return dict(partitioned=True)

# class Form(BaseComponent):
#     def th_options(self):
#         return dict(delrow=False,addrow=False)
